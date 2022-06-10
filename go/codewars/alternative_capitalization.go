package kata

import (
	"strings"
)

func Capitalize(st string) []string {
	stOne := ""
	stTwo := ""
	outputArray := []string{}
	for i := 0; i < len(st); i++ {
		if i%2 == 0 {
			stOne += strings.ToUpper(string(st[i]))
			stTwo += strings.ToLower(string(st[i]))
		} else {
			stOne += strings.ToLower(string(st[i]))
			stTwo += strings.ToUpper(string(st[i]))
		}
	}
	outputArray = append(outputArray, stOne)
	outputArray = append(outputArray, stTwo)
	return outputArray
}
