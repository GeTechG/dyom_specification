#!/usr/bin/env python3
"""
Main script to generate DYOM specification documentation.

Run this script to export the DYOM mission file specification to:
- JSON Schema
- Markdown documentation (single or multi-file)
- HTML documentation (single or multi-file)

Usage:
    python generate_docs.py              # Generate single-file documentation
    python generate_docs.py --multi      # Generate multi-file documentation
"""

import argparse
from pathlib import Path
from exporters import export_all
from models import Mission


def main():
    """Generate all specification documentation."""
    parser = argparse.ArgumentParser(
        description="Generate DYOM specification documentation"
    )
    parser.add_argument(
        '--multi',
        action='store_true',
        help="Generate multi-file documentation (separate files for each type)"
    )
    args = parser.parse_args()

    # Configure output directory
    output_dir = Path(__file__).parent / "output"

    # Generate all formats
    export_all(
        model=Mission,
        output_dir=output_dir,
        base_name="dyom_specification",
        multi_file=args.multi
    )

    print("\nYou can now:")
    print(f"   - View JSON Schema: {output_dir / 'dyom_specification.json'}")

    if args.multi:
        print(f"   - View Markdown: {output_dir / 'markdown' / 'index.md'}")
        print(f"   - Open HTML in browser: {output_dir / 'html' / 'index.html'}")
    else:
        print(f"   - View Markdown: {output_dir / 'dyom_specification.md'}")
        print(f"   - Open HTML in browser: {output_dir / 'dyom_specification.html'}")


if __name__ == "__main__":
    main()
