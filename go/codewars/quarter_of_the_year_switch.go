package kata

func QuarterOf(month int) int {
	output := 0

	switch month := month; month {
	case 1, 2, 3:
		output = 1
	case 4, 5, 6:
		output = 2
	case 7, 8, 9:
		output = 3
	case 10, 11, 12:
		output = 4
	}

	return output
}
