import os
from collections import defaultdict
from itertools import chain
from typing import Dict

import libcst as cst
from libcst.codemod import (
    CodemodContext,
    TransformFailure,
    TransformSkip,
    TransformSuccess,
    diff_code,
    transform_module,
)
from libcst.codemod.visitors import AddImportsVisitor, GatherImportsVisitor
from libcst.helpers import insert_header_comments
from loguru import logger


class GatherClassesVisitor(cst.CSTVisitor):
    def __init__(self) -> None:
        self.classes: Dict[str, list[cst.ClassDef]] = defaultdict(list)

    def visit_ClassDef(self, node: cst.ClassDef) -> None:
        self.classes[node.name.value.lstrip("_")].append(node)


class MergeClassesVisitor(cst.CSTTransformer):
    def __init__(
        self,
        classes: Dict[str, list[cst.ClassDef]],
    ) -> None:
        self.classes = classes

    def leave_ClassDef(
        self, original_node: cst.ClassDef, updated_node: cst.ClassDef
    ) -> cst.ClassDef:
        uitbreiding_classes = self.classes.pop(original_node.name.value, None)
        for uitbreiding_class in uitbreiding_classes or []:
            logger.debug(f"Class {original_node.name.value} uitbreiden")
            updated_node = updated_node.with_deep_changes(
                updated_node.body,
                body=list(chain(updated_node.body.body, uitbreiding_class.body.body)),
            )
        return updated_node

    def leave_Module(
        self,
        original_node: cst.Module,
        updated_node: cst.Module,
    ) -> cst.Module:
        new_body = list(updated_node.body)

        for key, uitbreiding_classes in self.classes.items():
            for uitbreiding_class in uitbreiding_classes:
                # Remove the leading underscore from the class name
                class_name_without_prefix = uitbreiding_class.name.value.lstrip("_")
                updated_class_def = uitbreiding_class.with_changes(
                    name=cst.Name(class_name_without_prefix)
                )
                new_body.append(updated_class_def)

        return updated_node.with_changes(body=new_body)


uitbreidingen_folder = os.path.join(
    "woningwaardering", "vera", "bvg", "model_uitbreidingen"
)

files = [
    f
    for f in os.listdir(uitbreidingen_folder)
    if os.path.isfile(os.path.join(uitbreidingen_folder, f)) and f.endswith(".py")
]

uitbreidingen_visitor = GatherClassesVisitor()

codemod_context = CodemodContext()
import_visitor = GatherImportsVisitor(codemod_context)

for f in files:
    with open(os.path.join(uitbreidingen_folder, f), "r") as uitbreidingen_file:
        uitbreidingen_source = uitbreidingen_file.read()
        uitbreidingen_module = cst.parse_module(uitbreidingen_source)

        uitbreidingen_module.visit(uitbreidingen_visitor)
        uitbreidingen_module.visit(import_visitor)

generated_file_path = "woningwaardering/vera/bvg/generated.py"

with open(generated_file_path, "r") as generated_file:
    generated_source = generated_file.read()
    generated_module = cst.parse_module(generated_source)
    merge_classes_visitor = MergeClassesVisitor(classes=uitbreidingen_visitor.classes)
    updated_module = generated_module.visit(merge_classes_visitor)

    class_diff = diff_code(generated_source, updated_module.code, 3)

    if class_diff is not None:
        updated_module = insert_header_comments(
            updated_module,
            [
                "# bewerk dit bestand niet met de hand",
                "# VERA classes zijn aangepast met de uitbreidingen in woningwaardering/vera/bvg/model_uitbreidingen",
            ],
        )

        generated_visitor = GatherClassesVisitor()
        updated_module.visit(generated_visitor)

        for module in import_visitor.module_imports:
            if module in generated_visitor.classes.keys():
                logger.debug(
                    f"`import {module}` wordt niet toegevoegd. Een class met deze naam bestaat al."
                )
            else:
                AddImportsVisitor.add_needed_import(
                    codemod_context,
                    module,
                )

        for module, objects in import_visitor.object_mapping.items():
            for obj in objects:
                if obj in generated_visitor.classes.keys():
                    logger.debug(
                        f"`from {module} import {obj}` wordt niet toegevoegd. Een class met deze naam bestaat al."
                    )
                else:
                    AddImportsVisitor.add_needed_import(
                        codemod_context,
                        module=module,
                        obj=obj,
                    )

        for module, import_aliases in import_visitor.alias_mapping.items():
            for obj, asname in import_aliases:
                if asname in generated_visitor.classes.keys():
                    logger.debug(
                        f"`from {module} import {obj} as {asname}` wordt niet toegevoegd. Een class met deze naam bestaat al."
                    )
                else:
                    AddImportsVisitor.add_needed_import(
                        codemod_context,
                        module=module,
                        obj=obj,
                        asname=asname,
                    )

        add_imports_visitor = AddImportsVisitor(codemod_context)

        result_source = updated_module.code

        transform_result = transform_module(add_imports_visitor, result_source)

        if isinstance(transform_result, TransformSuccess):
            result_source = transform_result.code
        elif isinstance(transform_result, TransformFailure):
            logger.error(
                f"Er heeft zich een fout voorgedaan bij het transformeren van imports: {transform_result.error}"
            )
        elif isinstance(transform_result, TransformSkip):
            logger.warning(
                f"Het transformeren van imports is overgeslagen: {transform_result.skip_description}"
            )

        result_diff = diff_code(generated_source, result_source, 3)
        file_names = '", "'.join(files)

        with open(generated_file_path, "w") as generated_file:
            generated_file.write(result_source)
        logger.success(
            f'Uitbreidingen uit "{file_names}" verwerkt in {generated_file_path}.'
        )
        logger.debug(f"Dit zijn de doorgevoerde wijzigingen:\n{result_diff}")
