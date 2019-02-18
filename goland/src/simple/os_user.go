package main
// 使用 os/user 模块获取机器用户信息

import (
     "fmt"
     "os/user"
)

func handleErr(err error){
    if err != nil {
        fmt.Println(err)
    }
}

func main() {
    u, err := user.Current()
    handleErr(err)
    fmt.Println("当前用户")
    fmt.Printf("Gid %s\n", u.Gid)
    fmt.Printf("Uid %s\n", u.Uid)
    fmt.Printf("Username %s\n", u.Username)
    fmt.Printf("Name %s\n", u.Name)
    fmt.Printf("HomeDir %s\n", u.HomeDir)
    fmt.Println("")

    u, err = user.Lookup("wxnacy")
    handleErr(err)
    fmt.Println("根据 Username wxnacy 查询")
    fmt.Printf("Gid %s\n", u.Gid)
    fmt.Printf("Uid %s\n", u.Uid)
    fmt.Printf("Username %s\n", u.Username)
    fmt.Printf("Name %s\n", u.Name)
    fmt.Printf("HomeDir %s\n", u.HomeDir)
    fmt.Println("")

    u, err = user.LookupId("501")
    handleErr(err)
    fmt.Println("根据 Uid 501 查询")
    fmt.Printf("Gid %s\n", u.Gid)
    fmt.Printf("Uid %s\n", u.Uid)
    fmt.Printf("Username %s\n", u.Username)
    fmt.Printf("Name %s\n", u.Name)
    fmt.Printf("HomeDir %s\n", u.HomeDir)


    // 当前用户
    // Gid 20
    // Uid 501
    // Username wxnacy
    // Name wxnacy
    // HomeDir /Users/wxnacy

    // 根据 Username wxnacy 查询
    // Gid 20
    // Uid 501
    // Username wxnacy
    // Name wxnacy
    // HomeDir /Users/wxnacy

    // 根据 Uid 501 查询
    // Gid 20
    // Uid 501
    // Username wxnacy
    // Name wxnacy
    // HomeDir /Users/wxnacy
}
