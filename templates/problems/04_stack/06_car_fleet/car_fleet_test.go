package car_fleet

import "testing"

func TestCarFleet(t *testing.T) {
	tests := []struct {
		name     string
		target   int
		position []int
		speed    []int
		want     int
	}{
		{"example 1", 12, []int{10, 8, 0, 5, 3}, []int{2, 4, 1, 1, 3}, 3},
		{"single car", 10, []int{3}, []int{3}, 1},
		{"all same speed", 10, []int{0, 2, 4}, []int{2, 2, 2}, 3},
		{"all merge", 10, []int{6, 8}, []int{5, 2}, 1},
		{"no cars", 10, []int{}, []int{}, 0},
		{"two separate fleets", 100, []int{0, 50}, []int{1, 1}, 2},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := carFleet(tt.target, tt.position, tt.speed); got != tt.want {
				t.Errorf("carFleet(%d, %v, %v) = %d, want %d", tt.target, tt.position, tt.speed, got, tt.want)
			}
		})
	}
}
