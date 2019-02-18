package main

import (
    "fmt"
    "encoding/json"
)

func main() {
	u := User{1, "wxnacy"}
    fmt.Println(u)
    fmt.Println(u.ToString())   // User Id: 1, Name: wxnacy
    fmt.Println(u.ToJson())     // {"id":1,"name":"wxnacy"}

    var a User
    fmt.Println(a)              // {0 }
    a.Id = 1
    fmt.Println(a)              // {1 }

    var b = User{Name: "wxnacy"}
    fmt.Println(b)              // {0 wxnacy}

    b.SetId(1)
    fmt.Println(b)              // {1 wxnacy}

    ChangeUser(&b)
    fmt.Println(b)              // {2 wxnacy}

    c := new(User)
    fmt.Println(c)              // &{0 }

    d := &User{1, "wxnacy"}
    fmt.Println(d)              // &{1 wxnacy}

    h := Human{Msg: "I am a Human"}
    // fmt.Println(h.ToString())
    fmt.Println(h)
    // m := Man{Human{Msg: "I am a Man"}}
    // fmt.Println(m.ToString())

    // m1 := Man{Id: 1}
    // m1.Msg = "I am a Man"
    // fmt.Println(m1.ToString())

}

type User struct {
    Id   int `json:"id"`
    Name string `json:"name"`
}

func (this *User) SetId(id int) {
    this.Id = id
}

func (u User) ToString() string {
    return fmt.Sprintf("User Id: %d, Name: %s", u.Id, u.Name)
}

func (u User) ToJson() string {
    b, e := json.Marshal(u)
    if e != nil {
        return ""
    }
    return string(b)
}

func ChangeUser(u *User) {
    u.SetId(2)
}

type Human struct {
    Name string
    Msg string
    IsMan bool
}

func (this Human) ToString() string {
    return this.Msg
}

type Man struct {
    Human
    Id int
}

