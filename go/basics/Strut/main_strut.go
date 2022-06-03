package main

import (
	"fmt"
)

type person struct {
	name string
	age  int
	boo  bool
}

func pointer(x *int) {
	*x++
}

func main() {
	p := person{name: "Hayley", age: 36, boo: false}
	fmt.Println(p)
	fmt.Println("Name:", p.name)
	fmt.Println("Age:", p.age)

	i := 7
	fmt.Println("pointer before:", &i)
	pointer(&i)
	fmt.Println(i)
	fmt.Println("pointer after:", &i)
}
