package kata

import (
	"fmt"
	"strconv"
)

func Incrementer(n []int) []int {
	output := []int{}
	for i := 0; i < len(n); i++ {
		fmt.Printf("i: %v n[i]: %v\n", i, n[i])
		o := fmt.Sprintf("%v", n[i]+i+1)
		ot, _ := strconv.Atoi(string(o[len(o)-1]))
		output = append(output, ot)
	}
	return output
}
