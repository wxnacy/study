package main

import (
    "fmt"
)

type IUser interface {
    Print()
    GetName() string
    SetName(string)
}

type User struct {
    name string
}

type Man struct {
    User
    age int
}

func (this *User) SetName(name string) {
    this.name = name
}

func (this *Man) SetName(name string) {
    this.name = name
}

func (this *User) Print() {
    fmt.Println(this.name)
}

func (this *User) GetName() string {
    return this.name
}

func main() {
     var i IUser

     u := &User{}
     i = u
     i.SetName("wxnacy")
     i.Print()
     fmt.Println(i.GetName())

     m := &Man{}
     i = m
     i.SetName("man")
     i.Print()
}
