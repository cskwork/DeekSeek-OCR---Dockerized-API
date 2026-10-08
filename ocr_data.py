"""Parse OCR coordinate and diagram literals as data."""
import ast
import math


def _numbers(values, size=None):
    if not isinstance(values, (list, tuple)) or (size is not None and len(values) != size):
        raise ValueError("Expected a numeric coordinate sequence")
    if any(type(value) not in (int, float) or (type(value) is float and not math.isfinite(value)) for value in values):
        raise ValueError("Coordinates must be finite numbers")
    return values


def parse_boxes(text):
    boxes = ast.literal_eval(text)
    if not isinstance(boxes, (list, tuple)):
        raise ValueError("Expected a sequence of bounding boxes")
    for box in boxes:
        _numbers(box, 4)
    return boxes


def parse_point(text):
    return _numbers(ast.literal_eval(text), 2)


def parse_diagram(text):
    diagram = ast.literal_eval(text)
    if not isinstance(diagram, dict):
        raise ValueError("Expected a diagram dictionary")
    return diagram


def parse_radii(values):
    return _numbers(values)
