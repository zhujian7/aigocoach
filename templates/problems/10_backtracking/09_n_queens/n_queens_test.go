package n_queens

import (
	"sort"
	"testing"
)

func TestSolveNQueens(t *testing.T) {
	tests := []struct {
		name      string
		n         int
		wantCount int
		wantBoards [][]string // nil means only check count
	}{
		{
			name:      "n=1",
			n:         1,
			wantCount: 1,
			wantBoards: [][]string{{"Q"}},
		},
		{
			name:      "n=2 no solution",
			n:         2,
			wantCount: 0,
			wantBoards: [][]string{},
		},
		{
			name:      "n=3 no solution",
			n:         3,
			wantCount: 0,
			wantBoards: [][]string{},
		},
		{
			name:      "n=4",
			n:         4,
			wantCount: 2,
			wantBoards: [][]string{
				{".Q..", "...Q", "Q...", "..Q."},
				{"..Q.", "Q...", "...Q", ".Q.."},
			},
		},
		{
			name:      "n=5",
			n:         5,
			wantCount: 10,
		},
		{
			name:      "n=6",
			n:         6,
			wantCount: 4,
		},
		{
			name:      "n=8",
			n:         8,
			wantCount: 92,
		},
	}

	sortBoards := func(boards [][]string) {
		sort.Slice(boards, func(i, j int) bool {
			for k := 0; k < len(boards[i]); k++ {
				if boards[i][k] != boards[j][k] {
					return boards[i][k] < boards[j][k]
				}
			}
			return false
		})
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := solveNQueens(tt.n)
			if len(got) != tt.wantCount {
				t.Fatalf("solveNQueens(%d) returned %d solutions, want %d", tt.n, len(got), tt.wantCount)
			}
			if tt.wantBoards != nil {
				sortBoards(got)
				sortBoards(tt.wantBoards)
				if !equalStringSlices(got, tt.wantBoards) {
					t.Errorf("solveNQueens(%d) = %v, want %v", tt.n, got, tt.wantBoards)
				}
			}
		})
	}
}
