package kata

func ReverseSeq(n int) []int {
	output := []int{}
	for i := n; i >= 1; i-- {
		output = append(output, i)
	}
	return output
}
