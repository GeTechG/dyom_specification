# DYOM Mission File Specification

A Python-based specification system for DYOM (Design Your Own Mission) mission files. This project uses Pydantic models to define the structure of DYOM missions and provides exporters to generate documentation in multiple formats.

## Features

- **Type-safe Python models** using Pydantic for DYOM mission structure
- **Validation** built-in validation for all mission data
- **JSON Schema export** for integration with other tools
- **Markdown documentation** for readable specifications
- **HTML documentation** with styled, browser-viewable docs

## Installation

1. Install Python 3.7 or higher

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Generate Documentation

Run the main script to generate all documentation formats:

**Single-file mode** (all content in one file):
```bash
python generate_docs.py
```

This will create three files in the `output/` directory:
- `dyom_specification.json` - JSON Schema
- `dyom_specification.md` - Markdown documentation
- `dyom_specification.html` - HTML documentation

**Multi-file mode** (separate file for each type, easier to navigate):
```bash
python generate_docs.py --multi
```

This will create:
- `output/dyom_specification.json` - JSON Schema
- `output/markdown/` - Multiple Markdown files with index
  - `index.md` - Main index with links to all types
  - `DYOMMission.md` - Root model documentation
  - `Actor.md`, `Vehicle.md`, etc. - Individual type documentation
- `output/html/` - Multiple HTML files with sidebar navigation
  - `index.html` - Main index page
  - `DYOMMission.html` - Root model page
  - Individual HTML pages for each type with persistent sidebar

### Using the Models in Your Code

```python
from models import Mission, MissionInfo, Position, Objective

# Create a mission
mission = Mission(
    info=MissionInfo(
        title="My First Mission",
        author="Creator Name",
        description="An exciting mission"
    ),
    player_start_position=Position(x=0.0, y=0.0, z=3.0),
    objectives=[
        Objective(
            id=1,
            type="goto",
            description="Go to the marker",
            position=Position(x=100.0, y=100.0, z=3.0),
            required=True
        )
    ]
)

# Validate and export to JSON
mission_json = mission.model_dump_json(indent=2)
print(mission_json)
```

## Project Structure

```
dyom_specification/
├── models.py           # Pydantic models defining DYOM structure
├── exporters.py        # Export functions for JSON/Markdown/HTML
├── generate_docs.py    # Main script to generate documentation
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── output/            # Generated documentation (created on first run)
```

## Customizing the Specification

The specification is defined in `models.py`. To customize it:

1. **Add new fields** to existing models by adding class attributes
2. **Add new models** by creating new classes that inherit from `BaseModel`
3. **Add enums** for constrained string values
4. **Update documentation** by modifying docstrings and field descriptions

Example of adding a new field:

```python
class MissionInfo(BaseModel):
    title: str = Field(..., description="Mission title")
    author: str = Field(..., description="Mission creator's name")
    # Add your new field here
    release_date: Optional[str] = Field(None, description="Release date (YYYY-MM-DD)")
```

After making changes, run `generate_docs.py` to regenerate all documentation.

## Model Structure Overview

The main model hierarchy:

- **DYOMMission** (root)
  - **MissionInfo** - Basic metadata (title, author, description)
  - **MissionSettings** - Global settings (weather, time, player stats)
  - **Position** - 3D coordinates
  - **Rotation** - Rotation angles
  - **Actor** - NPCs/pedestrians
  - **Vehicle** - Vehicles
  - **Objective** - Mission objectives
  - **Cutscene** - Cutscene sequences

## Export Formats

### JSON Schema
Standard JSON Schema (draft-07) that can be used for:
- Validation in other languages
- IDE autocompletion
- API documentation
- Code generation

### Markdown
Human-readable documentation with:
- **Single-file mode**: All content in one file with table of contents
- **Multi-file mode**: Separate file for each type with cross-references
- Field descriptions
- Type information
- Required/optional markers
- Default values

### HTML
Styled web documentation with:
- **Single-file mode**: All content in one scrollable page
- **Multi-file mode**: Separate pages with persistent sidebar navigation
- Modern, responsive design
- Color-coded types and fields
- Easy navigation
- Professional appearance

**Tip**: Use multi-file mode (`--multi` flag) for large specifications to reduce context size and improve navigation.

## Contributing

To extend this specification:

1. Update the models in `models.py`
2. Add appropriate type hints and descriptions
3. Run `generate_docs.py` to verify the output
4. Check all three export formats (JSON, MD, HTML)

## License

This specification system is provided as-is for documenting DYOM mission files.

## Related Resources

- DYOM official resources (add links as needed)
- GTA San Andreas modding documentation
- Pydantic documentation: https://docs.pydantic.dev/
