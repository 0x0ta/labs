package kata

type NBAPlayer struct {
  Team string
  Ppg  float64
}

func SumPpg(playerOne, playerTwo NBAPlayer) float64 {
  return playerOne.Ppg + playerTwo.Ppg
}