package detect_squares

import "testing"

func TestDetectSquares(t *testing.T) {
	tests := []struct {
		name       string
		addPoints  [][]int
		queryPoint []int
		expected   int
	}{
		{
			"basic square",
			[][]int{{3, 10}, {11, 10}, {11, 2}},
			[]int{3, 2},
			1,
		},
		{
			"no square possible",
			[][]int{{1, 1}, {2, 2}},
			[]int{3, 3},
			0,
		},
		{
			"duplicate points multiply count",
			[][]int{{3, 10}, {3, 10}, {11, 10}, {11, 2}},
			[]int{3, 2},
			2,
		},
		{
			"multiple squares from one query",
			[][]int{{0, 0}, {1, 0}, {1, 1}, {0, 1}, {2, 0}, {2, 2}, {0, 2}},
			[]int{0, 0},
			2,
		},
		{
			"no points added",
			[][]int{},
			[]int{0, 0},
			0,
		},
		{
			"collinear points",
			[][]int{{1, 1}, {2, 1}, {3, 1}},
			[]int{0, 1},
			0,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			ds := Constructor()
			for _, p := range tt.addPoints {
				ds.Add(p)
			}
			got := ds.Count(tt.queryPoint)
			if got != tt.expected {
				t.Errorf("Count(%v) = %d, want %d", tt.queryPoint, got, tt.expected)
			}
		})
	}
}
