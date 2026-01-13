# 表单模式

基于 React Hook Form + Zod 构建。

## 基本设置

```tsx
import { z } from 'zod'
import { useForm } from 'react-hook-form'
import { zodResolver } from '@hookform/resolvers/zod'
import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from '@/components/ui/form'

const formSchema = z.object({
  name: z.string().min(2, '至少2个字符'),
  email: z.string().email('无效邮箱'),
})

type FormValues = z.infer<typeof formSchema>

const form = useForm<FormValues>({
  resolver: zodResolver(formSchema),
  defaultValues: { name: '', email: '' },
})
```

## 表单组件结构

```tsx
<Form {...form}>
  <form onSubmit={form.handleSubmit(onSubmit)} className='space-y-6'>
    <FormField
      control={form.control}
      name='fieldName'
      render={({ field }) => (
        <FormItem>
          <FormLabel>标签</FormLabel>
          <FormControl>
            <Input {...field} />
          </FormControl>
          <FormMessage />
        </FormItem>
      )}
    />
    <Button type='submit'>提交</Button>
  </form>
</Form>
```

## 常见字段类型

- 文本输入: `<Input {...field} />`
- 密码输入: `<PasswordInput {...field} />`
- 下拉选择: `<Select onValueChange={field.onChange} />`
- 复选框: `<Checkbox checked={field.value} onCheckedChange={field.onChange} />`
- 开关: `<Switch checked={field.value} onCheckedChange={field.onChange} />`
