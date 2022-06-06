package kata

func Grow(arr []int) int {
	output := 1
	for i := 0; i < len(arr); i++ {
		output = output * arr[i]
	}
	return output
}
