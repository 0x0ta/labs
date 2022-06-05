package kata

func SmallestIntegerFinder(numbers []int) int {
	output := numbers[0]
	for _, number := range numbers {
		if number < output {
			output = number
		}
	}
	return output
}
