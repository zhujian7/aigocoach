package combination_sum

import (
	"sort"
	"testing"
)

func sortCombinations(result [][]int) {
	for _, c := range result {
		sort.Ints(c)
	}
	sort.Slice(result, func(i, j int) bool {
		a, b := result[i], result[j]
		if len(a) != len(b) {
			return len(a) < len(b)
		}
		for k := 0; k < len(a); k++ {
			if a[k] != b[k] {
				return a[k] < b[k]
			}
		}
		return false
	})
}

func TestCombinationSum(t *testing.T) {
	tests := []struct {
		name       string
		candidates []int
		target     int
		want       [][]int
	}{
		{
			name:       "example 1",
			candidates: []int{2, 3, 6, 7},
			target:     7,
			want:       [][]int{{2, 2, 3}, {7}},
		},
		{
			name:       "example 2",
			candidates: []int{2, 3, 5},
			target:     8,
			want:       [][]int{{2, 2, 2, 2}, {2, 3, 3}, {3, 5}},
		},
		{
			name:       "no combination",
			candidates: []int{2},
			target:     1,
			want:       [][]int{},
		},
		{
			name:       "single candidate equals target",
			candidates: []int{1},
			target:     1,
			want:       [][]int{{1}},
		},
		{
			name:       "single candidate repeated",
			candidates: []int{1},
			target:     3,
			want:       [][]int{{1, 1, 1}},
		},
		{
			name:       "multiple solutions",
			candidates: []int{2, 3, 7},
			target:     9,
			want:       [][]int{{2, 7}, {2, 2, 2, 3}, {3, 3, 3}},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := combinationSum(tt.candidates, tt.target)
			sortCombinations(got)
			sortCombinations(tt.want)
			if len(got) != len(tt.want) {
				t.Fatalf("combinationSum(%v, %d) returned %d results, want %d\ngot:  %v\nwant: %v",
					tt.candidates, tt.target, len(got), len(tt.want), got, tt.want)
			}
			if !equalSubsets(got, tt.want) {
				t.Errorf("combinationSum(%v, %d) = %v, want %v",
					tt.candidates, tt.target, got, tt.want)
			}
		})
	}
}
