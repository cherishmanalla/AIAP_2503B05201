import math
from typing import List, Tuple, Optional


def _parse_numbers(tokens: List[str]) -> List[float]:
    """Parse tokens as floats."""
    nums: List[float] = []
    for t in tokens:
        nums.append(float(t))
    return nums


def area_for_shape(shape: str, args: List[float]) -> float:
    """Compute area for a supported shape.

    Supported shapes and arguments (numbers expected):
      - circle r                  -> pi * r^2
      - rectangle w h             -> w * h
      - square s                  -> s^2
      - triangle base height      -> 0.5 * base * height
      - ellipse a b               -> pi * a * b
      - trapezoid a b height      -> 0.5 * (a + b) * height

    Raises ValueError for unknown shapes or wrong argument counts.
    """
    s = shape.lower()
    if s == "circle":
        if len(args) != 1:
            raise ValueError("circle requires 1 argument: radius")
        r = args[0]
        return math.pi * r * r
    if s == "rectangle":
        if len(args) != 2:
            raise ValueError("rectangle requires 2 arguments: width height")
        return args[0] * args[1]
    if s == "square":
        if len(args) != 1:
            raise ValueError("square requires 1 argument: side")
        return args[0] * args[0]
    if s == "triangle":
        if len(args) != 2:
            raise ValueError("triangle requires 2 arguments: base height")
        return 0.5 * args[0] * args[1]
    if s == "ellipse":
        if len(args) != 2:
            raise ValueError("ellipse requires 2 arguments: a b")
        return math.pi * args[0] * args[1]
    if s == "trapezoid":
        if len(args) != 3:
            raise ValueError("trapezoid requires 3 arguments: a b height")
        return 0.5 * (args[0] + args[1]) * args[2]

    raise ValueError(f"unsupported shape: {shape}")


def calculate_areas_from_lines(lines: List[str]) -> List[Tuple[str, Optional[float], Optional[str]]]:
    """Parse a list of lines describing shapes and return area results.

    Returns a list of tuples: (original_line, area or None on error, error_message or None)

    Lines are expected to be of the form:
        shape_name num num ...
    Blank lines and lines starting with '#' are ignored.
    """
    results: List[Tuple[str, Optional[float], Optional[str]]] = []
    for raw in lines:
        line = raw.strip()
        if not line or line.startswith('#'):
            # skip empty/comment lines
            continue
        parts = line.split()
        shape = parts[0]
        try:
            nums = _parse_numbers(parts[1:])
            area = area_for_shape(shape, nums)
            results.append((line, area, None))
        except Exception as e:
            results.append((line, None, str(e)))
    return results


if __name__ == '__main__':
    # Demo: no file input required — use a built-in list of shape lines
    import json

    sample_lines = [
        'circle 3',
        'rectangle 4 5',
        'square 6',
        'triangle 3 4',
        'ellipse 2 3',
        'trapezoid 3 4 5',
        'unknown 1 2',
    ]

    out = calculate_areas_from_lines(sample_lines)
    print(json.dumps([{"line": l, "area": a, "error": err} for (l, a, err) in out], indent=2))
