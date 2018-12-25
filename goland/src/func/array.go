package function

import (
    "reflect"
)

func inArray(val interface{}, array interface{}) (index int) {
    // 判断 val 是否在 array 中
    index = -1

    switch reflect.TypeOf(array).Kind() {
        case reflect.Slice: {
            s := reflect.ValueOf(array)
            for i := 0; i < s.Len(); i++ {
                if reflect.DeepEqual(val, s.Index(i).Interface()) {
                    index = i
                    return
                }
            }
        }
    }
    return
}

// func remove(array []reflect.Type, index int) (arr []reflect.Type) {

    // arr = append(array[0:index], array[index+1:]...)

    // return
// }

func remove(array interface{}, index int) (arr interface{}) {

    switch reflect.TypeOf(array).Kind() {
        case reflect.Slice: {
            s := reflect.ValueOf(array)
            arr s.Slice(0, index).Interface()

        }
    }

    return
}
