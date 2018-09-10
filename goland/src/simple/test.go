package main

import (
    "fmt"
    "bufio"
    "crypto/md5"
    "os"
    "io"
)

func main() {

    // fileInfo, _ := os.Stdin.Stat()
    // if (fileInfo.Mode() & os.ModeNamedPipe) != os.ModeNamedPipe {
        // fmt.Println("no")
    // }
    s := bufio.NewScanner(os.Stdin)
    _ = s


	h := md5.New()
	if _, err := io.Copy(h, os.Stdin); err != nil {
        fmt.Println(err)
	}

    fmt.Printf("%x", h.Sum(nil))
}
