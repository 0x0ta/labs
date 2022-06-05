package kata

func GetGrade(a, b, c int) rune {
	output := 0
	total := a + b + c
	average := total / 3
	switch {
	case average >= 0 && average < 60:
		output = 70
	case average >= 60 && average < 70:
		output = 68
	case average >= 70 && average < 80:
		output = 67
	case average >= 80 && average < 90:
		output = 66
	case average >= 90:
		output = 65
	}
	return rune(output)
}
