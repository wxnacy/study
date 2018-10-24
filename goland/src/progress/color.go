package main
// 带颜色的进度条

import (
    "fmt"
    "strings"
    "time"
)

const TOTAL = 20

func SetColor(msg string, conf, bg, text int) string {
    return fmt.Sprintf("%c[%d;%d;%dm%s%c[0m", 0x1B, conf, bg, text, msg, 0x1B)
}

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
            SetColor(strings.Repeat("=", progress), 0, 0, 36),
            SetColor(strings.Repeat("-", TOTAL - progress), 0, 0, 33),
        )

        fmt.Printf("%s \033[K\n", output)

        if progress >= 20 {
            break Loop
        }
        progress++
        time.Sleep(time.Duration(200) * time.Millisecond)
    }
}
