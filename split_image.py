#!/usr/bin/env python3
"""Split a grid of sub-images into individual files.

Usage:
    python split_image.py input.png
    python split_image.py input.png --rows 2 --cols 4
    python split_image.py input.png --rows 4 --cols 2 --output-dir ./crops
"""

import argparse
from pathlib import Path
from PIL import Image


def find_splits(size, gaps, min_gap=3):
    """Given a list of gap positions (indices where a gap exists), return split
    points (start, end) for each non-gap segment."""
    splits = []
    start = 0
    in_gap = True
    for i in range(size):
        is_gap = gaps[i]
        if not is_gap and in_gap:
            start = i
            in_gap = False
        elif is_gap and not in_gap:
            if i - start >= min_gap:
                splits.append((start, i))
            in_gap = True
    if not in_gap and size - start >= min_gap:
        splits.append((start, size))
    return splits


def auto_detect_grid(img, threshold=240, gap_ratio=0.8):
    """Auto-detect sub-image grid by scanning for gaps (rows/cols of mostly
    uniform background)."""
    gray = img.convert("L")
    w, h = gray.size
    pixels = gray.load()

    # Detect horizontal gaps (rows)
    row_gaps = [False] * h
    for y in range(h):
        bright = sum(1 for x in range(w) if pixels[x, y] > threshold)
        if bright > w * gap_ratio:
            row_gaps[y] = True

    # Detect vertical gaps (columns)
    col_gaps = [False] * w
    for x in range(w):
        bright = sum(1 for y in range(h) if pixels[x, y] > threshold)
        if bright > h * gap_ratio:
            col_gaps[x] = True

    y_splits = find_splits(h, row_gaps)
    x_splits = find_splits(w, col_gaps)

    if not y_splits or not x_splits:
        return None

    grid = []
    for y0, y1 in y_splits:
        row = []
        for x0, x1 in x_splits:
            row.append((x0, y0, x1, y1))
        grid.append(row)
    return grid


def split_image(input_path, rows=None, cols=None, output_dir=None, prefix=None):
    img = Image.open(input_path)
    w, h = img.size

    if rows and cols:
        # Manual grid
        cell_w = w // cols
        cell_h = h // rows
        grid = []
        for r in range(rows):
            row = []
            for c in range(cols):
                row.append((c * cell_w, r * cell_h, (c + 1) * cell_w, (r + 1) * cell_h))
            grid.append(row)
    else:
        # Auto-detect
        grid = auto_detect_grid(img)
        if grid is None:
            print("Auto-detection failed. Specify --rows and --cols manually.")
            return

    out_dir = Path(output_dir or ".")
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = Path(input_path).stem

    print(f"Image: {input_path} ({w}x{h})")
    print(f"Grid: {len(grid)} rows x {len(grid[0])} cols = {len(grid) * len(grid[0])} sub-images")
    print()

    for r, row in enumerate(grid):
        for c, bbox in enumerate(row):
            x0, y0, x1, y1 = bbox
            crop = img.crop(bbox)
            name = f"{stem}_{r+1}_{c+1}.png"
            if prefix:
                name = f"{prefix}_{name}"
            path = out_dir / name
            crop.save(path)
            print(f"  [{r+1},{c+1}] ({x0},{y0})-({x1},{y1}) {crop.size} -> {path}")

    print(f"\nSaved {len(grid) * len(grid[0])} sub-images to {out_dir}/")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Split a grid image into sub-images.")
    ap.add_argument("input", help="Input image path")
    ap.add_argument("--rows", type=int, help="Number of rows (auto-detect if omitted)")
    ap.add_argument("--cols", type=int, help="Number of columns (auto-detect if omitted)")
    ap.add_argument("--output-dir", default="./crops", help="Output directory (default: ./crops)")
    ap.add_argument("--prefix", help="Optional filename prefix")
    args = ap.parse_args()
    split_image(args.input, args.rows, args.cols, args.output_dir, args.prefix)
