package main

import (
    "bufio"
    "fmt"
    "io"
    "os"
    "strings"
)

func ReadLine(fileName string, handler func(string)) error {
    f, err := os.Open(fileName)
    if err != nil {
        return err
    }
    buf := bufio.NewReader(f)
    for {
        line, err := buf.ReadString('\n')
        line = strings.TrimSpace(line)
        fmt.Println(len(line))
        handler(line)
        if err != nil {
            if err == io.EOF {
                return nil
            }
            return err
        }
    }
    return nil
}

func Print(line string) {
    fmt.Println(line)
}

func main() {
    ReadLine("test", Print)
}
