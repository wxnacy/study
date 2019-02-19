# Go 简单了解 interface

在 Java 中 interface 是很常用的，因为父类单继承的特性，interface 可以让类的实现更加灵活。

而同样在强类型的 GO 中，interface 也是必不可少的。

## interface 的实现

```go
type I interface {

}
```

interface 是一种**类型**，可以包含 0 或更多的方法，如果一个类型实现了一个 interface 的所有方法，则它实现了该 interface，比如：

```go
package main
// interface 的实现

import (
     "fmt"
)

type IUser interface {
    SetName(string)
    GetName() string
}

type User struct {
    name string
}


func (self User) GetName() string {
    return self.name
}

func (self *User) SetName(name string) {
    self.name = name
}

func main() {

    var i IUser
    i = &User{}
    i.SetName("wxnacy")
    fmt.Println(i.GetName())
    // wxnacy

}
```

可以看到，因为 `SetName` 方法是在指针中实现的，所有 `i` 需要储存指针才可以实现 `struct` 中的所有方法

## 判断 interface 存储值的类型

使用 `i.(T)` 或 `i.(type)` 可以判断 interface 中储存的值，后者只能在 `switch` 中使用。

i 是 interface 类型的变量，T 代表要断言的类型，value 是 interface 变量存储的值，ok 是 bool 类型表示是否为该断言的类型 T

```go
if t, ok := i.(*User); ok {
    fmt.Println(t)
}
// &{User}
```

```go
switch t := m.(type) {
    case Man: {
        fmt.Println("m is ", t)
    }
    default: {
        fmt.Println("m is default")
    }
}

// m is  {Man}
```

## 使用 interface 实现泛型

强类型语言可以实现类似 Java 的泛型是必不可少的，在 Go 中可以使用 interface 来实现。

```go
func InArray(val interface{}, array interface{}) (index int){

}
```

避免通过编写重复代码实现方法的多态，我们可以使用 `interface{}` 来传入任意类型，
并使用 `reflect` 反射包来实现具体方法。

我们使用该特性，实现一个判断数组中是否包含某值的方法

```go
// 利用 reflect 反射方法判断 val 是否包含在 array 中，如果包含返回索引位置
func InArray(val interface{}, array interface{}) (index int) {
    index = -1
    switch reflect.TypeOf(array).Kind() {
        case reflect.Slice: {
            arr := reflect.ValueOf(array)
            for i := 0; i < arr.Len(); i++ {
                if reflect.DeepEqual(val, arr.Index(i).Interface()) {
                    index = i
                    return
                }
            }
        }
    }
    return
}
var arr = []int{1,2,3,4}
fmt.Println(InArray(3, arr))
// 2
```

- [reflact](https://golang.org/pkg/reflect)

本文代码在 Github 当前文件夹中
