def merge_intervals(intervals:list):
    intervals.sort(key=lambda x: x[0])
    merge_int = intervals[0]
    ans = []
    for start, end in intervals:
        if merge_int[0] <= start and start < merge_int[1]:
            merge_int = [min(start, merge_int[0]), max(end, merge_int[1])]
        else:
            ans.append(merge_int)
            merge_int = [start, end]
    # because the last merged interval hasn't been appended to ans
    ans.append(merge_int)
    return ans

print(merge_intervals([(1,3), (2,6), (8,9), (9,11), (8,10), (2,4), (15,18), (16,17)]))