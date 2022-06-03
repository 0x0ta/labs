package kata

import (
	"strings"
)

func IsPalindrome(str string) bool {
	palin := ""
	for i := 1; i <= len(str); i++ {
		palin += string(str[len(str)-i])
	}
	if strings.ToLower(palin) == strings.ToLower(str) {
		return true
	} else {
		return false
	}
}
