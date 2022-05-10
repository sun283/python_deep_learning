# Lattice paths
# Problem 15
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 
# there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?

def lattice_paths(m, n):
    cache = [1]
    larger = max(m, n)
    smaller = min(m, n)
    while(len(cache) < larger + 1):
        for i in range(1, len(cache)):
            cache[i] += cache[i - 1]
        cache.append(2 * cache[len(cache) - 1])
    return cache[smaller]

print(lattice_paths(2, 2))
