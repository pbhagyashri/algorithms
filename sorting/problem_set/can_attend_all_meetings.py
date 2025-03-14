def can_attend_all_meetings(intervals):
    intervals.sort(key=lambda x: x[0])

    current_end_time = 0
    for m in intervals:
        if m[0] < current_end_time:
            return 0
        current_end_time = m[1]
        
    return 1

intervals = [
[13, 56],
[1, 3],
[4, 5],
[9990, 10341],
[8, 10],
[67, 9990]
]

print(can_attend_all_meetings(intervals))
