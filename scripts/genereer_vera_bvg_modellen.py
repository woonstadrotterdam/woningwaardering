from pathlib import Path
from urllib.parse import urlparse

import tomli
from datamodel_code_generator import (
    DataModelType,
    InputFileType,
    PythonVersion,
    generate,
)


def generate_models() -> None:
    """
    Genereert de Pydantic modellen voor de VERA BVG API.
    """

    with open("pyproject.toml", "rb") as f:
        pyproject_data = tomli.load(f)

        woningwaardering_data = pyproject_data.get("tool", {}).get(
            "woningwaardering", {}
        )
        version = woningwaardering_data.get("datasources", {}).get("vera-openapi", {})

    url = urlparse(
        f"https://raw.githubusercontent.com/Aedes-datastandaarden/vera-openapi/{version}/docs/Ketenprocessen/BVG.yaml"
    )

    output = Path("woningwaardering/vera/bvg/generated.py")

    generate(
        url,
        input_file_type=InputFileType.OpenAPI,
        output=output,
        output_model_type=DataModelType.PydanticV2BaseModel,
        target_python_version=PythonVersion.PY_310,
        use_standard_collections=True,
        use_default_kwarg=True,
        use_field_description=True,
        snake_case_field=True,
        disable_timestamp=True,
        use_double_quotes=True,
        allow_population_by_field_name=True,
        use_title_as_name=True,
        field_include_all_keys=True,
        collapse_root_models=True,
    )


if __name__ == "__main__":
    generate_models()
