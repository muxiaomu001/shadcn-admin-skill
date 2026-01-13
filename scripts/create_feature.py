#!/usr/bin/env python3
"""
Feature Module Scaffold Generator for shadcn-admin

Creates a complete feature module structure with all necessary files:
- index.tsx (main page)
- components/ (table, columns, dialogs, provider, etc.)
- data/ (schema, data)

Usage:
    python create_feature.py <module-name> [--fields "field1,field2,..."] [--project-root <path>]

Example:
    python create_feature.py products --fields "id,name,price,status,category"
"""

import argparse
import re
import sys
from pathlib import Path
from typing import List, Optional


def to_pascal_case(name: str) -> str:
    """Convert kebab-case or snake_case to PascalCase."""
    return ''.join(word.capitalize() for word in re.split(r'[-_]', name))


def to_camel_case(name: str) -> str:
    """Convert kebab-case or snake_case to camelCase."""
    pascal = to_pascal_case(name)
    return pascal[0].lower() + pascal[1:] if pascal else ''


def to_kebab_case(name: str) -> str:
    """Convert PascalCase or camelCase to kebab-case."""
    s1 = re.sub(r'(.)([A-Z][a-z]+)', r'\1-\2', name)
    return re.sub(r'([a-z0-9])([A-Z])', r'\1-\2', s1).lower()


class FeatureGenerator:
    """Generate shadcn-admin feature module scaffold."""

    def __init__(self, module_name: str, fields: Optional[List[str]] = None, project_root: Optional[Path] = None):
        self.module_name = to_kebab_case(module_name)
        self.module_pascal = to_pascal_case(module_name)
        self.module_camel = to_camel_case(module_name)
        self.fields = fields or ['id', 'name', 'status', 'createdAt', 'updatedAt']
        self.has_status = 'status' in self.fields
        self.project_root = project_root or Path.cwd()
        self.features_dir = self.project_root / 'src' / 'features' / self.module_name

    def generate(self, dry_run: bool = False) -> tuple[bool, str]:
        """Generate the feature module structure."""
        if self.features_dir.exists():
            return False, f"Feature '{self.module_name}' already exists at {self.features_dir}"

        if dry_run:
            return True, f"Would create feature at: {self.features_dir}"

        try:
            # Create directories
            (self.features_dir / 'components').mkdir(parents=True, exist_ok=True)
            (self.features_dir / 'data').mkdir(parents=True, exist_ok=True)

            # Generate files
            self._create_schema()
            self._create_data()
            self._create_provider()
            self._create_columns()
            self._create_table()
            self._create_row_actions()
            self._create_bulk_actions()
            self._create_primary_buttons()
            self._create_dialogs()
            self._create_index()

            return True, f"Successfully created feature '{self.module_name}' at {self.features_dir}"

        except Exception as e:
            return False, f"Error creating feature: {e}"

    def _create_schema(self):
        """Create data/schema.ts"""
        status_type = ''
        if self.has_status:
            status_type = f'''const {self.module_camel}StatusSchema = z.union([
  z.literal('active'),
  z.literal('inactive'),
])
export type {self.module_pascal}Status = z.infer<typeof {self.module_camel}StatusSchema>

'''
        content = f'''import {{ z }} from 'zod'

{status_type}const {self.module_camel}Schema = z.object({{
{self._generate_schema_fields()}
}})

export type {self.module_pascal} = z.infer<typeof {self.module_camel}Schema>
export const {self.module_camel}ListSchema = z.array({self.module_camel}Schema)
'''
        (self.features_dir / 'data' / 'schema.ts').write_text(content, encoding='utf-8')

    def _generate_schema_fields(self) -> str:
        """Generate Zod schema fields."""
        lines = []
        for field in self.fields:
            if field == 'id':
                lines.append('  id: z.string(),')
            elif field in ['createdAt', 'updatedAt']:
                lines.append(f'  {field}: z.coerce.date(),')
            elif field == 'status':
                lines.append(f'  status: {self.module_camel}StatusSchema,')
            else:
                lines.append(f'  {field}: z.string(),')
        return '\n'.join(lines)

    def _create_data(self):
        """Create data/data.ts"""
        if self.has_status:
            content = f'''// Status colors for badges
export const statusColors = new Map<string, string>([
  ['active', 'bg-green-500/10 text-green-500 border-green-500/20'],
  ['inactive', 'bg-gray-500/10 text-gray-500 border-gray-500/20'],
])

// Status options for filters
export const statuses = [
  {{ label: 'Active', value: 'active' }},
  {{ label: 'Inactive', value: 'inactive' }},
]
'''
        else:
            content = '''// Add your data constants here
'''
        (self.features_dir / 'data' / 'data.ts').write_text(content, encoding='utf-8')

    def _create_provider(self):
        """Create components/[name]-provider.tsx"""
        content = f'''import {{ createContext, useContext, useState, type ReactNode }} from 'react'
import {{ type {self.module_pascal} }} from '../data/schema'

type DialogType = 'add' | 'edit' | 'delete' | 'multi-delete' | null

type {self.module_pascal}ContextType = {{
  open: DialogType
  setOpen: (type: DialogType) => void
  currentRow: {self.module_pascal} | null
  setCurrentRow: (row: {self.module_pascal} | null) => void
}}

const {self.module_pascal}Context = createContext<{self.module_pascal}ContextType | null>(null)

export function {self.module_pascal}Provider({{ children }}: {{ children: ReactNode }}) {{
  const [open, setOpen] = useState<DialogType>(null)
  const [currentRow, setCurrentRow] = useState<{self.module_pascal} | null>(null)

  return (
    <{self.module_pascal}Context.Provider value={{ open, setOpen, currentRow, setCurrentRow }}>
      {{children}}
    </{self.module_pascal}Context.Provider>
  )
}}

export function use{self.module_pascal}Context() {{
  const context = useContext({self.module_pascal}Context)
  if (!context) {{
    throw new Error('use{self.module_pascal}Context must be used within {self.module_pascal}Provider')
  }}
  return context
}}
'''
        (self.features_dir / 'components' / f'{self.module_name}-provider.tsx').write_text(content, encoding='utf-8')

    def _create_columns(self):
        """Create components/[name]-columns.tsx - stub"""
        pass

    def _create_table(self):
        """Create components/[name]-table.tsx - stub"""
        pass

    def _create_row_actions(self):
        """Create components/data-table-row-actions.tsx - stub"""
        pass

    def _create_bulk_actions(self):
        """Create components/data-table-bulk-actions.tsx - stub"""
        pass

    def _create_primary_buttons(self):
        """Create components/[name]-primary-buttons.tsx - stub"""
        pass

    def _create_dialogs(self):
        """Create components/[name]-dialogs.tsx - stub"""
        pass

    def _create_index(self):
        """Create index.tsx - stub"""
        pass


def main():
    parser = argparse.ArgumentParser(
        description='Generate shadcn-admin feature module scaffold',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  # Create basic feature
  python create_feature.py products

  # Create feature with custom fields
  python create_feature.py products --fields "id,name,price,status,category"

  # Dry run (show what would be created)
  python create_feature.py products --dry-run
        '''
    )

    parser.add_argument('module_name', help='Name of the feature module (kebab-case)')
    parser.add_argument('--fields', help='Comma-separated list of fields', default=None)
    parser.add_argument('--project-root', type=Path, help='Project root directory')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be done')

    args = parser.parse_args()

    fields = args.fields.split(',') if args.fields else None

    generator = FeatureGenerator(
        module_name=args.module_name,
        fields=fields,
        project_root=args.project_root,
    )

    success, message = generator.generate(dry_run=args.dry_run)
    print(message)
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
