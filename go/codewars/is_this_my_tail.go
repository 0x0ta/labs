package kata

func CorrectTail(body string, tail rune) bool {
	if string(body[len(body)-1]) != string(tail) {
		return false
	} else {
		return true
	}
}
