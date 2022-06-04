package kata

func Maps(x []int) []int {
	output := []int{}
	for i := 0; i < len(x); i++ {
		output = append(output, x[i]*2)
	}
	return output
}
