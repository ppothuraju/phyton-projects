'''
Selected functions from the math module

Let's start with a quick preview of some of the functions provided by the math module.

We've chosen them arbitrarily, but that doesn't mean that the functions we haven't mentioned here are any less significant. Dive into the modules' depths yourself - we don't have the space or the time to talk about everything in detail here.

The first group of the math's functions are connected with trigonometry:

    sin(x) → the sine of x;
    cos(x) → the cosine of x;
    tan(x) → the tangent of x.

All these functions take one argument (an angle measurement expressed in radians) and return the appropriate result (be careful with tan() - not all arguments are accepted).

Of course, there are also their inversed versions:

    asin(x) → the arcsine of x;
    acos(x) → the arccosine of x;
    atan(x) → the arctangent of x.

These functions take one argument (mind the domains) and return a measure of an angle in radians.

To effectively operate on angle measurements, the math module provides you with the following entities:

    pi → a constant with a value that is an approximation of π;
    radians(x) → a function that converts x from degrees to radians;
    degrees(x) → acting in the other direction (from radians to degrees)

Now look at the code in the editor. The example program isn't very sophisticated, but can you predict its results?

Apart from the circular functions (listed above) the math module also contains a set of their hyperbolic analogues:

    sinh(x) → the hyperbolic sine;
    cosh(x) → the hyperbolic cosine;
    tanh(x) → the hyperbolic tangent;
    asinh(x) → the hyperbolic arcsine;
    acosh(x) → the hyperbolic arccosine;
    atanh(x) → the hyperbolic arctangent.


Another group of the math's functions is formed by functions which are connected with exponentiation:

    e → a constant with a value that is an approximation of Euler's number (e)
    exp(x) → finding the value of ex;
    log(x) → the natural logarithm of x
    log(x, b) → the logarithm of x to base b
    log10(x) → the decimal logarithm of x (more precise than log(x, 10))
    log2(x) → the binary logarithm of x (more precise than log(x, 2))

Note: the pow() function:

    pow(x, y) → finding the value of xy (mind the domains)

'''

from math import pi, radians, degrees, sin, cos, tan, asin, e, exp, log

ad = 90
ar = radians(ad)
ad = degrees(ar)

print(ad == 90.)
print(ar == pi / 2.)
print(sin(ar) / cos(ar) == tan(ar))
print(asin(sin(ar)) == ar)



print(pow(e, 1) == exp(log(e)))
print(pow(2, 2) == exp(2 * log(2)))
print(log(e, e) == exp(0))