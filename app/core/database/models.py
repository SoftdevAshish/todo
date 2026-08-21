import importlib
import pathlib
from ast import parse, ClassDef
from pathlib import Path


def discover_models() -> list[str]:
    path = pathlib.Path(__file__).parent.parent.parent / "features"
    models = []

    for folder in path.iterdir():
        if not folder.is_dir():
            continue
        for file in folder.rglob("*.py"):
            if file.name == "__init__.py":
                continue
            read_file = parse(file.read_text("utf-8"), filename=str(file))
            for node in read_file.body:
                if isinstance(node, ClassDef):
                    for base in node.bases:
                        if getattr(base, "id", None) == "Base":
                            models.append({
                                "model": node.name,
                                "path": file.name,
                                "module": get_module_from_file(file),
                            })
    return models


def get_module_from_file(file: Path) -> str:
    relative = file.relative_to((pathlib.Path(__file__).parent.parent.parent / "features").parent.parent)

    return ".".join(relative.with_suffix("").parts)


def load_models():
    all_models = discover_models()
    for model in all_models:
        importlib.import_module(model["module"])
