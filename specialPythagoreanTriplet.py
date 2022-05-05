# Special Pythagorean triplet
# Problem 9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# square of a + square of b equals square of c
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

for c in range(2, 1000):
    for a in range(1, c):
        # Ensure a + b + c == 1000.
        # Since a is counting up, the first
        # answer we find should have a <= b.
        b = 1000 - c - a
        # Ensure Pythagorean triple
        if b > 0 and a**2 + b**2 == c**2:
            print("a = %d, b = %d, c = %d.  abc = %d" % (a, b, c, a * b * c))
