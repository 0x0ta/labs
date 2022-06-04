package kata

import (
	"strings"
)

func ReverseWords(str string) string {
	strArr := []string{}
	revStr := []string{}
	strArr = strings.Split(str, " ")
	for i := len(strArr) - 1; i >= 0; i-- {
		revStr = append(revStr, strArr[i])
	}
	return strings.Join(revStr, " ") // reverse those words
}
