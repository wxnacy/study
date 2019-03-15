package main

import (
     "os"
     "fmt"
     "io/ioutil"
     "strings"
     "os/exec"
)

func main() {
     // dir := "/Users/wxnacy/VagrantProjects/test"
     dir := "/Users/wxnacy/Downloads/nvshengs_dir"

     files, _ := ioutil.ReadDir(dir)
     for _, d := range files {
         name := d.Name()
         index := strings.Index(name, ".")
         if index > 0 && !d.IsDir(){
            fmt.Println(name)
            names := strings.Split(name, ".")
            prefix := names[0]
            fmt.Println(prefix)
            new_dir := fmt.Sprintf("%s/%s", dir, prefix)
            file := fmt.Sprintf("%s/%s", dir, name)
            if !IsDir(new_dir) {
                os.Mkdir(new_dir, os.ModePerm)
            }
            // new_file := fmt.Sprintf("%s/%s", new_dir, name)
            // fmt.Println(file, new_dir)
            cmd := exec.Command("mv", file, new_dir)
            cmd.Run()

         }

     }
}
// 判断所给路径文件/文件夹是否存在
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
