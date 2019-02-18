package main

import (
     "image"
     "fmt"
     "os"
)

func main() {
    path := "/Users/wxnacy/Downloads/react-app1.png"
    file, err := os.Open(path)
    if err != nil {
        fmt.Println(err)
    }

    img, _, err := image.Decode(file)
    if err != nil {
        fmt.Println(err)
    }
    file.Close()
    fmt.Println(img.Bounds().Size())
}
