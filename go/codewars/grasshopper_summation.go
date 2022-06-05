package kata

func Summation(n int) int {
	output := 0
	for i := 1; i <= n; i++ {
		output += i
	}
	return output
}
