'''
Selected functions from the platform module

The platform module lets you access the underlying platform's data, i.e., hardware, operating system, and interpreter version information.

There is a function that can show you all the underlying layers in one glance, named platform, too. It just returns a string describing the environment; thus, its output is rather addressed to humans than to automated processing (you'll see it soon).

This is how you can invoke it: platform(aliased = False, terse = False)

And now:

    aliased → when set to True (or any non-zero value) it may cause the function to present the alternative underlying layer names instead of the common ones;
    terse → when set to True (or any non-zero value) it may convince the function to present a briefer form of the result (if possible)

'''
from platform import platform, machine, processor,system,version,python_implementation, python_version_tuple

print(platform())
print(platform(1))
print(platform(0, 1))
print(machine())
print(processor())
print(system())
print(version())

print(python_implementation())

for atr in python_version_tuple():
    print(atr)