package kata

import (
	"fmt"
)

func Greet(name string) string {
	if name == "Johnny" {
		return "Hello, my love!"
	} else {
		output := fmt.Sprintf("Hello, %v!", name)
		return output
	}
}
