package kata

func CountPositivesSumNegatives(numbers []int) []int {
	neg, pos := 0, 0
	for i := 0; i < len(numbers); i++ {
		if numbers[i] <= 0 {
			neg += numbers[i]
		} else {
			pos += 1
		}
	}
	res := []int{pos, neg}
	return res // your code here
}
