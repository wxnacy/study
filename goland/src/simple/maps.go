package main

import (
    "fmt"
)

func main(){
    var m1 = make(map[string]string)
    m1["name"] = "wxnacy"
    fmt.Println(m1)
    m2 := map[string]string{"name": "wxnacy"}
    fmt.Println(m2)
}
