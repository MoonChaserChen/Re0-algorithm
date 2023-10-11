def top_students(positive_feedback, negative_feedback, report, student_id, k):
    words = {}
    for w in positive_feedback:
        words[w] = 3
    for w in negative_feedback:
        words[w] = -1
    arr = []
    for s, i in zip(report, student_id):
        score = sum(words.get(w, 0) for w in s.split())
        arr.append([-score, i])
    arr.sort()
    return [i for v, i in arr[:k]]
