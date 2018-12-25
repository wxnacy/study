package main

import (
    "fmt"
    "net/http"
    "io/ioutil"
    "strconv"
)

type User struct {
    id int
}


func main() {

    // client := http.DefaultClient()

    client := http.Client{}

    req, _ := http.NewRequest("GET", "http://mewevideo.oss-cn-beijing.aliyuncs.com/backup/1533869500000tyKnra.mp4", nil)
    req.Header.Set("Range", "bytes=0-512")

    res, _ := client.Do(req)
    body, _ := ioutil.ReadAll(res.Body)
    fmt.Println(body)
    for _, d := range body {
        fmt.Println(strconv.QuoteRune(d))
    }
    // fmt.Println(string(body))

}

