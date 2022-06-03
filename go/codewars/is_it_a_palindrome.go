package kata

import (
	"strings"
)

func IsPalindrome(str string) bool {
	str = strings.ToLower(str)
	palin := ""
	for i := 1; i <= len(str); i++ {
		palin += string(str[len(str)-i])
	}
	if palin == str {
		return true
	} else {
		return false
	}
}
