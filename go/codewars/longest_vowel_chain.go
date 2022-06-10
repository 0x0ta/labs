package kata

import (
	"strings"
)

func Solve(s string) int {
	vowelChain := []string{}
	o := ""
	for i := 0; i < len(s); i++ {
		if strings.Contains("aeiou", string(s[i])) {
			o += string(s[i])
		} else {
			o = ""
		}
		vowelChain = append(vowelChain, o)
	}
	vowelCounter := len(vowelChain[0])
	for i := 0; i < len(vowelChain); i++ {
		if len(vowelChain[i]) > vowelCounter {
			vowelCounter = len(vowelChain[i])
		}
	}
	return vowelCounter
}
