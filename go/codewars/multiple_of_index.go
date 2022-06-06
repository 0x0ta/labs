package kata

func multipleOfIndex(ints []int) []int {
	output := []int{}
	for idx, value := range ints {
		if idx != 0 && value%idx == 0 {
			output = append(output, value)
		}
	}
	return output
}
