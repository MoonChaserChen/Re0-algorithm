def minimum_length_encoding(words: [str]) -> int:
    s = set(words)
    for x in words:
        for k in range(1, len(words)):
            s.discard(x[k:])
    return sum(len(x) + 1 for x in s)
