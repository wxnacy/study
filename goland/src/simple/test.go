package main

import (
    "fmt"
    "reflect"
)

func main() {
    fmt.Println("Hello World") 
    fmt.Println( float64(101) / 2 )
    a := float64(101) / 2
    // fmt.Println( int(float64(33) / 345 * 20))
    fmt.Println( 101 % 2 )
    fmt.Println(reflect.TypeOf(a))

    fmt.Println(fmt.Sprintf("%.0f", 1.9))
}
