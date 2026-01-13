# 项目结构和技术栈

## 技术栈

| 类别 | 技术 | 版本 |
|-----|------|-----|
| 框架 | React | 19.x |
| 语言 | TypeScript | 5.9.x |
| 构建 | Vite | 7.x |
| 路由 | TanStack Router | 1.x |
| 数据表格 | TanStack Table | 8.x |
| 数据请求 | TanStack Query | 5.x |
| 样式 | Tailwind CSS | 4.x |
| UI 组件 | shadcn/ui (Radix UI) | - |
| 表单 | React Hook Form | 7.x |
| 验证 | Zod | 4.x |

## 目录结构

```
src/
├── components/             # 共享组件
│   ├── ui/                 # shadcn/ui 基础组件
│   ├── layout/             # 布局组件
│   └── data-table/         # 数据表格组件
├── features/               # 功能模块 (按业务划分)
├── hooks/                  # 自定义 Hooks
├── lib/                    # 工具函数
└── routes/                 # TanStack Router 路由
```

## 功能模块结构

```
features/[module]/
├── index.tsx              # 主页面导出
├── components/            # 模块专用组件
└── data/
    ├── schema.ts          # Zod Schema + 类型
    └── data.ts            # 枚举/静态数据
```
