package combination_sum_ii

import (
	"sort"
	"testing"
)

func TestCombinationSum2(t *testing.T) {
	tests := []struct {
		name       string
		candidates []int
		target     int
		want       [][]int
	}{
		{
			name:       "example 1",
			candidates: []int{10, 1, 2, 7, 6, 1, 5},
			target:     8,
			want:       [][]int{{1, 1, 6}, {1, 2, 5}, {1, 7}, {2, 6}},
		},
		{
			name:       "example 2",
			candidates: []int{2, 5, 2, 1, 2},
			target:     5,
			want:       [][]int{{1, 2, 2}, {5}},
		},
		{
			name:       "no combination",
			candidates: []int{3, 5},
			target:     1,
			want:       [][]int{},
		},
		{
			name:       "single element matches",
			candidates: []int{1},
			target:     1,
			want:       [][]int{{1}},
		},
		{
			name:       "all duplicates",
			candidates: []int{2, 2, 2},
			target:     4,
			want:       [][]int{{2, 2}},
		},
		{
			name:       "target zero",
			candidates: []int{1, 2, 3},
			target:     0,
			want:       [][]int{{}},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := combinationSum2(tt.candidates, tt.target)
			for _, c := range got {
				sort.Ints(c)
			}
			sortCombinations(got)
			sortCombinations(tt.want)
			if len(got) != len(tt.want) {
				t.Fatalf("combinationSum2(%v, %d) returned %d results, want %d\ngot:  %v\nwant: %v",
					tt.candidates, tt.target, len(got), len(tt.want), got, tt.want)
			}
			if !equalSubsets(got, tt.want) {
				t.Errorf("combinationSum2(%v, %d) = %v, want %v",
					tt.candidates, tt.target, got, tt.want)
			}
		})
	}
}
