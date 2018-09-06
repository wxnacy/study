package main

import (
    "fmt"
    "flag"
    "os"
)

var version bool
var name string
var age *int

func InitArgs() {
    flag.BoolVar(&version, "v", false, "Get Version")
    flag.StringVar(&name, "name", "", "Get Name")
    age = flag.Int("age", 0, "Get Age")
}

func main() {
    InitArgs()

    flag.Parse()

    fmt.Printf("version %t name %s age %d", version, name, *age)
    fmt.Println("")
    fmt.Printf("args %s", flag.Args())
    fmt.Println("")
    fmt.Printf("args num %d, flag args num %d", flag.NArg(), flag.NFlag())
    fmt.Println("")
    fmt.Printf("os.Args %s", os.Args)
    fmt.Println("")


    // > $ go run src/simple/flag.go -v -name wxnacy -age 2 arg1 arg2
    // version true name wxnacy age 2
    // args [arg1 arg2]
    // args num 2, flag args num 3
    // os.Args [/var/folders/kz/8syfctw919zdt3shr9w5j8v00000gn/T/go-build512483375/b001/exe/flag -v -name wxnacy -age 2 arg1 arg2]

}
