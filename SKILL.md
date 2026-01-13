---
name: shadcn-admin
description: 基于 shadcn-admin 项目开发管理后台的专业助手。支持页面生成、组件开发、数据表格 CRUD、表单处理、布局配置等功能。当用户需要开发 admin dashboard、管理后台、后台管理系统、仪表盘页面，或提到 shadcn-admin、TanStack Table、数据表格、用户管理、任务管理等关键词时触发此 skill。
license: MIT
version: 1.0.0
---

# Shadcn-Admin 开发助手

基于 [shadcn-admin](https://github.com/satnaing/shadcn-admin) 项目的管理后台开发助手，提供页面生成、组件开发、数据表格 CRUD 等功能。

## 技术栈

> **注意**：以下为 shadcn-admin 项目的最新/目标版本，实际版本请以项目 `package.json` 为准。

- React 19 + TypeScript + Vite 7
- TanStack Router (路由) + TanStack Table (数据表格) + TanStack Query (数据请求)
- Tailwind CSS 4 + shadcn/ui (Radix UI)
- React Hook Form + Zod (表单验证)
- Zustand (状态管理) + Recharts (图表)
- Lucide Icons (图标)

## 参考文档导航

根据任务类型选择对应文档：

| 任务类型 | 参考文档 |
|---------|----------|
| 了解项目结构和技术栈 | [project-structure.md](references/project-structure.md) |
| 创建页面布局、侧边栏、导航 | [layout-patterns.md](references/layout-patterns.md) |
| 创建数据表格、CRUD 功能 | [data-table-patterns.md](references/data-table-patterns.md) |
| 创建表单、验证逻辑 | [form-patterns.md](references/form-patterns.md) |
| 创建完整页面 (Dashboard/List/Settings) | [page-templates.md](references/page-templates.md) |
| 使用 UI 组件 | [component-examples.md](references/component-examples.md) |

## 快速开始

### 1. 创建新的功能模块

```
src/features/[module-name]/
├── index.tsx              # 主页面组件
├── components/            # 模块专用组件
│   ├── [name]-table.tsx   # 数据表格
│   ├── [name]-columns.tsx # 列定义
│   ├── [name]-dialogs.tsx # 对话框
│   └── [name]-provider.tsx # Context Provider
└── data/
    ├── schema.ts          # Zod Schema
    └── data.ts            # 静态数据/枚举
```

### 2. 添加路由

在 `src/routes/_authenticated/` 下创建路由文件，TanStack Router 会自动生成路由。

### 3. 添加侧边栏导航

编辑 `src/components/layout/data/sidebar-data.ts`，在 `navGroups` 中添加菜单项。

## 核心模式速查

### 页面结构

```tsx
export function PageName() {
  return (
    <Provider>
      <Header fixed>
        <Search />
        <div className='ms-auto flex items-center space-x-4'>
          <ThemeSwitch />
          <ProfileDropdown />
        </div>
      </Header>
      <Main className='flex flex-1 flex-col gap-4'>
        {/* 页面标题 */}
        <div className='flex items-end justify-between gap-2'>
          <div>
            <h2 className='text-2xl font-bold'>标题</h2>
            <p className='text-muted-foreground'>描述</p>
          </div>
          <PrimaryButtons />
        </div>
        {/* 主要内容 */}
        <DataTable />
      </Main>
      <Dialogs />
    </Provider>
  )
}
```

### 数据表格列定义

```tsx
export const columns: ColumnDef<T>[] = [
  {
    id: 'select',
    header: ({ table }) => <Checkbox ... />,
    cell: ({ row }) => <Checkbox ... />,
  },
  {
    accessorKey: 'name',
    header: ({ column }) => <DataTableColumnHeader column={column} title='Name' />,
    cell: ({ row }) => <div>{row.getValue('name')}</div>,
  },
  { id: 'actions', cell: DataTableRowActions },
]
```

### 表单验证

```tsx
const schema = z.object({
  name: z.string().min(2, '至少2个字符'),
  email: z.string().email('无效邮箱'),
})

const form = useForm({
  resolver: zodResolver(schema),
  defaultValues: { name: '', email: '' },
})
```

## 最佳实践

1. **组件组织**: 功能相关组件放在 `features/[module]/components/`
2. **类型安全**: 使用 Zod schema 定义数据类型并导出 TypeScript 类型
3. **状态管理**: 简单状态用 React Context，复杂状态用 Zustand
4. **样式**: 使用 Tailwind 工具类，复杂样式用 `cn()` 合并
5. **响应式**: 移动优先，使用 `sm:` `md:` `lg:` 断点
6. **RTL 支持**: 使用 `ms-` `me-` `ps-` `pe-` 替代 `ml-` `mr-` `pl-` `pr-`

## 自动化脚本

### create_feature.py - 功能模块脚手架

快速创建完整的功能模块结构：

```bash
# 在项目根目录下运行（包含 src/ 目录的位置）
python scripts/create_feature.py <module-name> [--fields "field1,field2,..."]

# 或指定项目根目录
python scripts/create_feature.py <module-name> --project-root /path/to/project
```

示例：
```bash
python scripts/create_feature.py products --fields "id,name,price,status,category"
```

> **注意**：
> - 脚本默认使用当前工作目录作为项目根目录，请确保在正确的目录下运行
> - 生成的 `[name]-dialogs.tsx` 仅包含占位符，需要根据业务需求自行实现增删改对话框

### add_sidebar_item.py - 添加侧边栏菜单

向 sidebar-data.ts 添加菜单项：

```bash
python scripts/add_sidebar_item.py --title "Products" --url "/products" --icon "Package" --group "General"
```

> **注意**：
> - 脚本使用文本插入方式修改 `sidebar-data.ts`，建议运行后检查文件语法
> - 确保指定的 `--icon` 是有效的 Lucide 图标名称
> - 如果插入失败，可手动编辑 `src/components/layout/data/sidebar-data.ts`
