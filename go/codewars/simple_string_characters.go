package kata

import (
	"unicode"
)

func Solve(s string) []int {
	uc_counter, lc_counter, nu_counter, sp_counter := 0, 0, 0, 0
	for i := 0; i < len(s); i++ {
		if unicode.IsUpper(rune(s[i])) {
			uc_counter += 1
		} else if unicode.IsLower(rune(s[i])) {
			lc_counter += 1
		} else if unicode.IsDigit(rune(s[i])) {
			nu_counter += 1
		} else {
			sp_counter += 1
		}
	}
	output := []int{uc_counter, lc_counter, nu_counter, sp_counter}
	return output
}
