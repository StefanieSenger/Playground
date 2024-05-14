""" mutable objects as default arguments will keep their state even after the function
has finished """

def append_to(element, to=[]):
    to.append(element)
    return to

print(append_to(12)) # [12]
print(append_to(22)) # [12, 22]

""" Python default arguments (the list `to`) are evaluated (created) once when the
function is defined and the same list is used in each successive call. If we mutate it,
the mutated argument will be used in later calls. """

""" If we want to avoid this, we should use a non-mutable default line None and test for
if to has already been made into a list: """

def append_to(element, to=None):
    if to is None:
        to = []
    to.append(element)
    return to

print(append_to(12)) # [12]
print(append_to(22)) # [22]

""" Or, we can also use this fact for our own good and utilise it like a cache: """

def expensive_function(x, y, cache={}):
    args = (x, y)
    if args in cache:
        return cache[args]
    # otherwise this is the first time with these arguments: do the expensive calculation
    result = expensive_calc(x, y)
    cache[args] = result
    return result