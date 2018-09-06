package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
)

func main() {
    url := "http://ip-api.com/json"
	// res, err := http.Get(url)
	// fmt.Println(err)

	// defer res.Body.Close()
	// body, _ := ioutil.ReadAll(res.Body)
	// fmt.Println(string(body))

	// var data map[string]interface{}
	// err = json.Unmarshal([]byte(string(body)), &data)
	// if err != nil {
		// panic(err)
	// }

	// fmt.Println(data)


    fmt.Println(HttpGet(url))

}

func HttpGet(url string) map[string]interface{} {
    res, err := http.Get(url)
    if err != nil {
        fmt.Println(err)
    }
    body, err := ioutil.ReadAll(res.Body)
    var data map[string]interface{}

    err = json.Unmarshal([]byte(body), &data)
    fmt.Println(err)
    return data
}
