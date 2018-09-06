package main

import (
    "fmt"
    "net/http"
    "os"
    "io/ioutil"
    "time"
    "flag"
)

var url string

func InitArgs() {
    url = flag.Args()[0]
    // flag.StringVar(&url, "u")
    flag.Parse()
}

func GetUrlBody() []byte {
    client := http.Client{}
    req, err := http.NewRequest("GET", "https://mewevideo.oss-cn-beijing.aliyuncs.com/mp4MultibitrateIn50/1535440227000pdwhAw.mp4", nil)
    // req, err := http.NewRequest("GET", "https://mewephoto.oss-cn-beijing.aliyuncs.com/mp4MultibitrateIn50/1535436469000Zew8Gs.png", nil)
    // req, err := http.NewRequest("GET", "https://mewephoto.oss-cn-beijing.aliyuncs.com/mp4MultibitrateIn50/1535436453000acr7E5.jpg", nil)
    req.Header.Set("Range", "bytes=0-2404746")
    resp, err := client.Do(req)
    fmt.Println(resp.Header)
    // fmt.Println(resp.Header.Get("Accept-Ranges"))
    // fmt.Println(resp.Header.Get("Content-Length"))
    defer resp.Body.Close()
    body, _ := ioutil.ReadAll(resp.Body)
    fmt.Println(err)
    return body

}

func Save(body []byte) {
    file, err := os.Create("/Users/wxnacy/.wdown/test")
    fmt.Println(*file, err)
    // byteSlice := []byte("Bytes!\n")
    bytesWritten, err := file.Write(body)
    fmt.Println(bytesWritten, err)
    defer file.Close()
}

func main() {
    begin := time.Now().Unix()
    // InitArgs()
    fmt.Println(url)

    body := GetUrlBody()
    // _ = body

    end := time.Now().Unix()
    fmt.Println(end - begin)

    begin = time.Now().Unix()
    Save(body)
    end = time.Now().Unix()
    fmt.Println(end - begin)
}
