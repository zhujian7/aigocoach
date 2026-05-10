from typing import List
from collections import deque


def ladder_length(begin_word: str, end_word: str, word_list: List[str]) -> int:
    word_set = set(word_list)
    if end_word not in word_set:
        return 0
    if begin_word == end_word:
        return 0

    queue = deque([begin_word])
    visited = {begin_word}
    length = 1

    while queue:
        size = len(queue)
        for _ in range(size):
            word = queue.popleft()
            chars = list(word)
            for j in range(len(chars)):
                original = chars[j]
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c == original:
                        continue
                    chars[j] = c
                    nxt = ''.join(chars)
                    if nxt == end_word:
                        return length + 1
                    if nxt in word_set and nxt not in visited:
                        visited.add(nxt)
                        queue.append(nxt)
                chars[j] = original
        length += 1

    return 0
