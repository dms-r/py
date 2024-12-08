print("Hello World")

# This is comment

# This is var
pi: float = 22/7
# Print var
print(f"Nilai pi = {pi}")


# Import lib
from typing import Final

# Var const, style upper case
PI: Final[float] = 22/7
# Print var
print(f"Nilai pi = {PI}")


# Null type data
custom: str = None
# Print var
print(f"Value coutom = {custom}")
# Add some value
custom = "huh"
print(f"Value coutom = {custom}")


# Null type data for number
custom: int = 0
# Print var
print(f"Value coutom = {custom}")
# Add some value
custom += 22/7
print(f"Value coutom = {custom}")

for i in range(5):
    if i % 2 == 0:
        i += 1
        pass
    else:
        print(f"Ganjil: {i}")
        i += 1


# Type data list
true_number = [0, 1, 2]
for i in true_number:
    print(f"True number: {true_number[i]}")

# Type data tuple, cann'r changes
date = tuple(range(30))
for i in date:
    if i % 7  == 0:
        print(f"date: {date[i]}")
    else:
        pass

# Type data dictionary
profile = {
    "name": "dimas",
    "umur": 19,
    "hobby": ["run", "swimming"]
}
print("The name author: %s" % (profile["name"]))
for i in profile:
    if i == "hobby":
        for j in "hobby"
        print("profile: %s" % profile[]")
