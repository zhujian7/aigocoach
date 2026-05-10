package permutations

import (
	"sort"
	"testing"
)

func sortPermutations(result [][]int) {
	sort.Slice(result, func(i, j int) bool {
		a, b := result[i], result[j]
		for k := 0; k < len(a) && k < len(b); k++ {
			if a[k] != b[k] {
				return a[k] < b[k]
			}
		}
		return len(a) < len(b)
	})
}

func TestPermute(t *testing.T) {
	tests := []struct {
		name string
		nums []int
		want [][]int
	}{
		{
			name: "three elements",
			nums: []int{1, 2, 3},
			want: [][]int{
				{1, 2, 3}, {1, 3, 2}, {2, 1, 3}, {2, 3, 1}, {3, 1, 2}, {3, 2, 1},
			},
		},
		{
			name: "single element",
			nums: []int{1},
			want: [][]int{{1}},
		},
		{
			name: "two elements",
			nums: []int{0, 1},
			want: [][]int{{0, 1}, {1, 0}},
		},
		{
			name: "negative numbers",
			nums: []int{-1, 0, 1},
			want: [][]int{
				{-1, 0, 1}, {-1, 1, 0}, {0, -1, 1}, {0, 1, -1}, {1, -1, 0}, {1, 0, -1},
			},
		},
		{
			name: "four elements count",
			nums: []int{1, 2, 3, 4},
			want: nil, // checked by count
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := permute(tt.nums)
			if tt.want == nil {
				// just check count: 4! = 24
				if len(got) != 24 {
					t.Errorf("permute(%v) returned %d permutations, want 24", tt.nums, len(got))
				}
				return
			}
			sortPermutations(got)
			sortPermutations(tt.want)
			if !equalSubsets(got, tt.want) {
				t.Errorf("permute(%v) = %v, want %v", tt.nums, got, tt.want)
			}
		})
	}
}
