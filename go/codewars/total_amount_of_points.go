package kata

import (
	"strings"
)

func Points(games []string) int {
	points_total := 0
	for i := 0; i < len(games); i++ {
		home := strings.Split(games[i], ":")
		if home[0] > home[1] {
			points_total += 3
		} else if home[0] == home[1] {
			points_total += 1
		}
	}
	return points_total
}
