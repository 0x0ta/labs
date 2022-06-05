package kata

import (
	"strconv"
)

func FakeBin(x string) string {
	output := ""
	for i := 0; i < len(x); i++ {
		char, _ := strconv.Atoi(string(x[i]))
		if char < 5 {
			output += "0"
		} else {
			output += "1"
		}
	}
	return output
}
