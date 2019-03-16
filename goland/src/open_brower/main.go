package main
// 自动打开系统默认浏览器
// 1 各个平台打开浏览器的命令是什么
//      windows     start
//      darwin      open
//      linux       xdg-open
// 2 判断当前所处系统
// 3 编写代码执行命令

import (
    "runtime"
    "fmt"
    "os/exec"
)

var CMDS = map[string]string{
    "windows": "start",
    "darwin": "open",
    "linux": "xdg-open",
}

func Open(url string) error {
    command , ok := CMDS[runtime.GOOS]
    if !ok {
        fmt.Errorf("don't know how to open browser on %s platform", runtime.GOOS)
    }
    cmd := exec.Command(command, url)
    return cmd.Start()
}

func main() {
    Open("http://baidu.com")
}

