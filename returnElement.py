# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. 
# For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

# Given this implementation of cons:
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

# Implement car and cdr.
def car(a,b):
    return a

def cdr(a,b):
    return b

print(cons(1,2)(car))
print(cons(1,2)(cdr))