package main

import (
	"crypto/md5"
	"crypto/hmac"
	"fmt"
    "io"
    "os"
    "log"
)

func main() {

    fmt.Println("md5\t", MD51("message"))
    fmt.Println("md5\t", MD52("message"))
    fmt.Println("HmacMD5\t", HmacMD5("message", "message_key"))
    fmt.Println("md5file\t", MD5File("main.go"))

}

func MD51(message string) string {
    res := md5.Sum([]byte(message))
    return fmt.Sprintf("%x", res)
}

func MD52(message string) string {
    h := md5.New()
    io.WriteString(h, message)
    return fmt.Sprintf("%x", h.Sum(nil))
}

func MD5File(filePath string) string {
    f, err := os.Open(filePath)
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()

	h := md5.New()
	if _, err := io.Copy(h, f); err != nil {
		log.Fatal(err)
	}

    return fmt.Sprintf("%x", h.Sum(nil))
}

func HmacMD5(message string, key string) string {
    h := hmac.New(md5.New, []byte(key))
    h.Write([]byte(message))
    return fmt.Sprintf("%x", h.Sum(nil))
}
