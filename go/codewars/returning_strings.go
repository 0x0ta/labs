package kata

import (
	"fmt"
)

func Greet(name string) string {
	str := fmt.Sprintf("Hello, %v how are you doing today?", name)
	return str
}
