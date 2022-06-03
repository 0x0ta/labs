package main

import (
	"fmt"
	"errors"
	"math"
)

func main() {
	fmt.Println(sum(12, 3))
	fmt.Println(sqrt(0))
}

func sum(x int, y int) int {
	return x + y
}

func sqrt(x float64) (float64, error) {
	if x < 0 {
		return 0, errors.New("Undefined for negative")
	}

	return math.Sqrt(x), nil
}
