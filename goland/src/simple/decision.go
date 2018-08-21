package main

import "fmt"

func main(){
    If()
    Switch()
}

func If(){
    a := 1
    if a > 0 {
        fmt.Println("> 0")
    } else {
        fmt.Println("< 0")
    }
}

func Switch(){
    a := 1
    var c string

    switch a {
        case 1: c = "1"
        case 2: c = "2"
        default: 
            c = "default"
    }

    fmt.Println(c)
}
