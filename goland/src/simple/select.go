package main

import "fmt"

func main() {
   var  c3 chan int
   c1 := make(chan int, 1)
   var i1, i2 int
   c2 := make(chan bool, 1)
   c2 <- true

   select {
      case <-c1:
         fmt.Printf("received ", i1, " from c1\n")
        case <- c2:
         fmt.Printf("sent ", i2, " to c2\n")
      case i3, ok := (<-c3):  // same as: i3, ok := <-c3
         if ok {
            fmt.Printf("received ", i3, " from c3\n")
         } else {
            fmt.Printf("c3 is closed\n")
         }
      default:
         fmt.Printf("no communication\n")
   }
}

