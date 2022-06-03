package main

import (
	"fmt"
)

func main() {
	b := true
	a := make(map[string]int)
	a["test"] = 12
	a["test2"] = 13
	a["test123123"] = 123123
	a["deleteme"] = 6666
	fmt.Println(a)


	// For loop using a bool value to stop the loop
	for b {
		fmt.Println(a["deleteme"])
		delete(a, "deleteme")
		b = false
		fmt.Println(a)
	}

	for key, value := range a {
		fmt.Println("key:", key, "value:", value)
	}

	// basic for loop with initialisation of the i variable, the condition
	// and the incrementation value in the same line
	for i := 0; i < 5; i++ {
		fmt.Println(i)
	}

	i := 0

	// basic for loop with incrementation inside the loop
	for i < 5 {
		fmt.Println(i)
		i++
	}

	arr := []string{"a", "b", "c"}

	for index, value := range arr {
		fmt.Println("index:", index, "value:", value)
	}
}
