package main

import (
    "fmt"
    "strings"
)

type User struct {
    id int
}


func main() {

    dir := "/Users/wxnacy/Documents/001.jpg"
    dirs := strings.Split(dir, "/")
    fmt.Println(dirs[0:len(dirs)-1])


}

