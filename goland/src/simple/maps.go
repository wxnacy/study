package main

import (
	"fmt"
)

func main() {

	var m1 = make(map[string]string)
	fmt.Println(m1)     // map[]

	m1["name"] = "wxnacy"
    fmt.Println(m1)     // map[name:wxnacy]

	m2 := map[string]string{"name": "wxnacy"}
    fmt.Println(m2)     // map[name:wxnacy]

    delete(m2, "name")
    fmt.Println(m2)     // map[]

    var m3 map[string]string
    fmt.Println(m3)

}
