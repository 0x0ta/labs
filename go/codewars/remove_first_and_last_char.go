package kata

func RemoveChar(word string) string {
	output := ""
	for i := 0; i < len(word) && len(word) > 2; i++ {
		if i != 0 && i != (len(word)-1) {
			output += string(word[i])
		}
	}

	return output
}
