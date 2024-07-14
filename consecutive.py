def longestconsecutive(nums):
    num_set = set(nums)
    longest_streak = 0
    best_sequence = []

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1
            current_sequence = [num]

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
                current_sequence.append(current_num)

            if current_streak > longest_streak:
                longest_streak = current_streak
                best_sequence = current_sequence
    return longest_streak, best_sequence

# مثال : 
input_nums = [100, 4, 200, 1, 3, 2]
length, sequence = longestconsecutive(input_nums)

print(f"sequence length:{length}, sequential sequence: {sequence})")
