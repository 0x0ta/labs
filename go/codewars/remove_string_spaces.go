package kata

import (
  "strings"
)

func NoSpace(word string) string {
  out := ""
  v := strings.Split(word, " ")
  for i := 0; i < len(v); i++ {
    out = out + v[i]
  }
  return out`
  
}
