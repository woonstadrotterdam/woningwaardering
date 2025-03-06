import difflib
import importlib
import warnings
from loguru import logger
import pytest
from pathlib import Path
from woningwaardering.vera.bvg.generated import EenhedenEenheid

def get_test_cases():
    """Scan for test case folders containing pairs of .py and .json files"""
    base_path = Path("docs/implementatietoelichtingen/voorbeelden")
    test_cases = []
    
    # Iterate through housing type directories
    for stelsel_dir in base_path.iterdir():
        if not stelsel_dir.is_dir():
            continue
            
        stelsel = stelsel_dir.name  # e.g., "zelfstandige_woonruimten"
        
        # Iterate through case folders in the housing type directory
        for stelselgroep_dir in stelsel_dir.iterdir():
            if not stelselgroep_dir.is_dir():
                continue
                
            # Look for all Python files in the folder
            python_files = list(stelselgroep_dir.glob("*.py"))
            
            # Convert folder name to class name (e.g., 'energieprestatie' -> 'Energieprestatie')
            stelselgroep_class_name = stelselgroep_dir.name.replace('_', ' ').title().replace(' ', '')
            
            for python_file in python_files:
                # For each Python file, check if there's a matching JSON file
                base_name = python_file.stem
                json_file = stelselgroep_dir / f"{base_name}.json"
                
                if json_file.exists():
                    test_cases.append({
                        'stelsel': stelsel,
                        'folder': stelselgroep_dir,
                        'python_file': python_file,
                        'json_file': json_file,
                        'class_name': stelselgroep_class_name,
                        'id': f"{stelsel}/{stelselgroep_dir.name}/{base_name}"
                    })
    
    return test_cases

# Helper functions to reduce code duplication
def get_pydantic_instance(test_case):
    """Get the Pydantic instance from the Python file"""
    spec = importlib.util.spec_from_file_location(test_case['python_file'].stem, test_case['python_file'])
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.get_eenheid()

def get_json_instance(test_case):
    """Get the JSON-parsed instance"""
    with open(test_case['json_file'], "r") as f:
        json_data = f.read()
        return EenhedenEenheid.model_validate_json(json_data)

def get_stelselgroep(test_case):
    """Get the appropriate validator class"""
    stelsel = test_case['stelsel']
    import_path = f"woningwaardering.stelsels.{stelsel}"
    module = __import__(import_path, fromlist=[test_case['class_name']])
    return getattr(module, test_case['class_name'])

# For test_pydantic_validation
@pytest.mark.parametrize(
    "test_case", 
    get_test_cases(), 
    ids=lambda case: f"{case['id']} - Pydantic input"
)
def test_pydantic(test_case):
    pydantic_instance = get_pydantic_instance(test_case)
    stelselgroep = get_stelselgroep(test_case)
    
    with warnings.catch_warnings(record=True) as warning_list:
        logger.enable("woningwaardering")
        stelselgroep().waardeer(pydantic_instance)
        assert len(warning_list) == 0, f"{[str(w.message) for w in warning_list]}"

# For test_json_validation
@pytest.mark.parametrize(
    "test_case", 
    get_test_cases(), 
    ids=lambda case: f"{case['id']} - JSON input"
)
def test_json(test_case):
    """Test that the JSON instance can be validated"""
    json_instance = get_json_instance(test_case)
    stelselgroep = get_stelselgroep(test_case)
    
    with warnings.catch_warnings(record=True) as warning_list:
        logger.enable("woningwaardering")
        stelselgroep().waardeer(json_instance)
        assert len(warning_list) == 0, f"{[str(w.message) for w in warning_list]}"

# For test_pydantic_equals_json
@pytest.mark.parametrize(
    "test_case", 
    get_test_cases(), 
    ids=lambda case: f"{case['id']} - Vergelijken Pydantic en JSON"
)
def test_pydantic_equals_json(test_case):
    """Test that the Pydantic and JSON instances are equivalent"""
    pydantic_instance = get_pydantic_instance(test_case)
    json_instance = get_json_instance(test_case)
    
    py_json = pydantic_instance.model_dump_json(indent=2, exclude_none=True)
    js_json = json_instance.model_dump_json(indent=2, exclude_none=True)
        
    if py_json != js_json:        
        # Get dictionaries from both instances for detailed comparison
        difflines = list(
            difflib.unified_diff(
                fromfile="verwacht",
                tofile="testresultaat",
                a=py_json.split("\n"),
                b=js_json.split("\n"),
                lineterm="",
                n=3,
            )
        )

        diff = "\n".join(difflines)

        # Fail with detailed message
        pytest.fail(diff)
