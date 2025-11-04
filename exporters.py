"""
Export functionality for DYOM mission specifications.

This module provides functions to export the Pydantic models to various formats:
- JSON Schema
- Markdown documentation
- HTML documentation
"""

import json
from pathlib import Path
from typing import Dict, Any, Type, Optional
from pydantic import BaseModel


def export_json_schema(
    model: Type[BaseModel],
    output_path: Path,
    pretty: bool = True
) -> None:
    """
    Export a Pydantic model to JSON Schema format.

    Args:
        model: The Pydantic model class to export
        output_path: Path where the JSON schema will be saved
        pretty: Whether to format the JSON with indentation
    """
    schema = model.model_json_schema()

    # Add schema metadata
    schema["$schema"] = "http://json-schema.org/draft-07/schema#"

    indent = 2 if pretty else None
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(schema, f, indent=indent, ensure_ascii=False)

    print(f"[OK] JSON Schema exported to: {output_path}")


def _format_field_type(field_info: Dict[str, Any]) -> str:
    """Format field type information from JSON schema."""
    if 'type' in field_info:
        type_str = field_info['type']
        if type_str == 'array' and 'items' in field_info:
            item_type = _format_field_type(field_info['items'])
            return f"Array<{item_type}>"
        elif type_str == 'object':
            return "Object"
        return type_str.capitalize()
    elif 'anyOf' in field_info:
        types = [_format_field_type(t) for t in field_info['anyOf']]
        return " | ".join(types)
    elif '$ref' in field_info:
        ref = field_info['$ref'].split('/')[-1]
        return ref
    elif 'enum' in field_info:
        return f"Enum: {', '.join(repr(e) for e in field_info['enum'])}"
    return "Unknown"


def export_markdown(
    model: Type[BaseModel],
    output_path: Path,
    title: str = "DYOM Mission File Specification"
) -> None:
    """
    Export a Pydantic model to Markdown documentation.

    Args:
        model: The Pydantic model class to export
        output_path: Path where the Markdown will be saved
        title: Title for the documentation
    """
    schema = model.model_json_schema()

    lines = [
        f"# {title}",
        "",
        schema.get('description', 'No description available.'),
        "",
        "## Table of Contents",
        ""
    ]

    # Build table of contents
    if '$defs' in schema:
        for def_name in schema['$defs'].keys():
            lines.append(f"- [{def_name}](#{def_name.lower()})")
        lines.append("")

    # Document the root model
    lines.extend([
        "## Root Model: " + model.__name__,
        "",
        schema.get('description', ''),
        "",
        "### Fields",
        ""
    ])

    if 'properties' in schema:
        for field_name, field_info in schema['properties'].items():
            required = field_name in schema.get('required', [])
            req_badge = " **[Required]**" if required else " *[Optional]*"

            lines.extend([
                f"#### `{field_name}`{req_badge}",
                "",
                f"- **Type:** `{_format_field_type(field_info)}`",
            ])

            if 'description' in field_info:
                lines.append(f"- **Description:** {field_info['description']}")

            if 'default' in field_info:
                lines.append(f"- **Default:** `{field_info['default']}`")

            lines.append("")

    # Document definitions (nested models)
    if '$defs' in schema:
        lines.extend([
            "---",
            "",
            "## Type Definitions",
            ""
        ])

        for def_name, def_schema in schema['$defs'].items():
            lines.extend([
                f"### {def_name}",
                "",
                def_schema.get('description', ''),
                ""
            ])

            if def_schema.get('type') == 'object' and 'properties' in def_schema:
                lines.append("#### Fields")
                lines.append("")

                for field_name, field_info in def_schema['properties'].items():
                    required = field_name in def_schema.get('required', [])
                    req_badge = " **[Required]**" if required else " *[Optional]*"

                    lines.extend([
                        f"##### `{field_name}`{req_badge}",
                        "",
                        f"- **Type:** `{_format_field_type(field_info)}`",
                    ])

                    if 'description' in field_info:
                        lines.append(f"- **Description:** {field_info['description']}")

                    if 'default' in field_info:
                        lines.append(f"- **Default:** `{field_info['default']}`")

                    lines.append("")

            elif def_schema.get('type') == 'string' and 'enum' in def_schema:
                lines.extend([
                    "**Possible values:**",
                    ""
                ])
                for enum_value in def_schema['enum']:
                    lines.append(f"- `{enum_value}`")
                lines.append("")

    # Write to file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

    print(f"[OK] Markdown documentation exported to: {output_path}")


def export_html(
    model: Type[BaseModel],
    output_path: Path,
    title: str = "DYOM Mission File Specification"
) -> None:
    """
    Export a Pydantic model to HTML documentation.

    Args:
        model: The Pydantic model class to export
        output_path: Path where the HTML will be saved
        title: Title for the documentation
    """
    schema = model.model_json_schema()

    html_parts = [
        "<!DOCTYPE html>",
        "<html lang='en'>",
        "<head>",
        "    <meta charset='UTF-8'>",
        "    <meta name='viewport' content='width=device-width, initial-scale=1.0'>",
        f"    <title>{title}</title>",
        "    <style>",
        "        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif; line-height: 1.6; max-width: 1200px; margin: 0 auto; padding: 20px; background: #f5f5f5; }",
        "        .container { background: white; padding: 40px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }",
        "        h1 { color: #2c3e50; border-bottom: 3px solid #3498db; padding-bottom: 10px; }",
        "        h2 { color: #34495e; margin-top: 40px; border-bottom: 2px solid #ecf0f1; padding-bottom: 8px; }",
        "        h3 { color: #2c3e50; margin-top: 30px; }",
        "        h4 { color: #555; margin-top: 20px; margin-bottom: 10px; }",
        "        .field { background: #f8f9fa; padding: 15px; margin: 10px 0; border-left: 4px solid #3498db; border-radius: 4px; }",
        "        .field-name { font-family: 'Courier New', monospace; font-weight: bold; color: #2c3e50; font-size: 1.1em; }",
        "        .required { color: #e74c3c; font-weight: bold; }",
        "        .optional { color: #95a5a6; font-style: italic; }",
        "        .type { color: #8e44ad; font-family: 'Courier New', monospace; }",
        "        .description { color: #555; margin: 8px 0; }",
        "        .default { color: #27ae60; font-family: 'Courier New', monospace; }",
        "        .toc { background: #ecf0f1; padding: 20px; border-radius: 4px; margin: 20px 0; }",
        "        .toc ul { list-style: none; padding-left: 0; }",
        "        .toc li { margin: 8px 0; }",
        "        .toc a { color: #3498db; text-decoration: none; }",
        "        .toc a:hover { text-decoration: underline; }",
        "        .enum-values { background: #fff3cd; padding: 10px; border-radius: 4px; margin: 10px 0; }",
        "        .enum-value { font-family: 'Courier New', monospace; color: #856404; }",
        "        code { background: #e8e8e8; padding: 2px 6px; border-radius: 3px; font-size: 0.9em; }",
        "    </style>",
        "</head>",
        "<body>",
        "    <div class='container'>",
        f"        <h1>{title}</h1>",
        f"        <p>{schema.get('description', '')}</p>",
    ]

    # Table of contents
    if '$defs' in schema:
        html_parts.extend([
            "        <div class='toc'>",
            "            <h2>Table of Contents</h2>",
            "            <ul>",
        ])
        for def_name in schema['$defs'].keys():
            html_parts.append(f"                <li><a href='#{def_name}'>{def_name}</a></li>")
        html_parts.extend([
            "            </ul>",
            "        </div>",
        ])

    # Root model
    html_parts.extend([
        f"        <h2>Root Model: {model.__name__}</h2>",
        f"        <p>{schema.get('description', '')}</p>",
        "        <h3>Fields</h3>",
    ])

    if 'properties' in schema:
        for field_name, field_info in schema['properties'].items():
            required = field_name in schema.get('required', [])
            req_badge = "<span class='required'>[Required]</span>" if required else "<span class='optional'>[Optional]</span>"

            html_parts.extend([
                "        <div class='field'>",
                f"            <div class='field-name'>{field_name} {req_badge}</div>",
                f"            <div><strong>Type:</strong> <span class='type'>{_format_field_type(field_info)}</span></div>",
            ])

            if 'description' in field_info:
                html_parts.append(f"            <div class='description'>{field_info['description']}</div>")

            if 'default' in field_info:
                html_parts.append(f"            <div><strong>Default:</strong> <span class='default'>{field_info['default']}</span></div>")

            html_parts.append("        </div>")

    # Definitions
    if '$defs' in schema:
        html_parts.append("        <h2>Type Definitions</h2>")

        for def_name, def_schema in schema['$defs'].items():
            html_parts.extend([
                f"        <h3 id='{def_name}'>{def_name}</h3>",
                f"        <p>{def_schema.get('description', '')}</p>",
            ])

            if def_schema.get('type') == 'object' and 'properties' in def_schema:
                for field_name, field_info in def_schema['properties'].items():
                    required = field_name in def_schema.get('required', [])
                    req_badge = "<span class='required'>[Required]</span>" if required else "<span class='optional'>[Optional]</span>"

                    html_parts.extend([
                        "        <div class='field'>",
                        f"            <div class='field-name'>{field_name} {req_badge}</div>",
                        f"            <div><strong>Type:</strong> <span class='type'>{_format_field_type(field_info)}</span></div>",
                    ])

                    if 'description' in field_info:
                        html_parts.append(f"            <div class='description'>{field_info['description']}</div>")

                    if 'default' in field_info:
                        html_parts.append(f"            <div><strong>Default:</strong> <span class='default'>{field_info['default']}</span></div>")

                    html_parts.append("        </div>")

            elif def_schema.get('type') == 'string' and 'enum' in def_schema:
                html_parts.append("        <div class='enum-values'>")
                html_parts.append("            <strong>Possible values:</strong>")
                html_parts.append("            <ul>")
                for enum_value in def_schema['enum']:
                    html_parts.append(f"                <li><span class='enum-value'>{enum_value}</span></li>")
                html_parts.append("            </ul>")
                html_parts.append("        </div>")

    html_parts.extend([
        "    </div>",
        "</body>",
        "</html>",
    ])

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(html_parts))

    print(f"[OK] HTML documentation exported to: {output_path}")


def export_markdown_multifile(
    model: Type[BaseModel],
    output_dir: Path,
    title: str = "DYOM Mission File Specification"
) -> None:
    """
    Export a Pydantic model to multiple Markdown files (one per type definition).

    Args:
        model: The Pydantic model class to export
        output_dir: Directory where the Markdown files will be saved
        title: Title for the documentation
    """
    schema = model.model_json_schema()
    output_dir.mkdir(exist_ok=True)

    # Create index file
    index_lines = [
        f"# {title}",
        "",
        schema.get('description', 'No description available.'),
        "",
        "## Documentation Structure",
        "",
        f"- [Root Model: {model.__name__}](./{model.__name__}.md)",
        ""
    ]

    if '$defs' in schema:
        index_lines.append("### Type Definitions")
        index_lines.append("")
        for def_name in schema['$defs'].keys():
            index_lines.append(f"- [{def_name}](./{def_name}.md)")
        index_lines.append("")

    # Write index
    with open(output_dir / "index.md", 'w', encoding='utf-8') as f:
        f.write('\n'.join(index_lines))

    # Create file for root model
    root_lines = [
        f"# {model.__name__}",
        "",
        "[← Back to Index](./index.md)",
        "",
        schema.get('description', ''),
        "",
        "## Fields",
        ""
    ]

    if 'properties' in schema:
        for field_name, field_info in schema['properties'].items():
            required = field_name in schema.get('required', [])
            req_badge = " **[Required]**" if required else " *[Optional]*"

            root_lines.extend([
                f"### `{field_name}`{req_badge}",
                "",
                f"**Type:** `{_format_field_type(field_info)}`",
                ""
            ])

            if 'description' in field_info:
                root_lines.append(field_info['description'])
                root_lines.append("")

            if 'default' in field_info:
                root_lines.append(f"**Default:** `{field_info['default']}`")
                root_lines.append("")

            # Add link to type definition if it's a reference
            if '$ref' in field_info:
                ref_name = field_info['$ref'].split('/')[-1]
                root_lines.append(f"[View {ref_name} definition](./{ref_name}.md)")
                root_lines.append("")

    with open(output_dir / f"{model.__name__}.md", 'w', encoding='utf-8') as f:
        f.write('\n'.join(root_lines))

    # Create file for each definition
    if '$defs' in schema:
        for def_name, def_schema in schema['$defs'].items():
            def_lines = [
                f"# {def_name}",
                "",
                "[← Back to Index](./index.md)",
                "",
                def_schema.get('description', ''),
                ""
            ]

            if def_schema.get('type') == 'object' and 'properties' in def_schema:
                def_lines.append("## Fields")
                def_lines.append("")

                for field_name, field_info in def_schema['properties'].items():
                    required = field_name in def_schema.get('required', [])
                    req_badge = " **[Required]**" if required else " *[Optional]*"

                    def_lines.extend([
                        f"### `{field_name}`{req_badge}",
                        "",
                        f"**Type:** `{_format_field_type(field_info)}`",
                        ""
                    ])

                    if 'description' in field_info:
                        def_lines.append(field_info['description'])
                        def_lines.append("")

                    if 'default' in field_info:
                        def_lines.append(f"**Default:** `{field_info['default']}`")
                        def_lines.append("")

                    # Add link to type definition if it's a reference
                    if '$ref' in field_info:
                        ref_name = field_info['$ref'].split('/')[-1]
                        def_lines.append(f"[View {ref_name} definition](./{ref_name}.md)")
                        def_lines.append("")

            elif def_schema.get('type') == 'string' and 'enum' in def_schema:
                def_lines.extend([
                    "## Possible Values",
                    ""
                ])
                for enum_value in def_schema['enum']:
                    def_lines.append(f"- `{enum_value}`")
                def_lines.append("")

            with open(output_dir / f"{def_name}.md", 'w', encoding='utf-8') as f:
                f.write('\n'.join(def_lines))

    print(f"[OK] Multi-file Markdown documentation exported to: {output_dir}")


def export_html_multifile(
    model: Type[BaseModel],
    output_dir: Path,
    title: str = "DYOM Mission File Specification"
) -> None:
    """
    Export a Pydantic model to multiple HTML files with navigation.

    Args:
        model: The Pydantic model class to export
        output_dir: Directory where the HTML files will be saved
        title: Title for the documentation
    """
    schema = model.model_json_schema()
    output_dir.mkdir(exist_ok=True)

    # Common CSS
    css = """
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif; line-height: 1.6; margin: 0; padding: 0; background: #f5f5f5; }
        .sidebar { position: fixed; left: 0; top: 0; bottom: 0; width: 250px; background: #2c3e50; color: white; overflow-y: auto; padding: 20px; }
        .sidebar h2 { color: #3498db; font-size: 1.2em; margin-top: 0; }
        .sidebar a { color: #ecf0f1; text-decoration: none; display: block; padding: 8px 0; border-left: 3px solid transparent; padding-left: 10px; }
        .sidebar a:hover { background: #34495e; border-left-color: #3498db; }
        .sidebar a.active { background: #34495e; border-left-color: #3498db; font-weight: bold; }
        .content { margin-left: 270px; padding: 40px; }
        .container { background: white; padding: 40px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); max-width: 1000px; }
        h1 { color: #2c3e50; border-bottom: 3px solid #3498db; padding-bottom: 10px; margin-top: 0; }
        h2 { color: #34495e; margin-top: 40px; border-bottom: 2px solid #ecf0f1; padding-bottom: 8px; }
        h3 { color: #2c3e50; margin-top: 30px; }
        .field { background: #f8f9fa; padding: 15px; margin: 10px 0; border-left: 4px solid #3498db; border-radius: 4px; }
        .field-name { font-family: 'Courier New', monospace; font-weight: bold; color: #2c3e50; font-size: 1.1em; }
        .required { color: #e74c3c; font-weight: bold; }
        .optional { color: #95a5a6; font-style: italic; }
        .type { color: #8e44ad; font-family: 'Courier New', monospace; }
        .description { color: #555; margin: 8px 0; }
        .default { color: #27ae60; font-family: 'Courier New', monospace; }
        .enum-values { background: #fff3cd; padding: 10px; border-radius: 4px; margin: 10px 0; }
        .enum-value { font-family: 'Courier New', monospace; color: #856404; }
        code { background: #e8e8e8; padding: 2px 6px; border-radius: 3px; font-size: 0.9em; }
        .back-link { color: #3498db; text-decoration: none; display: inline-block; margin-bottom: 20px; }
        .back-link:hover { text-decoration: underline; }
    """

    def create_sidebar(current_page: str) -> str:
        """Generate sidebar HTML."""
        index_active = 'class="active"' if current_page == 'index' else ''
        root_active = 'class="active"' if current_page == model.__name__ else ''

        sidebar_html = [
            "    <div class='sidebar'>",
            f"        <h2>{title}</h2>",
            f"        <a href='index.html' {index_active}>Index</a>",
            f"        <a href='{model.__name__}.html' {root_active}>{model.__name__}</a>",
        ]

        if '$defs' in schema:
            sidebar_html.append("        <h3 style='color: #3498db; font-size: 1em; margin-top: 20px;'>Types</h3>")
            for def_name in schema['$defs'].keys():
                active = 'class="active"' if current_page == def_name else ''
                sidebar_html.append(f"        <a href='{def_name}.html' {active}>{def_name}</a>")

        sidebar_html.append("    </div>")
        return '\n'.join(sidebar_html)

    # Create index page
    index_html = [
        "<!DOCTYPE html>",
        "<html lang='en'>",
        "<head>",
        "    <meta charset='UTF-8'>",
        "    <meta name='viewport' content='width=device-width, initial-scale=1.0'>",
        f"    <title>{title}</title>",
        f"    <style>{css}</style>",
        "</head>",
        "<body>",
        create_sidebar('index'),
        "    <div class='content'>",
        "        <div class='container'>",
        f"            <h1>{title}</h1>",
        f"            <p>{schema.get('description', '')}</p>",
        "            <h2>Documentation Structure</h2>",
        f"            <p><a href='{model.__name__}.html'>View Root Model: {model.__name__}</a></p>",
    ]

    if '$defs' in schema:
        index_html.append("            <h3>Type Definitions</h3>")
        index_html.append("            <ul>")
        for def_name, def_schema in schema['$defs'].items():
            desc = def_schema.get('description', '')[:100]
            index_html.append(f"                <li><a href='{def_name}.html'>{def_name}</a> - {desc}</li>")
        index_html.append("            </ul>")

    index_html.extend([
        "        </div>",
        "    </div>",
        "</body>",
        "</html>"
    ])

    with open(output_dir / "index.html", 'w', encoding='utf-8') as f:
        f.write('\n'.join(index_html))

    # Create root model page
    root_html = [
        "<!DOCTYPE html>",
        "<html lang='en'>",
        "<head>",
        "    <meta charset='UTF-8'>",
        "    <meta name='viewport' content='width=device-width, initial-scale=1.0'>",
        f"    <title>{model.__name__} - {title}</title>",
        f"    <style>{css}</style>",
        "</head>",
        "<body>",
        create_sidebar(model.__name__),
        "    <div class='content'>",
        "        <div class='container'>",
        f"            <h1>{model.__name__}</h1>",
        f"            <p>{schema.get('description', '')}</p>",
        "            <h2>Fields</h2>",
    ]

    if 'properties' in schema:
        for field_name, field_info in schema['properties'].items():
            required = field_name in schema.get('required', [])
            req_badge = "<span class='required'>[Required]</span>" if required else "<span class='optional'>[Optional]</span>"

            root_html.extend([
                "            <div class='field'>",
                f"                <div class='field-name'>{field_name} {req_badge}</div>",
                f"                <div><strong>Type:</strong> <span class='type'>{_format_field_type(field_info)}</span></div>",
            ])

            if 'description' in field_info:
                root_html.append(f"                <div class='description'>{field_info['description']}</div>")

            if 'default' in field_info:
                root_html.append(f"                <div><strong>Default:</strong> <span class='default'>{field_info['default']}</span></div>")

            # Add link to type definition if it's a reference
            if '$ref' in field_info:
                ref_name = field_info['$ref'].split('/')[-1]
                root_html.append(f"                <div><a href='{ref_name}.html'>View {ref_name} definition →</a></div>")

            root_html.append("            </div>")

    root_html.extend([
        "        </div>",
        "    </div>",
        "</body>",
        "</html>"
    ])

    with open(output_dir / f"{model.__name__}.html", 'w', encoding='utf-8') as f:
        f.write('\n'.join(root_html))

    # Create page for each definition
    if '$defs' in schema:
        for def_name, def_schema in schema['$defs'].items():
            def_html = [
                "<!DOCTYPE html>",
                "<html lang='en'>",
                "<head>",
                "    <meta charset='UTF-8'>",
                "    <meta name='viewport' content='width=device-width, initial-scale=1.0'>",
                f"    <title>{def_name} - {title}</title>",
                f"    <style>{css}</style>",
                "</head>",
                "<body>",
                create_sidebar(def_name),
                "    <div class='content'>",
                "        <div class='container'>",
                f"            <h1>{def_name}</h1>",
                f"            <p>{def_schema.get('description', '')}</p>",
            ]

            if def_schema.get('type') == 'object' and 'properties' in def_schema:
                def_html.append("            <h2>Fields</h2>")

                for field_name, field_info in def_schema['properties'].items():
                    required = field_name in def_schema.get('required', [])
                    req_badge = "<span class='required'>[Required]</span>" if required else "<span class='optional'>[Optional]</span>"

                    def_html.extend([
                        "            <div class='field'>",
                        f"                <div class='field-name'>{field_name} {req_badge}</div>",
                        f"                <div><strong>Type:</strong> <span class='type'>{_format_field_type(field_info)}</span></div>",
                    ])

                    if 'description' in field_info:
                        def_html.append(f"                <div class='description'>{field_info['description']}</div>")

                    if 'default' in field_info:
                        def_html.append(f"                <div><strong>Default:</strong> <span class='default'>{field_info['default']}</span></div>")

                    # Add link to type definition if it's a reference
                    if '$ref' in field_info:
                        ref_name = field_info['$ref'].split('/')[-1]
                        def_html.append(f"                <div><a href='{ref_name}.html'>View {ref_name} definition →</a></div>")

                    def_html.append("            </div>")

            elif def_schema.get('type') == 'string' and 'enum' in def_schema:
                def_html.append("            <div class='enum-values'>")
                def_html.append("                <strong>Possible Values:</strong>")
                def_html.append("                <ul>")
                for enum_value in def_schema['enum']:
                    def_html.append(f"                    <li><span class='enum-value'>{enum_value}</span></li>")
                def_html.append("                </ul>")
                def_html.append("            </div>")

            def_html.extend([
                "        </div>",
                "    </div>",
                "</body>",
                "</html>"
            ])

            with open(output_dir / f"{def_name}.html", 'w', encoding='utf-8') as f:
                f.write('\n'.join(def_html))

    print(f"[OK] Multi-file HTML documentation exported to: {output_dir}")


def export_all(
    model: Type[BaseModel],
    output_dir: Path = Path("output"),
    base_name: str = "dyom_specification",
    multi_file: bool = False
) -> None:
    """
    Export the model to all available formats.

    Args:
        model: The Pydantic model class to export
        output_dir: Directory where all outputs will be saved
        base_name: Base name for output files (without extension)
        multi_file: If True, export Markdown and HTML as multiple files
    """
    output_dir.mkdir(exist_ok=True)

    print(f"\nExporting {model.__name__} specification...")
    print("=" * 60)

    # Export JSON Schema (always single file)
    export_json_schema(model, output_dir / f"{base_name}.json")

    if multi_file:
        # Export to multi-file formats
        md_dir = output_dir / "markdown"
        html_dir = output_dir / "html"
        export_markdown_multifile(model, md_dir)
        export_html_multifile(model, html_dir)
    else:
        # Export to single file formats
        export_markdown(model, output_dir / f"{base_name}.md")
        export_html(model, output_dir / f"{base_name}.html")

    print("=" * 60)
    print(f"[OK] All exports completed successfully!")
    print(f"  Output directory: {output_dir.absolute()}")
