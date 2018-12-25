package main

// https://golang.org/pkg/encoding/json/
// https://cloud.tencent.com/developer/section/1141542#stage-100023262

import (
	"encoding/json"
	"fmt"
)

type User struct {
	Id   int    `json:"id"`
	Name string `json:"name"`
}

func main() {
	// 字符串解析为结构体
	s := `{"id": 1, "name": "wxnacy 温"}`

	var user User
	// 将字符串反解析为结构体
	json.Unmarshal([]byte(s), &user)
	fmt.Println(user) // {1 wxnacy}

	var d map[string]interface{}
	// 将字符串反解析为字典
	json.Unmarshal([]byte(s), &d)
    m, _ := json.MarshalIndent(d, "", "    ")

    fmt.Println(string(m))
	fmt.Println(d) // map[id:1 name:wxnacy]

	s = `[1, 2, 3, 4]`
	var a []int
	// 将字符串反解析为数组
	json.Unmarshal([]byte(s), &a)
	fmt.Println(a) // [1 2 3 4]

	// 将结构体解析为字符串
	b, e := json.Marshal(user)
	fmt.Println(e)
	fmt.Println(string(b)) // {"id":1,"name":"wxnacy"}

	b, e = json.Marshal(a)
	fmt.Println(string(b), e) // [1,2,3,4] <nil>

	b, e = json.Marshal(d)
	fmt.Println(string(b), e) // {"id":1,"name":"wxnacy"} <nil>
}
