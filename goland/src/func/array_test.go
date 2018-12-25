package function

import (
    "testing"
    "reflect"
)

func TestInArray(t *testing.T) {
    var index int

    index = inArray(1, []int{1, 2})
    if index != 0 {
        t.Errorf("%d is error", index)
    }

    index = inArray(3, []int{1, 2})
    if index != -1 {
        t.Errorf("%d is error", index)
    }

    index = inArray("a", []string{"b", "c"})
    if index != -1 {
        t.Errorf("%d is error", index)
    }

    index = inArray("c", []string{"b", "c"})
    if index != 1 {
        t.Errorf("%d is error", index)
    }
}

func TestRemove(t *testing.T) {

    var arr []interface{}

    arr = remove([]int{1,2,3}, 1)
    t.Log(reflect.TypeOf(arr))
    // if !reflect.DeepEqual(arr, []int{1,3}) {
        // t.Errorf("%v is error", arr)
    // }
}
