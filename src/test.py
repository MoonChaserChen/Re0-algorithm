from typing import List
def minimum_length_encoding(self, words: List[str]) -> int:
    sorted(words)
    words.sort(key=lambda x: x[::-1])
    return sum(len(v) + 1 for i, v in enumerate(words) if i == len(words) - 1 or not words[i + 1].endswith(v))

def fun(words: List[str]) -> None:
    words.sort()

arr = [1, 9, 4, 7]
arr.sort()
print(arr)