package kata

func Solution(word string) string {
	reverse := ""
	for i := 0; i < len(word); i++ {
		reverse += string(word[len(word)-i-1])
	}
	return reverse
}
