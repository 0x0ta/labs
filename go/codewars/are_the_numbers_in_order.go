package kata

import (
	"sort"
)

func InAscOrder(src []int) bool {
	dst := make([]int, len(src))
	copy(dst, src)
	sort.Ints(dst)
	for i := 0; i < len(src); i++ {
		if src[i] == dst[i] {
			continue
		} else {
			return false
		}
	}
	return true
}
