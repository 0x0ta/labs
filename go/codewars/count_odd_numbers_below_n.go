package kata

func OddCount(n int) int {
	output := []int{}
	for i := 1; i < n; i++ {
		if i%2 == 0 {
			output = append(output, i)
		}
	}

	return len(output)
}
