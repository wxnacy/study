package main

import (
    "github.com/nsf/termbox-go"
    "os"
)

func main() {
    err := termbox.Init()
    if err != nil {
        os.Exit(0)
    }

    defer termbox.Close()

    for {

        termbox.Clear(termbox.ColorWhite, termbox.ColorDefault)

        contents := []rune("Hello World")

        for i, d := range contents {
            termbox.SetCell(i, 0, d, termbox.ColorWhite, termbox.ColorDefault)
        }

        termbox.SetCursor(0, 0)
        termbox.Flush()

        e := termbox.PollEvent()
        switch e.Key {
            case termbox.KeyEsc: {
                os.Exit(0)
            }
        }
    }

}
