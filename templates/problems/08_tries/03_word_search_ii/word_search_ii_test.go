package word_search_ii

import (
	"sort"
	"testing"
)

func TestFindWords(t *testing.T) {
	tests := []struct {
		name  string
		board [][]byte
		words []string
		want  []string
	}{
		{
			name: "example 1",
			board: [][]byte{
				{'o', 'a', 'a', 'n'},
				{'e', 't', 'a', 'e'},
				{'i', 'h', 'k', 'r'},
				{'i', 'f', 'l', 'v'},
			},
			words: []string{"oath", "pea", "eat", "rain"},
			want:  []string{"eat", "oath"},
		},
		{
			name:  "example 2",
			board: [][]byte{{'a', 'b'}, {'c', 'd'}},
			words: []string{"abcb"},
			want:  []string{},
		},
		{
			name:  "single cell match",
			board: [][]byte{{'a'}},
			words: []string{"a"},
			want:  []string{"a"},
		},
		{
			name:  "single cell no match",
			board: [][]byte{{'a'}},
			words: []string{"b"},
			want:  []string{},
		},
		{
			name: "multiple found",
			board: [][]byte{
				{'a', 'b'},
				{'c', 'd'},
			},
			words: []string{"ab", "ac", "abdc", "abcd", "dcba"},
			want:  []string{"ab", "abdc", "ac"},
		},
		{
			name:  "no words",
			board: [][]byte{{'a', 'b'}, {'c', 'd'}},
			words: []string{},
			want:  []string{},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := findWords(tt.board, tt.words)
			if got == nil {
				got = []string{}
			}
			sort.Strings(got)
			sort.Strings(tt.want)
			if len(got) != len(tt.want) {
				t.Errorf("findWords() returned %d results, want %d: got %v, want %v", len(got), len(tt.want), got, tt.want)
				return
			}
			for i := range got {
				if got[i] != tt.want[i] {
					t.Errorf("findWords() = %v, want %v", got, tt.want)
					return
				}
			}
		})
	}
}
