package kata

func combat(health, damage float64) float64 {
	if health-damage < 0 {
		return 0
	} else {
		return health - damage
	}
}
