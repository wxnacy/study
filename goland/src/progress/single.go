package main

import (
    "fmt"
    "strings"
    "time"
)

const TOTAL = 20

func main() {

    var progress = 0
    var position = 1
    Loop:
    for {
        if progress > 0 {
            fmt.Printf("\033[%dA\033[K", position)
        }

        output := fmt.Sprintf(
            "%s%s%s",
            "progress: ",
            strings.Repeat("=", progress),
            strings.Repeat("-", TOTAL - progress),
        )

        fmt.Printf("%s \033[K\n", output)

        if progress >= 20 {
            break Loop
        }
        progress++
        time.Sleep(time.Duration(200) * time.Millisecond)
    }
}
