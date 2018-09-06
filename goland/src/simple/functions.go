package main

import "fmt"

func main() {
	fmt.Println(Sum(1, 2))
	Func1("a", 2)
	fmt.Println(Func2("a", "b"))

	a, b := 1, 2
	Func3(&a, &b)
	fmt.Println(a, b)

	Func4()

	f5 := Func5()
	fmt.Println(f5())
	fmt.Println(f5())

	fmt.Println(Func6(1)(2))

	var u User
	u.id = 1
	fmt.Println(u.GetId())

	c, _ := Func7()
	fmt.Println(c)

}

func Sum(a, b int) int {
	return a + b
}

func Func1(a string, b int) {
	fmt.Println(a, b)
}

func Func2(a, b string) (string, string) {
	return a, b
}

func Func3(a, b *int) {
	temp := *a
	*a = *b
	*b = temp
}

func Func4() {
	test := func(a int) {
		fmt.Println(a)
	}

	test(1)
}

func Func5() func() int {
	i := 0

	return func() int {
		i++
		return i
	}
}

func Func6(a int) func(b int) int {
	return func(b int) int {
		a++
		b++
		fmt.Println(a, b)
		return a + b
	}
}

type User struct {
	id int
}

func (u User) GetId() int {
	return u.id
}

func Func7() (int, int) {
	return 1, 2
}
