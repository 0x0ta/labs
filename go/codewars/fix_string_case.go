package kata

import "strings"

func solve(str string) string {
	upperCounter, lowerCounter := 0, 0
	for i := 0; i < len(str); i++ {
		if string(str[i]) == strings.ToUpper(string(str[i])) {
			upperCounter += 1
		} else {
			lowerCounter += 1
		}
	}

	if upperCounter > lowerCounter {
		return strings.ToUpper(str)
	} else {
		return strings.ToLower(str)
	}

}
