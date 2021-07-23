import time
current_time = time.time()
print(current_time)


def speed_calc_decorator(function):
    def wrapper_function():
        start_time = time.time()
        function()
        end_time = time.time()
        print(f"{function.__name__} run speed: {end_time - start_time}s")
    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()


# Create the logging_decorator() function 👇

# def logging_decorator(function):
#   def wrapper(*args, **kwargs):
#     print(f"You called {function.__name__}{args}")
#     result = function(args[0],args[1],args[2])
#     print(f"It returned {result} ")
#   return wrapper


# # Use the decorator 👇

# @logging_decorator
# def sample(a, b, c):
#   return a + b + c

# sample(10, 20, 30)
