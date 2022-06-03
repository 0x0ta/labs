package main

import (
	"fmt"
)

func main() {
	fmt.Println("Hello, world")

	var x int = 100
	var y string = "old string"
	var b rune
	var c bool = true
	var a byte = 0x00

	d := "string"

	y = "test string"
	a = 0x46

	fmt.Println("x = ", x)
	fmt.Println("y = ", y)
	fmt.Println("b = ", b)
	fmt.Println("c = ", c)
	fmt.Println("a = ", a)
	fmt.Println(d)

	if x < 100 {
		fmt.Println(x * x)
	} else if x > 100 {
		fmt.Println(x - 1)
	} else {
		fmt.Println("mehheeee")
	}

}
