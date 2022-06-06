package kata

func monkeyCount(n int) []int {
	output := []int{}
	for i := 1; i <= n; i++ {
		output = append(output, i)
	}
	return output
}
