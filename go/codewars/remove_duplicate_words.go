package kata

import (
	"strings"
)

func RemoveDuplicateWords(str string) string {
	st := strings.Split(str, " ")
	output := ""
	output_final := []string{}
	for i := 0; i < len(st); i++ {
		if !strings.Contains(output, st[i]) {
			output += st[i]
			output_final = append(output_final, st[i])
		}
	}

	return strings.Join(output_final, " ")
}
