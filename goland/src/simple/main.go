package main

import "fmt"

func main() {
    var a map[string]string = make(map[string]string)
    a["id"] = "1"
    fmt.Println(a)

    b := map[string]string{"name": "wxnacy", "id": "1"}
    fmt.Println(b)

    c, ok:= b["name"]
    fmt.Println(c)
    fmt.Println(ok)

    c = b["names"]
    fmt.Println(c)

    delete(b, "name")
    fmt.Println(b)

}
