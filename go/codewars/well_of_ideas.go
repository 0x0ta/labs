package kata

func Well(x []string) string {
	counter := 0
	for i := 0; i < len(x); i++ {
		if x[i] == "good" {
			counter += 1
		}
	}
	if counter <= 0 {
		return "Fail!"
	} else if counter > 0 && counter <= 2 {
		return "Publish!"
	} else {
		return "I smell a series!"
	}
}
