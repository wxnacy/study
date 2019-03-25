// 自动打开系统浏览器
// 1 各个系统如何使用命令行打开浏览器
// 2 如何判断当前系统
// 3 根据系统调用相应的命令

package main

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
    command, ok := CMDS[runtime.GOOS]
    if !ok {
        fmt.Errorf("don't know how to open browser on %s platform", runtime.GOOS)
    }

    cmd := exec.Command(command, url)
    return cmd.Start()
}

func main() {
    Open("http://baidu.com")
}
