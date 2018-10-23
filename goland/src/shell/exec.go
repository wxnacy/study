package main

import (
    "os/exec"
    "fmt"
    "os"
    "strings"
)

func main() {
    var ip, whoami []byte
    var err error
    var cmd *exec.Cmd

    // 执行单个shell命令时, 直接运行即可
    cmd = exec.Command("whoami")
    if whoami, err = cmd.Output(); err != nil {
        fmt.Println(err)
        os.Exit(1)
    }
    // 默认输出有一个换行
    fmt.Println(string(whoami))
    // 指定参数后过滤换行符
    fmt.Println(strings.Trim(string(whoami), "\n"))

    fmt.Println("====")

    // mac平台获取ip地址
    // 执行连续的shell命令时, 需要注意指定执行路径和参数, 否则运行出错
    cmd = exec.Command("/bin/sh", "-c", `/sbin/ifconfig en0 | grep -E 'inet ' |  awk '{print $2}'`)
    if ip, err = cmd.Output(); err != nil {
        fmt.Println(err)
        os.Exit(1)
    }
    fmt.Println(string(ip))
    fmt.Println(strings.Trim(string(ip), "\n"))
}
