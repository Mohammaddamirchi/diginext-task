def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    
    merged = []
    current_interval = intervals[0]

    for interval in intervals[1:]:
        if interval[0] <= current_interval[1]:
            current_interval = (current_interval[0], max(current_interval[1], interval[1]))
        else:
            merged.append(current_interval)
            current_interval = interval
    merged.append(current_interval)
    
    return merged

# مثال : 
input_intervals = [(1, 3), (2, 6), (8, 10)]
output = merge_intervals(input_intervals)

print(output)
