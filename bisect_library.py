import bisect

def get_grade(score, cutoffs=[60, 70, 80, 90], grades="FDCBA"):
    i = bisect.bisect_right(cutoffs, score)
    return grades[i]

grades = [get_grade(score) for score in [52, 99, 77, 70, 89, 90, 100]]
print(grades)