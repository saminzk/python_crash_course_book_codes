import time

start_time = time.time()

counts = [value for value in range(1,1000001)]
print(min(counts))
print(max(counts))
print(sum(counts))

end_time = time.time()

print(f"execution time {end_time - start_time} seconds")