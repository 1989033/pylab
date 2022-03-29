def sum_for_loop(N):
    count = 0
    for n in range(1, N+1):
        count += n
    return count
print(sum_for_loop(100))
print(sum_for_loop(1000))
