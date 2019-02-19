package main
// 判断 interface 储存的值

import (
     "fmt"
)

type IUser interface {

}

type User struct {
    name string
}

type Man struct {
    name string

}

func main() {

    var i IUser
    i = &User{name: "User"}
    var m IUser
    m = Man{name: "Man"}

    if t, ok := i.(*User); ok {
        fmt.Println(t)
    }

    switch t := m.(type) {
        case Man: {
            fmt.Println("m is ", t)
        }
        default: {
            fmt.Println("m is default")
        }
    }

// &{User}
// m is  {Man}

}
