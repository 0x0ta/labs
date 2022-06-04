package kata

func HowMuchILoveYou(i int) string {
	arr := []string{"I love you", "a little", "a lot", "passionately", "madly", "not at all"}
	return arr[(i-1)%6]
}
