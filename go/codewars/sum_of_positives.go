package kata

func PositiveSum(numbers []int) int {
	out := 0
	for i := 0; i < len(numbers); i++ {
		if numbers[i] > 0 {
			out += numbers[i]
		}
	}

	return out
}
