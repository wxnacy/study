package main

import (
    "fmt"
)

func main() {
    Try(
        func() {
            panic(11)
        }, func(e interface{}) {
            fmt.Println(e)
        }
    )
}

func Try(main func(), recovers func(interface{})) {
    defer call func () {
        if err := recover(); err != nil {
            recovers(err)
        }
    }
    main()
}
