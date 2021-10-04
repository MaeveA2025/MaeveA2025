# Create a function that accepts 3 integer values a,b,c
# The function itself should return True if a triangle can
# be built with the sides of a given length and False
# In any other case. (All triangles must have surface greater than 0 to be accepted)

def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

# solved using the triangle inequality theorem


