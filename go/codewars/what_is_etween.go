package kata

func Between(a, b int) []int {
	res := []int{}
	for i := a; i <= b; i++ {
		res = append(res, i)
	}
	return res
}
