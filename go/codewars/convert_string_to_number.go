package kata

import (
	"strconv"
)

func StringToNumber(str string) int {
	i, _ := strconv.ParseInt(str, 10, 64)
	return int(i)
}
