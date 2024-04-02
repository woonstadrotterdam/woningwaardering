if __name__ == "__main__":
    import re

    file_path = "woningwaardering/vera/bvg/generated.py"

    uitbreidingen = ["EenhedenRuimte"]

    with open(file_path, "r") as file:
        generated = file.read()

    for class_naam in uitbreidingen:
        pattern = re.escape(class_naam) + r"\(BaseModel\)"
        uitbreiding = "_" + class_naam
        replacement = class_naam + r"(" + uitbreiding + r")"
        generated = re.sub(pattern, replacement, generated)

    with open(file_path, "w") as file:
        file.write(generated)
