def sum_range(start, end):
    if start > end:
        end, start = start, end
    return sum(range(start, end + 1))

print(sum_range(34, 12))
print(sum_range(-4, 4))
