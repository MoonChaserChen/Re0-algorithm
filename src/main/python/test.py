def letter_combinations(digits):
    m = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno",
         "7": "pqrs", "8": "tuv", "9": "wxyz"}
    result, curr_result = [], []
    if not digits:
        return []

    def back_tracing(curr_idx=0):
        for candidate in m.get(digits[curr_idx]):
            curr_result.append(candidate)
            if curr_idx == len(digits) - 1:
                result.append("".join(curr_result))
            else:
                back_tracing(curr_idx + 1)
            curr_result.pop()

    back_tracing()
    return result


print(letter_combinations("23"))
print(letter_combinations("2"))
