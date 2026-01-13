# 布局模式

## 布局组件概览

```
┌─────────────────────────────────────────────────────┐
│                    Header                           │
├──────────┬──────────────────────────────────────────┤
│          │                                          │
│ Sidebar  │              Main                        │
│          │                                          │
└──────────┴──────────────────────────────────────────┘
```

## AppSidebar 侧边栏

```tsx
import {
  Sidebar,
  SidebarContent,
  SidebarFooter,
  SidebarHeader,
} from '@/components/ui/sidebar'

export function AppSidebar() {
  return (
    <Sidebar>
      <SidebarHeader>
        <TeamSwitcher />
      </SidebarHeader>
      <SidebarContent>
        {navGroups.map((props) => (
          <NavGroup key={props.title} {...props} />
        ))}
      </SidebarContent>
      <SidebarFooter>
        <NavUser />
      </SidebarFooter>
    </Sidebar>
  )
}
```

## Header 头部

```tsx
<Header fixed>
  <Search />
  <div className='ms-auto flex items-center space-x-4'>
    <ThemeSwitch />
    <ProfileDropdown />
  </div>
</Header>
```

## Main 主内容区

```tsx
<Main className='flex flex-1 flex-col gap-4 sm:gap-6'>
  <div className='flex flex-wrap items-end justify-between gap-2'>
    <div>
      <h2 className='text-2xl font-bold tracking-tight'>页面标题</h2>
      <p className='text-muted-foreground'>页面描述</p>
    </div>
    <PrimaryButtons />
  </div>
  <DataTable />
</Main>
```
