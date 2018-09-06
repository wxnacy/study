package main

import (
    "fmt"
    "golang.org/x/crypto/bcrypt"
)

func main() {
    fmt.Println("Hello World")
    hash, _ := bcrypt.GenerateFromPassword([]byte("message"), 10)
    fmt.Println(string(hash))
    fmt.Println(bcrypt.CompareHashAndPassword(hash, []byte("message")))
}
