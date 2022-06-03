package kata

func RepeatStr(repetitions int, value string) string {
	output := ""
	for i := 0; i < repetitions; i++ {
		output += value
	}
	return output
}
