import os
import re


uitbreidingen_folder = os.path.join(
    "woningwaardering", "vera", "bvg", "model_uitbreidingen"
)

files = [
    f
    for f in os.listdir(uitbreidingen_folder)
    if os.path.isfile(os.path.join(uitbreidingen_folder, f)) and f.endswith(".py")
]

class_file_dict = {}
for f in files:
    with open(os.path.join(uitbreidingen_folder, f), "r") as file:
        content = file.read()
        matches = re.findall(r"class _(.*?)Uitbreiding(?=\(BaseModel\))", content)
        for match in matches:
            class_file_dict[match] = f.replace(".py", "")

generated_file_path = "woningwaardering/vera/bvg/generated.py"

with open(generated_file_path, "r") as file:
    generated = file.read()

for class_naam, file_naam in class_file_dict.items():
    pattern = re.escape(class_naam) + r"\(BaseModel\)"
    uitbreiding = "_" + class_naam + "Uitbreiding"
    vervanging = class_naam + r"(" + uitbreiding + r")"
    if re.search(pattern, generated):
        generated = re.sub(pattern, vervanging, generated)
    else:
        raise ValueError(f"Class {class_naam} not found in generated.py")

    import_statement = f"from woningwaardering.vera.bvg.model_uitbreidingen.{file_naam} import {uitbreiding}\n"

    class_def = re.search(r"\n\nclass .*:", generated)

    if class_def:
        generated = (
            generated[: class_def.start()]
            + import_statement
            + generated[class_def.start() :]
        )

with open(generated_file_path, "w") as file:
    file.write(generated)
