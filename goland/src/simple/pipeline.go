package main

import (
    "bufio"
    "fmt"
    "log"
    "os"
)

func main() {
    fileInfo, _ := os.Stdin.Stat()
    fmt.Println(fileInfo.Mode(), os.ModeNamedPipe, os.ModeNamedPipe)
    if (fileInfo.Mode() & os.ModeNamedPipe) != os.ModeNamedPipe {
        log.Fatal("The command is intended to work with pipes.")
    }
    s := bufio.NewScanner(os.Stdin)
    for s.Scan() {
        fmt.Println(s.Text())
    }
}
