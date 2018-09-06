package main

import (
    "fmt"
    "encoding/hex"
)

func main() {
    s := "wxnacy"
    b := []byte(s)
    // 字符串和字节的相互转换
    fmt.Println(b)      // [119 120 110 97 99 121]
    fmt.Println(string(b))  // wxnacy

    hexStr := "78e731027d8fd50ed642340b7c9a63b3"
    data, err := hex.DecodeString(hexStr)   // [120 231 49 2 125 143 213 14 214 66 52 11 124 154 99 179] <nil>
    fmt.Println(data, err)
    fmt.Println(hex.EncodeToString(data))   // 78e731027d8fd50ed642340b7c9a63b3
}
