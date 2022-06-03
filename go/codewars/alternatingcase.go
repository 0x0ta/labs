package kata

import (
	"strings"
)

func ToAlternatingCase(str string) string {
	output := ""
	for i := 0; i < len(str); i++ {
		if string(str[i]) == strings.ToUpper(string(str[i])) {
			output += strings.ToLower(string(str[i]))
		} else {
			output += strings.ToUpper(string(str[i]))
		}
	}
	return output
}
