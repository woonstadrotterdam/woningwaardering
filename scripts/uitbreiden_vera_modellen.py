from collections import defaultdict
from typing import Dict
from itertools import chain
import libcst as cst
from libcst.helpers import insert_header_comments
from libcst.codemod import diff_code
import os

from loguru import logger


class GatherClassesVisitor(cst.CSTVisitor):
    def __init__(self) -> None:
        self.classes: Dict[str, list[cst.ClassDef]] = defaultdict(list)

    def visit_ClassDef(self, node: cst.ClassDef) -> None:
        self.classes[node.name.value.lstrip("_")].append(node)


class MergeClassesVisitor(cst.CSTTransformer):
    def __init__(self, classes: Dict[str, list[cst.ClassDef]]) -> None:
        self.classes: Dict[str, list[cst.ClassDef]] = classes

    def leave_ClassDef(
        self, original_node: cst.ClassDef, updated_node: cst.ClassDef
    ) -> cst.ClassDef:
        uitbreiding_classes = self.classes.get(original_node.name.value)
        for uitbreiding_class in uitbreiding_classes or []:
            logger.debug(f"Class {original_node.name.value} uitbreiden")
            updated_node = updated_node.with_deep_changes(
                updated_node.body,
                body=list(chain(updated_node.body.body, uitbreiding_class.body.body)),
            )
        return updated_node


uitbreidingen_folder = os.path.join(
    "woningwaardering", "vera", "bvg", "model_uitbreidingen"
)

files = [
    f
    for f in os.listdir(uitbreidingen_folder)
    if os.path.isfile(os.path.join(uitbreidingen_folder, f)) and f.endswith(".py")
]

uitbreidingen_visitor = GatherClassesVisitor()

for f in files:
    with open(os.path.join(uitbreidingen_folder, f), "r") as uitbreidingen_file:
        uitbreidingen_source = uitbreidingen_file.read()
        uitbreidingen_module = cst.parse_module(uitbreidingen_source)

        uitbreidingen_classes = uitbreidingen_module.visit(uitbreidingen_visitor)

generated_file_path = "woningwaardering/vera/bvg/generated.py"

with open(generated_file_path, "r") as generated_file:
    generated_source = generated_file.read()
    generated_module = cst.parse_module(generated_source)
    generated_visitor = MergeClassesVisitor(classes=uitbreidingen_visitor.classes)
    updated_module = generated_module.visit(generated_visitor)

    updated_source = updated_module.code

    diff = diff_code(generated_source, updated_source, 3)

    if diff is not None:
        file_names = '", "'.join(files)
        updated_module = insert_header_comments(
            updated_module,
            [
                "# bewerk dit bestand niet met de hand",
                "# VERA classes zijn aangepast met de uitbreidingen in woningwaardering/vera/bvg/model_uitbreidingen",
            ],
        )
        with open(generated_file_path, "w") as generated_file:
            generated_file.write(updated_module.code)
        logger.success(
            f'Uitbreidingen uit "{file_names}" verwerkt in {generated_file_path}.'
        )
        logger.debug(f"De wijzigingen zijn:\n{diff}")
