import csv
import os
from typing import Optional, Dict, Any


def compute_sample_stats(sample_path: Optional[str] = None,
                         column: Optional[int | str] = None,
                         delimiter: str = ',',
                         has_header: bool = True) -> Dict[str, Dict[str, Any]]:
    """Read `sample_data.csv` (or provided path) and compute mean/min/max/count.

    Args:
        sample_path: path to CSV file. If None, looks for 'sample_data.csv' next to this file.
        column: If provided, either an int index (0-based) or a header name (str) to compute only that column.
        delimiter: CSV delimiter.
        has_header: whether the CSV has a header row.

    Returns:
        A mapping column_name -> {"mean", "min", "max", "count"}.
    """
    if sample_path is None:
        sample_path = os.path.join(os.path.dirname(__file__), 'sample_data.csv')

    cols: Dict[int, list] = {}
    headers = None

    with open(sample_path, newline='', encoding='utf-8') as fh:
        reader = csv.reader(fh, delimiter=delimiter)
        if has_header:
            try:
                headers = next(reader)
            except StopIteration:
                return {}

        for row in reader:
            for i, cell in enumerate(row):
                if i not in cols:
                    cols[i] = []
                if cell is None:
                    continue
                cell = cell.strip()
                if cell == "":
                    continue
                try:
                    val = float(cell)
                except Exception:
                    continue
                cols[i].append(val)

    def col_name(i: int) -> str:
        if headers and i < len(headers):
            return headers[i]
        return str(i)

    # resolve requested indices
    requested_indices = None
    if column is not None:
        if isinstance(column, int):
            requested_indices = [column]
        else:
            # try integer-like string
            try:
                requested_indices = [int(column)]
            except Exception:
                if headers is None:
                    raise ValueError("column name requested but file has no header")
                try:
                    requested_indices = [headers.index(column)]
                except ValueError:
                    raise ValueError(f"column '{column}' not found in header")

    indices = requested_indices if requested_indices is not None else sorted(cols.keys())

    result: Dict[str, Dict[str, Any]] = {}
    for i in indices:
        values = cols.get(i, [])
        if not values:
            result[col_name(i)] = {"mean": None, "min": None, "max": None, "count": 0}
        else:
            s = sum(values)
            cnt = len(values)
            result[col_name(i)] = {"mean": s / cnt, "min": min(values), "max": max(values), "count": cnt}

    return result


if __name__ == '__main__':
    # quick demo using the bundled sample_data.csv
    import argparse
    import json

    parser = argparse.ArgumentParser(description='Compute mean/min/max for sample_data.csv')
    parser.add_argument('-c', '--column', help='column name or index')
    parser.add_argument('--no-header', dest='has_header', action='store_false')
    parser.add_argument('-d', '--delimiter', default=',')
    parser.add_argument('--path', help='path to csv file (optional)')
    args = parser.parse_args()

    col = None
    if args.column is not None:
        try:
            col = int(args.column)
        except Exception:
            col = args.column

    stats = compute_sample_stats(sample_path=args.path, column=col, delimiter=args.delimiter, has_header=args.has_header)
    print(json.dumps(stats, indent=2))
