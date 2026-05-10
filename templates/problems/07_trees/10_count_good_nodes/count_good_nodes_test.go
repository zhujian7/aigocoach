package count_good_nodes

import "testing"

func TestGoodNodes(t *testing.T) {
	tests := []struct {
		name string
		vals []int
		want int
	}{
		{"example 1", []int{3, 1, 4, 3, -101, 1, 5}, 4},
		{"example 2", []int{3, 3, -101, 4, 2}, 3},
		{"single node", []int{1}, 1},
		{"all same", []int{1, 1, 1, 1, 1}, 5},
		{"decreasing", []int{5, 3, 4, 1, 2, -101, 3}, 1},
		{"increasing left", []int{1, 2, -101, 3}, 3},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			root := buildTreeHelper(tt.vals)
			if got := goodNodes(root); got != tt.want {
				t.Errorf("goodNodes() = %v, want %v", got, tt.want)
			}
		})
	}
}
