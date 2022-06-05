package kata

import (
	"math"
)

func SquareSum(numbers []int) int {
	output := 0.0
	for i := 0; i < len(numbers); i++ {
		output += math.Pow(float64(numbers[i]), 2.0)
	}
	return int(output)
}
