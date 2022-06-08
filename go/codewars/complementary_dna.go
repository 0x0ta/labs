package kata

import (
	//"strings"
	"fmt"
)

func DNAStrand(dna string) string {
	output := ""
	fmt.Println(dna)
	for i := 0; i < len(dna); i++ {
		o := ""
		if string(dna[i]) == "A" {
			o = "T"
		} else if string(dna[i]) == "T" {
			o = "A"
		} else if string(dna[i]) == "C" {
			o = "G"
		} else if string(dna[i]) == "G" {
			o = "C"
		}

		output += o
	}
	return output
}
