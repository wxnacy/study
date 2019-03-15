package main

import (
     "os"
     "fmt"
     "io/ioutil"
)

// var dir = "/Users/wxnacy/VagrantProjects/test"
var dir = "/Users/wxnacy/Downloads/nvshengs_dir"


func Files(names []string, dir string) []string{

     files, _ := ioutil.ReadDir(dir)
     for _, d := range files {
         if d.IsDir() {
             names = Files(names, fmt.Sprintf("%s/%s",dir, d.Name()))
         } else {
            names = append(names, d.Name())
         }
     }
     return names

}

func main() {
     // dir := "/Users/wxnacy/Downloads/nvshengs_dir"
     names := make([]string, 0)
     names = Files(names, dir)

     fmt.Println(len(names))

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
