package main

import (
    "bufio"
    "fmt"
    "log"
    "os"
    "strings"
)

func HasStdin() (string, bool) {
    fileInfo, _ := os.Stdin.Stat()
    if (fileInfo.Mode() & os.ModeNamedPipe) != os.ModeNamedPipe {
        return "", false
    }
    s := bufio.NewScanner(os.Stdin)
    resList := make([]string, 0, 0)
    for s.Scan() {
        resList = append(resList, s.Text())
    }
    result := strings.Join(resList, "\n")
    return result, true
}

func main() {
    stdin, flag := HasStdin()
    if flag {
        fmt.Println(stdin)
    } else {
        log.Fatal("The command is intended to work with pipes.")
    }
}
