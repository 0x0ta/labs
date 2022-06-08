package kata

import (
	"strings"
)

func ReverseWords(str string) string {
	st := strings.Split(str, " ")
	output := []string{}

	for i := 0; i < len(st); i++ {
		o := ""
		for c := 0; c < len(string(st[i])); c++ {
			o = string(st[i][c]) + o
		}
		output = append(output, string(o))
	}
	return strings.Join(output, " ")
}
