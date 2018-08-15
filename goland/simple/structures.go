package main

import "fmt"

func main() {
    u := User{1, "wxnacy"}
    fmt.Println(u)
    u1 := User{id: 1}
    fmt.Println(u1)

    var u2 User
    u2.id = 1
    fmt.Println(u2, u2.id)

    Print(u2)

    Test(&u)
    // fmt.Println(&u)
    fmt.Println(&u)
}

type User struct {
    id int
    name string
}

func (u User) SetId(id int) {
    u.id = id
}

func Print(u User) {
    fmt.Println(u)
}

func Test(u *User) {
    // u.id = 2
    // u.name = 'user'
    u.SetId(2)
    fmt.Print(*u)
}
