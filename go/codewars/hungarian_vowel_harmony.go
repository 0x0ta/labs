package kata

import (
	"fmt"
	"strings"
)

func Dative(word string) string {
	nek := []string{"e", "é", "i", "í", "ö", "ő", "ü", "ű"}
	nak := []string{"a", "á", "o", "ó", "u", "ú"}
	o := ""

	for i := 0; i < len(nek); i++ {
		if strings.Contains(word, string(nek[i])) {
			o = fmt.Sprintf("%vnek", word)
		}
	}
	for i := 0; i < len(nak); i++ {
		if strings.Contains(word, string(nak[i])) {
			o = fmt.Sprintf("%vnak", word)
		}
	}
	return o
}
