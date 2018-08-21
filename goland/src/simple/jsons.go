package main

// https://golang.org/pkg/encoding/json/
// https://cloud.tencent.com/developer/section/1141542#stage-100023262

import (
    "fmt"
    "encoding/json"
)

type User struct {
    Id int `json:"id"`
    Name string `json:"name"`
}

func main() {
    // 字符串解析为结构体
    s := `{"id": 1, "name": "wxnacy"}`

    var user User
    json.Unmarshal([]byte(s), &user)
    fmt.Println(user)   // {1 wxnacy}

    s = `[1, 2, 3, 4]`
    var a []int
    json.Unmarshal([]byte(s), &a)
    fmt.Println(a)      // [1 2 3 4]

    b, e := json.Marshal(user)
    fmt.Println(e)
    fmt.Println(string(b))  // {"id":1,"name":"wxnacy"}

    b, e = json.Marshal(a)
    fmt.Println(string(b), e)   // [1,2,3,4] <nil>
}
