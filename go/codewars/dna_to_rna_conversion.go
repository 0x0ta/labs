package kata

import (
	"strings"
)

func DNAtoRNA(dna string) string {
	output := ""
	for i := 0; i < len(dna); i++ {
		if string(dna[i]) == "T" {
			output += "U"
		} else {
			output += strings.ToUpper(string(dna[i]))
		}
	}

	return output
}
