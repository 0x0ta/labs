package kata

import (
	"fmt"
	"strings"
)

func MultiTable(number int) string {
	output := []string{}
	for i := 1; i <= 10; i++ {
		o := fmt.Sprint(rune(i), " * ", rune(number), " = ", rune(i*number))
		output = append(output, o)
	}
	return strings.Join(output, "\n")
}
