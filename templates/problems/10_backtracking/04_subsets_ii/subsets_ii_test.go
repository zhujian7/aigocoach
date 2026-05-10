package subsets_ii

import (
	"testing"
)

func TestSubsetsWithDup(t *testing.T) {
	tests := []struct {
		name string
		nums []int
		want [][]int
	}{
		{
			name: "example with duplicates",
			nums: []int{1, 2, 2},
			want: [][]int{{}, {1}, {2}, {1, 2}, {2, 2}, {1, 2, 2}},
		},
		{
			name: "single element",
			nums: []int{0},
			want: [][]int{{}, {0}},
		},
		{
			name: "all duplicates",
			nums: []int{1, 1, 1},
			want: [][]int{{}, {1}, {1, 1}, {1, 1, 1}},
		},
		{
			name: "no duplicates",
			nums: []int{1, 2, 3},
			want: [][]int{{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}},
		},
		{
			name: "two pairs of duplicates",
			nums: []int{1, 1, 2, 2},
			want: [][]int{
				{}, {1}, {2}, {1, 1}, {1, 2}, {2, 2},
				{1, 1, 2}, {1, 2, 2}, {1, 1, 2, 2},
			},
		},
		{
			name: "unsorted input with duplicates",
			nums: []int{2, 1, 2},
			want: [][]int{{}, {1}, {2}, {1, 2}, {2, 2}, {1, 2, 2}},
		},
		{
			name: "empty input",
			nums: []int{},
			want: [][]int{{}},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := subsetsWithDup(tt.nums)
			sortSubsets(got)
			sortSubsets(tt.want)
			if !equalSubsets(got, tt.want) {
				t.Errorf("subsetsWithDup(%v) = %v, want %v", tt.nums, got, tt.want)
			}
		})
	}
}
