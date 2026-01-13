# 组件示例

## Button 按钮

```tsx
import { Button } from '@/components/ui/button'

<Button variant='default'>Default</Button>
<Button variant='destructive'>Destructive</Button>
<Button variant='outline'>Outline</Button>
<Button variant='ghost'>Ghost</Button>

<Button size='sm'>Small</Button>
<Button size='lg'>Large</Button>
<Button size='icon'><Icon /></Button>
```

## Card 卡片

```tsx
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from '@/components/ui/card'

<Card>
  <CardHeader>
    <CardTitle>Card Title</CardTitle>
    <CardDescription>Description</CardDescription>
  </CardHeader>
  <CardContent>
    <p>Content</p>
  </CardContent>
</Card>
```

## Toast 通知 (Sonner)

```tsx
import { toast } from 'sonner'

toast.success('Successfully saved!')
toast.error('Something went wrong')
toast.promise(saveData(), {
  loading: 'Saving...',
  success: 'Data saved!',
  error: 'Could not save.',
})
```
