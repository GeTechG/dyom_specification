# DYOM Mission File Specification

A comprehensive Python-based specification system for DYOM (Design Your Own Mission) mission files. This project uses Pydantic models to define the complete structure of DYOM missions and provides exporters to generate documentation in multiple formats.

## Features

- **Complete type-safe Python models** using Pydantic for all DYOM mission components
- **22 objective types** fully documented and validated
- **Built-in validation** for all mission data including bitfield flags and enums
- **JSON Schema export** for integration with other tools and code generation
- **Multi-file documentation** with separate pages for each model type
- **Markdown documentation** for readable specifications
- **HTML documentation** with styled, browser-viewable docs and sidebar navigation

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
from models import (
    Mission,
    MissionInfo,
    InitialSettings,
    PlayerInitial,
    ObjectiveCheckpoint,
    ObjectiveActor,
    Actor,
    CheckpointShape
)

# Create a mission
mission = Mission(
    mission=MissionInfo(
        name="My First Mission",
        author="Creator Name",
        intro_text_1="Welcome to my mission",
        intro_text_2="Get ready for action",
        intro_text_3="",
        sound_filename="",
        published=False
    ),
    initial=InitialSettings(
        timelimit=0,
        day_time=12,
        weather=0,
        wanted_level_min=0,
        wanted_level_max=6,
        flags=0,
        player=PlayerInitial(
            interior=0,
            position_x=2488.56,
            position_y=-1666.84,
            position_z=12.38,
            direction=0.0,
            skin=0,
            health=100,
            weapon=0,
            ammo=1000000
        )
    ),
    objectives=[
        ObjectiveCheckpoint(
            position_x=2500.0,
            position_y=-1700.0,
            position_z=13.0,
            radius=2.0,
            interior=0,
            objective_type=2,
            shape=CheckpointShape.BEACON,
            radar_marker=4,
            direction=0.0,
            text="Go to the marker!"
        ),
        ObjectiveActor(
            position_x=2510.0,
            position_y=-1710.0,
            position_z=13.0,
            direction=90.0,
            interior=0,
            objective_type=5,
            skin=102,
            weapon=30,
            ammo=500,
            health=100,
            accuracy=75,
            radar_marker=0,
            flags=0,
            animation=-1,
            animation_argument=0,
            text="Kill the enemy!"
        )
    ],
    actors=[],
    cars=[],
    pickups=[],
    objects=[]
)

# Validate and export to JSON
mission_json = mission.model_dump_json(indent=2)
print(mission_json)

# Access specific objective type
if isinstance(mission.objectives[0], ObjectiveCheckpoint):
    print(f"Checkpoint radius: {mission.objectives[0].radius}")
```

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


## License

This specification system is provided as-is for documenting DYOM mission files.

## Related Resources

- DYOM official resources
- GTA San Andreas modding documentation
- Pydantic documentation: https://docs.pydantic.dev/