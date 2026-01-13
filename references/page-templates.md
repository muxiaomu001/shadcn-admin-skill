# 页面模板

## 列表页面 (CRUD)

```tsx
import { Header } from '@/components/layout/header'
import { Main } from '@/components/layout/main'
import { EntityDialogs } from './components/entity-dialogs'
import { EntityPrimaryButtons } from './components/entity-primary-buttons'
import { EntityProvider } from './components/entity-provider'
import { EntityTable } from './components/entity-table'

export function EntityList() {
  return (
    <EntityProvider>
      <Header fixed>
        <Search />
        <div className='ms-auto flex items-center space-x-4'>
          <ThemeSwitch />
          <ProfileDropdown />
        </div>
      </Header>

      <Main className='flex flex-1 flex-col gap-4 sm:gap-6'>
        <div className='flex flex-wrap items-end justify-between gap-2'>
          <div>
            <h2 className='text-2xl font-bold tracking-tight'>Entity List</h2>
            <p className='text-muted-foreground'>Manage entities here.</p>
          </div>
          <EntityPrimaryButtons />
        </div>
        <EntityTable data={data} />
      </Main>

      <EntityDialogs />
    </EntityProvider>
  )
}
```

## Provider 组件

```tsx
import { createContext, useContext, useState, type ReactNode } from 'react'
import { type Entity } from '../data/schema'

type DialogType = 'add' | 'edit' | 'delete' | 'multi-delete' | null

type EntityContextType = {
  open: DialogType
  setOpen: (type: DialogType) => void
  currentRow: Entity | null
  setCurrentRow: (row: Entity | null) => void
}

const EntityContext = createContext<EntityContextType | null>(null)

export function EntityProvider({ children }: { children: ReactNode }) {
  const [open, setOpen] = useState<DialogType>(null)
  const [currentRow, setCurrentRow] = useState<Entity | null>(null)

  return (
    <EntityContext.Provider value={{ open, setOpen, currentRow, setCurrentRow }}>
      {children}
    </EntityContext.Provider>
  )
}

export function useEntityContext() {
  const context = useContext(EntityContext)
  if (!context) {
    throw new Error('useEntityContext must be used within EntityProvider')
  }
  return context
}
```
