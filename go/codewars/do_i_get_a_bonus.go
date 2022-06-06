package kata

import (
	"fmt"
)

func BonusTime(salary int, bonus bool) string {
	if bonus == true {
		return fmt.Sprintf("£%d", salary*10)
	} else {
		return fmt.Sprintf("£%d", salary)
	}
}
