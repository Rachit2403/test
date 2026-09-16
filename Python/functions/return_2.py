def name_generator(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last
name = name_generator("rachit", "vyas")
print(name)