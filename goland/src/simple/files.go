package main

import (
	"fmt"
	"log"
	"os"
)

func checkErr(err error) {
    if err != nil {
        panic(err)
    }
}

func main() {

	// Func1()
    // exists := Exists("file.go")
    // fmt.Println(exists)

    f, err := os.Create("test")
    checkErr(err)
    f.WriteString("ww")
    f.Close()
    fmt.Println(os.Getenv("HOME"))
    err = os.MkdirAll("/Users/wxnacy/.tm/credentials", os.ModePerm)
    // err := os.MkdirAll("sss", os.ModePerm)
    fmt.Println(err)
    os.Remove("test")
}

func Func1() {
	fmt.Println("Hello World ")
	file, err := os.Stat("loops.go")
	if err != nil {
		// fmt.Println(err)
		log.Fatal(err)
	}

	fmt.Println(file.Name(), file.Size(), file.Mode(), file.ModTime(),
		file.IsDir(), file.Sys())
	fmt.Printf("System interface type: %T\n", file.Sys())
	fmt.Printf("System info: %+v\n\n", file.Sys())
}


func Exists(path string) bool {
	_, err := os.Stat(path)    //os.Stat获取文件信息
	if err != nil {
		if os.IsExist(err) {
			return true
		}
		return false
	}
	return true
}

// 判断所给路径是否为文件夹
func IsDir(path string) bool {
	s, err := os.Stat(path)
	if err != nil {
		return false
	}
	return s.IsDir()
}

// 判断所给路径是否为文件
func IsFile(path string) bool {
	return !IsDir(path)
}

