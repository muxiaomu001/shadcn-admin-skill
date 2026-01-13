# 数据表格模式

基于 TanStack Table v8 构建。

## 列定义

```tsx
import { type ColumnDef } from '@tanstack/react-table'
import { Checkbox } from '@/components/ui/checkbox'
import { DataTableColumnHeader } from '@/components/data-table'

export const columns: ColumnDef<Entity>[] = [
  // 选择列
  {
    id: 'select',
    header: ({ table }) => (
      <Checkbox
        checked={table.getIsAllPageRowsSelected()}
        onCheckedChange={(value) => table.toggleAllPageRowsSelected(!!value)}
      />
    ),
    cell: ({ row }) => (
      <Checkbox
        checked={row.getIsSelected()}
        onCheckedChange={(value) => row.toggleSelected(!!value)}
      />
    ),
  },
  // 数据列
  {
    accessorKey: 'name',
    header: ({ column }) => (
      <DataTableColumnHeader column={column} title='Name' />
    ),
  },
  // 操作列
  {
    id: 'actions',
    cell: DataTableRowActions,
  },
]
```

## 工具栏

```tsx
<DataTableToolbar
  table={table}
  searchPlaceholder='Filter...'
  filters={[
    {
      columnId: 'status',
      title: 'Status',
      options: [
        { label: 'Active', value: 'active' },
        { label: 'Inactive', value: 'inactive' },
      ],
    },
  ]}
/>
```
