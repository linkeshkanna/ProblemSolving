'''
Study the math library in Python:
Give an Example for each functions in https://docs.python.org/3/library/math.html
'''
import math
# Round a number upward to its nearest integer
print(math.ceil(1.4))
print(math.ceil(5.3))
print(math.ceil(-5.3))
print(math.ceil(22.6))

# method returns the number of ways picking k unordered outcomes from n possibilities
#print (math.comb(n, k))
print (math.comb(7, 5))

#Return the first value, with the sign of the second value
print(math.copysign(4, -1))
print(math.copysign(-8, 97.21))
print(math.copysign(-43, -76))

#Remove - sign of given number
print(math.fabs(-66.43))
print(math.fabs(-7))

#Return factorial of a number
print(math.factorial(9))
print(math.factorial(6))
print(math.factorial(12))

# Round a number downward to its nearest integer
print(math.floor(1.4))
print(math.floor(5.3))
print(math.floor(-5.3))
print(math.floor(22.6))

# Return the remainder after modulo operation
print (math.fmod(67, 7))
print (math.fmod(17, 4))
print (math.fmod(16, 4))

#Return mantissa and exponent of a given number
print(math.frexp(4))
print(math.frexp(7.9))

# Print the sum of all items
print(math.fsum((1, 2, 3, 4, 5)))

#find the highest number that can divide two numbers
print (math.gcd(26, 12))
print (math.gcd(12, 6))
print (math.gcd(10, 0))
print (math.gcd(0, 34))
print (math.gcd(0, 0))

#compare the closeness of two values
print(math.isclose(1.233, 1.4566))
print(math.isclose(1.233, 1.233))
print(math.isclose(1.233, 1.233000001))

# Check whether some values are finite
print (math.isfinite (56))
print (math.isfinite (-45.34))
print (math.isfinite (+45.34))
print (math.isfinite (float("nan")))
print (math.isfinite (float("inf")))
print (math.isfinite (float("-inf")))
print (math.isfinite (-math.inf))

# Check whether some values are infinite
print (math.isinf (56))
print (math.isinf (-45.34))
print (math.isinf (+45.34))
print (math.isinf (math.inf))
print (math.isinf (float("nan")))
print (math.isinf (float("inf")))
print (math.isinf (float("-inf")))
print (math.isinf (-math.inf))

# Check whether some values are NaN or not
print (math.isnan (56))
print (math.isnan (-45.34))
print (math.isnan (+45.34))
print (math.isnan (math.inf))
print (math.isnan (float("nan")))
print (math.isnan (float("inf")))
print (math.isnan (float("-inf")))
print (math.isnan (math.nan))
print (math.isnan (float("NaN")))

# Examples to print the square root of different numbers
print (math.sqrt(10))
print (math.sqrt (12))
print (math.sqrt (68))
print (math.sqrt (100))

# Round square root numbers downward to the nearest integer
print (math.isqrt(10))
print (math.isqrt (12))
print (math.isqrt (68))
print (math.isqrt (100))

#Returns x * (2**i). This is also called as inverse of Python frexp()
print (math.ldexp(4,3))

#Return the fractional and integer parts of x
print (math.modf(100.12))

# Print the number of ways to choose k items from n items
#print (math.perm(n, k))
print (math.perm(7, 5))

#Returns the product of an iterable (lists, array, tuples, etc.)
print(math.prod((1, 2, 3, 4, 5)))

# Find the value n that makes x completely divisible by y
print (math.remainder(9, 2))
print (math.remainder(17, 4))

# Return the truncated integer parts of different numbers
print(math.trunc(2.77))
print(math.trunc(8.32))
print(math.trunc(-99.29))

#find the exponential of the specified value
print(math.exp(65))
print(math.exp(-6.89))

#Return the exponential ex-1
print(math.expm1(32))
print(math.expm1(-10.89))

# Return the natural logarithm of different numbers
print(math.log(2.7183))
print(math.log(2))
print(math.log(1))

# Return the log(1+number) for different numbers
print(math.log1p(2.7183))
print(math.log1p(2))
print(math.log1p(1))

# Return the base-2 logarithm of different numbers
print(math.log2(2.7183))
print(math.log2(2))
print(math.log2(1))

# Return the base-10 logarithm of different numbers
print(math.log10(2.7183))
print(math.log10(2))
print(math.log10(1))

#Return the value of 9 raised to the power of 3
print(math.pow(9, 3))

# Return the arc cosine value of numbers
print (math.acos(0.55))
print (math.acos(-0.55))
print (math.acos(0))
print (math.acos(1))
print (math.acos(-1))

# Return the arc sine value of numbers
print (math.asin(0.55))
print (math.asin(-0.55))
print (math.asin(0))
print (math.asin(1))
print (math.asin(-1))

#find the arctangent of different numbers
print (math.atan(0.39))
print (math.atan(67))
print (math.atan(-21))

# Return the arc tangent of y/x in radians
print (math.atan2(8, 5))
print (math.atan2(20, 10))
print (math.atan2(34, -7))

# Return the cosine of different numbers
print (math.cos(0.00))
print (math.cos(-1.23))
print (math.cos(10))
print (math.cos(3.14159265359))

## Calculate the distance between point p and q
print (math.dist([3], [1]))

#print the hypotenuse of a right-angled triangle
#print (math.hypot(parendicular, base))
print (math.hypot(10, 5))

# Return the sine of different values
print (math.sin(0.00))
print (math.sin(-1.23))
print (math.sin(10))
print (math.sin(math.pi))
print (math.sin(math.pi/2))

# Return the tangent of different numbers
print (math.tan(90))
print (math.tan(-90))
print (math.tan(45))
print (math.tan(60))

# Convert angles from radians to degrees:
print (math.degrees(8.90))
print (math.degrees(-20))
print (math.degrees(1))
print (math.degrees(90))

# Convert different degrees into radians
print(math.radians(180))
print(math.radians(100.03))
print(math.radians(-20))

# Print the error function of different numbers
print (math.erf(0.67))
print (math.erf(1.34))
print (math.erf(-6))

# Print the complementary error function of different numbers
print (math.erfc(0.67))
print (math.erfc(1.34))
print (math.erfc(-6))

# Return the gamma value of different numbers
print (math.gamma(7))
print (math.gamma(-4.2))

# Return the log gamma value of different numbers
print (math.lgamma(7))
print (math.lgamma(-4.2))

#Constants
print (math.pi)
print (math.e)
print (math.tau)
print (math.inf)
print (-math.inf)
print (math.nan)