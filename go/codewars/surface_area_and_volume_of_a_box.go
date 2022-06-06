package kata

func GetSize(w, h, d int) [2]int {
	return [2]int{(w*h + h*d + d*w) * 2, w * h * d}
}
