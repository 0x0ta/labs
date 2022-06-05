package kata

import (
	"fmt"
	"sort"
	"strings"
)

func TwoSort(arr []string) string {
	output := []string{}
	sort.Strings(arr)
	fmt.Println(arr)
	for i := 0; i < len(arr[0]); i++ {
		output = append(output, string(arr[0][i]))
	}
	return strings.Join(output, "***")
}
