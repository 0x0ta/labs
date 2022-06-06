package kata

import (
	"strings"
)

func ToJadenCase(str string) string {
	words := strings.Split(str, " ")
	output := []string{}
	for i := 0; i < len(words); i++ {
		word := ""
		for c := 0; c < len(words[i]); c++ {
			if c == 0 {
				word += strings.ToUpper(string(words[i][c]))
			} else {
				word += string(words[i][c])
			}
		}
		output = append(output, word)
	}
	return strings.Join(output, " ")
}
