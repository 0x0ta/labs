package kata

func GetCount(str string) (count int) {
	vowels := []string{"a", "e", "i", "o", "u"}
	for i := 0; i < len(str); i++ {
		for v := 0; v < len(vowels); v++ {
			if string(str[i]) == string(vowels[v]) {
				count += 1
			}
		}
	}
	return count
}
