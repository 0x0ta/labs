package kata

import (
	"crypto/md5"
	"fmt"
)

func PassHash(str string) string {
	hashString := []byte(str)
	output := fmt.Sprintf("%x", md5.Sum(hashString))
	return output
}
