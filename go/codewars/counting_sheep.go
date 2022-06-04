package kata

import (
	"fmt"
	"strconv"
)

func CountSheep(num int) string {
	output, sheep := "", " sheep..."
	for i := 0; i < num; i++ {
		o := fmt.Sprintf(strconv.Itoa(i+1) + sheep)
		output += o
	}

	return output

}
