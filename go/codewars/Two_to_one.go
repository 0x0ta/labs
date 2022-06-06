package kata

import (
	"sort"
	"strings"
)

func TwoToOne(s1 string, s2 string) string {
	var temp = []string{s1, s2}
	sort.Strings(temp)
	output := []string{}

	for i := 0; i < len(temp); i++ {
		for v := 0; v < len(temp[i]); v++ {
			if strings.Contains(strings.Join(output, ""), string(temp[i][v])) != true {
				output = append(output, string(temp[i][v]))
			}

		}
	}
	sort.Strings(output)
	return strings.Join(output, "")
}
