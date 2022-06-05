package kata

func SmallestIntegerFinder(numbers []int) int {
	output := 100000000000
	for _, number := range numbers {
		if number < output {
			output = number
		}
	}
	return output
}
