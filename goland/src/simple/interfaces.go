package main

import "fmt"

func main() {
	var p Phone = new(MiPhone)
	fmt.Println(p.GetName())

	var p1 = new(MiPhone)
	fmt.Println(p1.GetName())

	var p2 = MiPhone{}
	fmt.Println(p2.GetName())

}

type Phone interface {
	GetName() string
}

type MiPhone struct {
}

func (miPhone MiPhone) GetName() string {
	return "this is mi phone"
}
