package kata

import (
	"fmt"
	"strings"
)

func DontGiveMeFive(start int, end int) int {
	counter := 0
	for i := start; i <= end; i++ {
		if strings.Contains(fmt.Sprintf("%v", i), "5") == false {
			counter += 1
		}
	}
	return counter
}
