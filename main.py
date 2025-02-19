import multiprocessing as mp
import time

# Function to compute sum of squares for a range
def sum_of_squares(start, end):
    return sum(x * x for x in range(start, end))

if __name__ == "__main__":
    N = 10**7  # Large dataset

    # **Single-threaded computation**
    start = time.time()
    total = sum_of_squares(1, N + 1)  # +1 to include N
    end = time.time()
    print(f"Single-threaded result: {total}")
    print(f"Single-threaded runtime: {end - start:.6f} seconds\n")

    # **Parallel computation using multiprocessing**
    num_workers = mp.cpu_count()  # Use all available CPU cores
    pool = mp.Pool(processes=num_workers)

    chunk_size = N // num_workers
    ranges = [(i * chunk_size + 1, (i + 1) * chunk_size + 1) for i in range(num_workers)]
    ranges[-1] = (ranges[-1][0], N + 1)  # Adjust the last range to include N

    start = time.time()
    results = pool.starmap(sum_of_squares, ranges)
    total_parallel = sum(results)
    end = time.time()

    pool.close()
    pool.join()

    print(f"Parallel result: {total_parallel}")
    print(f"Parallel runtime: {end - start:.6f} seconds")
