package kata

import (
	"fmt"
	"strings"
)

func Accum(s string) string {
	output := []string{}
	for i := 0; i < len(s); i++ {
		o := ""
		for c := 0; c <= i; c++ {
			o += fmt.Sprintf("%v", strings.ToLower(string(s[i])))
		}
		output = append(output, strings.Title(o))
	}
	return strings.Join(output, "-")
}
