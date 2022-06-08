package kata

import (
	"fmt"
	"strings"
)

func FreqSeq(str string, sep string) string {
	output := []string{}
	counter := make(map[string]int)
	for i := 0; i < len(str); i++ {
		counter[string(str[i])] += 1
	}
	for i := 0; i < len(str); i++ {
		o := fmt.Sprintf("%v", counter[string(str[i])])
		output = append(output, o)
	}
	return strings.Join(output, sep)
}
