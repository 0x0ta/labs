package kata

func CountSheeps(numbers []bool) int {
	counter := 0
	for _, sheep := range numbers {
		if sheep == true {
			counter += 1
		}
	}
	return counter
}
