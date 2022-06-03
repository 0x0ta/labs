package main

import (
	"fmt"
)

func main() {
	a := []int{5, 3, 2, 7, 10}
	fmt.Println(a)
	fmt.Println(a[0])

	a = append(a, 13)
	fmt.Println(a)
}
