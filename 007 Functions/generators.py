# Generators are functions that can pause and resume their execution.
# when a generator function is called, it returns a genertor object, which is an iterator.
# The code inside the function is not executed yet, it is only compiled. The function only executes when you iterate over the generator.
def my_generator():
    yield 1
    yield 2
    yield 3

for value in my_generator():
    print(value)

# Generators allow you to iterate over data without storing the entire dataset in memory
# instead of using "return", generators use the "yield" keyword
# "yield" keyword makes a function a generator.
# When "yield" is encountered, the function's state is saved, and the value is returned. The next time the generator is called, it continues from where it left off.
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for num in count_up_to(10):
    print(num)

# unlike return , which terminates the function, "yeild" pauses it and can be called multiple times.
# Generators are memory-efficient because they generate values on-the fly instead of storing everything in memory
def large_sequence(n):
    for i in range(n):
        yield i
        
gen = large_sequence(1000000)
print()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print()
# you can manually iterate through a generator using "next()" function
# when there are no more values to yield, the generator raise a "StopIteration" exception

# Generator expression : Similar to list comprehensions. you can create generators using generator expressions with parenthess instead of square brackets.
gen_exp = (x*x for x in range(5))
print(gen_exp)
print(list(gen_exp))
print()
# calculate sum of squares without creating a list
total = sum(x*x for x in range(10))
print(total)

# fibonacci sequence generator
def fibonacci():
    a,b = 0,1
    while True:
        yield a
        a, b = b, a+b

gen = fibonacci()
for i in range(30):
    print(next(gen))
    
# generator method : 
# "send()" : allows to send a vlaue to the generator
def print_generator():
    while True:
        received = yield
        print("Received value : ", received)

gen = print_generator()
next(gen) # prime the generator
gen.send("Hello")
gen.send("World")

# "close()" : stops the generator
def my_gen():
    try:
        yield 1
        yield 2
        yield 3
    finally:
        print("Generator closed")

gen = my_gen()
print(next(gen))
gen.close()