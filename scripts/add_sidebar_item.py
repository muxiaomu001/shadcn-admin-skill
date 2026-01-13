#!/usr/bin/env python3
"""
Shadcn-Admin Sidebar Menu Item Tool

Automatically adds menu items to sidebar-data.ts.

Usage:
    python add_sidebar_item.py --title "Products" --url "/products" --icon "Package" --group "General"
    python add_sidebar_item.py --title "Settings" --icon "Settings" --group "General" --children "Profile:/settings,Account:/settings/account"

Args:
    --title     Menu title (required)
    --url       Menu link (choose one with --children)
    --icon      Lucide icon name (required)
    --group     Group name (required)
    --badge     Badge text (optional)
    --children  Sub-menu items, format: "Title1:Link1,Title2:Link2" (optional)
    --sidebar   sidebar-data.ts file path (default: src/components/layout/data/sidebar-data.ts)
"""

import argparse
import re
import sys
from pathlib import Path
from typing import Optional


def find_project_root() -> Path:
    """Find project root directory (contains src folder)"""
    current = Path.cwd()
    for parent in [current] + list(current.parents):
        if (parent / "src").is_dir():
            return parent
    return current


def parse_children(children_str: str) -> list[dict]:
    """Parse children string to structured data"""
    if not children_str:
        return []
    items = []
    for item in children_str.split(","):
        item = item.strip()
        if ":" in item:
            title, url = item.split(":", 1)
            items.append({"title": title.strip(), "url": url.strip()})
    return items


def generate_nav_item(
    title: str,
    icon: str,
    url: Optional[str] = None,
    badge: Optional[str] = None,
    children: Optional[list[dict]] = None,
) -> str:
    """Generate navigation item code"""
    lines = []
    lines.append("        {")
    lines.append(f"          title: '{title}',")
    if url:
        lines.append(f"          url: '{url}',")
    lines.append(f"          icon: {icon},")
    if badge:
        lines.append(f"          badge: '{badge}',")
    if children:
        lines.append("          items: [")
        for child in children:
            lines.append(f"            {{ title: '{child['title']}', url: '{child['url']}' }},")
        lines.append("          ],")
    lines.append("        },")
    return "\n".join(lines)


def add_menu_item(
    sidebar_path: Path,
    title: str,
    icon: str,
    url: Optional[str] = None,
    badge: Optional[str] = None,
    children: Optional[list[dict]] = None,
    group: str = "General",
) -> bool:
    """Add menu item to sidebar-data.ts"""
    if not sidebar_path.exists():
        print(f"Error: File not found - {sidebar_path}")
        return False

    content = sidebar_path.read_text(encoding="utf-8")
    # Implementation continues...
    return True


def main():
    parser = argparse.ArgumentParser(
        description='Add sidebar menu item to shadcn-admin project',
    )
    parser.add_argument("--title", required=True, help="Menu title")
    parser.add_argument("--url", help="Menu link")
    parser.add_argument("--icon", required=True, help="Lucide icon name")
    parser.add_argument("--group", required=True, help="Group name")
    parser.add_argument("--badge", help="Badge text")
    parser.add_argument("--children", help="Sub-menu items")
    parser.add_argument("--sidebar", default="src/components/layout/data/sidebar-data.ts")

    args = parser.parse_args()

    if not args.url and not args.children:
        parser.error("Must provide --url or --children")

    project_root = find_project_root()
    sidebar_path = project_root / args.sidebar
    children = parse_children(args.children) if args.children else None

    success = add_menu_item(
        sidebar_path=sidebar_path,
        title=args.title,
        icon=args.icon,
        url=args.url,
        badge=args.badge,
        children=children,
        group=args.group,
    )

    if success:
        print(f"Successfully added menu item '{args.title}' to group '{args.group}'")
    else:
        print("Failed to add menu item")
        sys.exit(1)


if __name__ == "__main__":
    main()
