package main

import (
    "fmt"
    "reflect"
)

func Type(i interface{}) {

    switch i.(type) {
    case string:
        fmt.Println("string")
    case int:
        fmt.Println("int")
    case bool:
        fmt.Println("bool")
    default:
        fmt.Println("default")
    }

}

func main() {

    t := reflect.TypeOf("Hello World")
    fmt.Println(t)
    Type("")
}
