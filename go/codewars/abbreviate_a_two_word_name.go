package kata

import (
	"strings"
)

func AbbrevName(name string) string {
	names := strings.Split(name, " ")
	abbr := string(names[0][0]) + "." + string(names[1][0])
	return strings.ToUpper(abbr)
}
