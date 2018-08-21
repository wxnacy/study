package main

import (
    "fmt"
    "encoding/json"
    "io/ioutil"
    "net/http"
)

func main(){
    res, err := http.Get("http://ip-api.com/json")
    fmt.Println(err)

    defer res.Body.Close()
    body, _ := ioutil.ReadAll(res.Body)
    fmt.Println(string(body))

    var data map[string]interface{}
    err = json.Unmarshal([]byte(string(body)), &data)
    if err != nil {
        panic(err)
    }

    fmt.Println(data)

    fmt.Println(data["timezone"])

}
