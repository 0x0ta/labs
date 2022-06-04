package kata

func OddCount(n int) int {
	output := 0
	for i := 1; i < n; i++ {
		if i%2 == 0 {
			output += 1
		}
	}

	return output
}
