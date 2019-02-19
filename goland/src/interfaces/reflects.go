package main

import (
     "fmt"
     "reflect"
)

// 利用 reflect 反射方法判断 val 是否包含在 array 中，如果包含返回索引位置
func InArray(val interface{}, array interface{}) (index int) {
    index = -1
    switch reflect.TypeOf(array).Kind() {
        case reflect.Slice: {
            arr := reflect.ValueOf(array)
            for i := 0; i < arr.Len(); i++ {
                if reflect.DeepEqual(val, arr.Index(i).Interface()) {
                    index = i
                    return
                }
            }
        }
    }
    return
}

func main() {
     var arr = []int{1,2,3,4}
     fmt.Println(InArray(3, arr))
     // 2

     var arr2 = []string{"a", "b", "c"}
     fmt.Println(InArray("d", arr2))
     // -1
}
