# Module 7 – DA Introduction to Python
# Assignment solutions
# Questions 4–6, 9–16, 18–24, 26–42, 44–64, 66–70, 72–82, 90

# Q4 Positive, negative or zero
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Q5 Factorial
num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial =", fact)

# Q6 Fibonacci series
n = int(input("Enter range: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()

# Q9 Swap with temp and without temp
a, b = 10, 20
temp = a
a = b
b = temp
print(a, b)

a, b = 10, 20
a, b = b, a
print(a, b)

# Q10 Even or odd
num = int(input("Enter a number: "))
print("Even" if num % 2 == 0 else "Odd")

# Q11 Vowel
letter = input("Enter a letter: ").lower()
print("Vowel" if letter in "aeiou" else "Not a vowel")

# Q12 Sum of three integers; if any two are equal, return zero
a, b, c = 1, 2, 3
result = 0 if a == b or b == c or a == c else a + b + c
print(result)

# Q13 Equal, or sum/difference is 5
a, b = 3, 8
print(a == b or a + b == 5 or abs(a - b) == 5)

# Q14 Sum of first n positive integers
n = int(input("Enter n: "))
print(sum(range(1, n + 1)))

# Q15 Length of a string
s = input("Enter a string: ")
print(len(s))

# Q16 Character frequency
s = input("Enter a string: ")
frequency = {}
for ch in s:
    frequency[ch] = frequency.get(ch, 0) + 1
print(frequency)

# Q18 Count substring occurrences
s = "hello hello world"
sub = "hello"
print(s.count(sub))

# Q19 Count occurrences of each word
sentence = "this is a test this is python"
words = sentence.split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)

# Q20 Swap first two characters of two strings
a, b = "abc", "xyz"
new_a = b[:2] + a[2:]
new_b = a[:2] + b[2:]
print(new_a + " " + new_b)

# Q21 Add 'in', or 'ly' if already ends with 'ing'
s = input("Enter a string: ")
if len(s) < 3:
    result = s
elif s.endswith("ing"):
    result = s + "ly"
else:
    result = s + "in"
print(result)

# Q22 Reverse if length is a multiple of 4
def reverse_if_multiple_of_4(s):
    return s[::-1] if len(s) % 4 == 0 else s
print(reverse_if_multiple_of_4("abcd"))

# Q23 First 2 and last 2 characters
def first_last_two(s):
    return s[:2] + s[-2:] if len(s) >= 2 else ""
print(first_last_two("w3resource"))

# Q24 Insert a string in the middle
def insert_middle(original, insert):
    middle = len(original) // 2
    return original[:middle] + insert + original[middle:]
print(insert_middle("abcd", "XY"))

# Q26 Remove last object from a list
items = [1, 2, 3, 4]
items.pop()
print(items)

# Q27 list1[-1]
list1 = [2, 33, 222, 14, 25]
print(list1[-1])  # 25

# Q29 Largest, smallest and sum
def list_stats(values):
    return max(values), min(values), sum(values)
print(list_stats([4, 8, 1, 6]))

# Q30 Compare two lists
list_a = [1, 2, 3]
list_b = [1, 2, 3]
print(list_a == list_b)

# Q31 Count strings length >=2 with same first/last character
values = ["abc", "xyz", "aba", "1221", "a"]
count = sum(len(x) >= 2 and x[0] == x[-1] for x in values)
print(count)

# Q32 Remove duplicates
values = [1, 2, 2, 3, 1, 4]
unique = list(dict.fromkeys(values))
print(unique)

# Q33 Check empty list
values = []
print("Empty" if not values else "Not empty")

# Q34 Common member
def has_common(a, b):
    return bool(set(a) & set(b))
print(has_common([1, 2], [3, 2]))

# Q35 First and last 5 squares from 1 to 30
squares = [i * i for i in range(1, 31)]
print(squares[:5] + squares[-5:])

# Q36 Unique elements in a new list
def unique_list(values):
    return list(dict.fromkeys(values))
print(unique_list([1, 2, 2, 3, 3, 4]))

# Q37 Characters to string
chars = ['P', 'y', 't', 'h', 'o', 'n']
print("".join(chars))

# Q38 Random item from a list
import random
items = [10, 20, 30, 40]
print(random.choice(items))

# Q39 Second smallest number
values = [5, 1, 8, 2, 2, 9]
print(sorted(set(values))[1])

# Q40 Unique values
values = [1, 2, 2, 3, 1, 4]
print(set(values))

# Q41 Check whether a list contains a sub-list
def contains_sublist(main, sub):
    n = len(sub)
    return any(main[i:i+n] == sub for i in range(len(main) - n + 1))
print(contains_sublist([1, 2, 3, 4], [2, 3]))

# Q42 Split a list into variables
values = [10, 20, 30]
a, b, c = values
print(a, b, c)

# Q44 Tuple with different data types
mixed = (10, "Python", 3.14, True)
print(mixed)

# Q45 Unzip list of tuples
pairs = [(1, "a"), (2, "b"), (3, "c")]
numbers, letters = zip(*pairs)
print(list(numbers), list(letters))

# Q46 List of tuples to dictionary
pairs = [("a", 1), ("b", 2)]
print(dict(pairs))

# Q47 Create dictionary using tuples
keys = ("name", "age")
values = ("Alex", 20)
print(dict(zip(keys, values)))

# Q48 Sort dictionary ascending and descending by value
d = {"a": 3, "b": 1, "c": 2}
print(dict(sorted(d.items(), key=lambda x: x[1])))
print(dict(sorted(d.items(), key=lambda x: x[1], reverse=True)))

# Q49 Concatenate dictionaries
d1 = {"a": 1}
d2 = {"b": 2}
d3 = {"c": 3}
combined = {**d1, **d2, **d3}
print(combined)

# Q50 Check if key exists
d = {"name": "Alex", "age": 20}
key = "name"
print(key in d)

# Q51 Traverse dictionary
for key, value in d.items():
    print(key, value)

# Q52 Check presence of a key
print("age" in d)

# Q53 Dictionary with keys 1 to 15
d = {i: i*i for i in range(1, 16)}
print(d)

# Q54 Check multiple keys
required = ["name", "age"]
print(all(key in d for key in required))  # False for this d

# Q55 Merge two dictionaries
a = {"x": 1}
b = {"y": 2}
merged = a.copy()
merged.update(b)
print(merged)

# Q56 Map two lists into a dictionary
keys = ["a", "b", "c"]
values = [400, 400, 300]
print(dict(zip(keys, values)))

# Q57 Highest 3 values in a dictionary
d = {"a": 10, "b": 50, "c": 30, "d": 40}
print(sorted(d.items(), key=lambda x: x[1], reverse=True)[:3])

# Q58 Combine values in list of dictionaries
from collections import Counter
data = [
    {"item": "item1", "amount": 400},
    {"item": "item2", "amount": 300},
    {"item": "item1", "amount": 750},
]
print(Counter({item: sum(x["amount"] for x in data if x["item"] == item)
               for item in {x["item"] for x in data}}))

# Q59-60 Dictionary from a string / character count
s = "w3resource"
print(dict(Counter(s)))

# Q61 Factorial function
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print(factorial(5))

# Q62 Check number in range
def in_range(n, start, end):
    return start <= n <= end
print(in_range(5, 1, 10))

# Q63 Perfect number
def is_perfect(n):
    if n < 2:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n
print(is_perfect(6))

# Q64 Palindrome
def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome("madam"))

# Q66 Random item from list/tuple
print(random.choice([1, 2, 3, 4]))

# Q67 Random item from range
print(random.choice(range(1, 11)))

# Q68 Random number
print(random.random())

# Q69 Set starting value (seed)
random.seed(10)
print(random.random())

# Q70 Randomize list in place
values = [1, 2, 3, 4, 5]
random.shuffle(values)
print(values)

# Q72 Read entire text file
# with open("sample.txt", "r") as f:
#     print(f.read())

# Q73 Append text and display
# with open("sample.txt", "a") as f:
#     f.write("\nNew text")
# with open("sample.txt", "r") as f:
#     print(f.read())

# Q74 Read first n lines
# n = 3
# with open("sample.txt", "r") as f:
#     for _ in range(n):
#         print(f.readline(), end="")

# Q75 Read last n lines
# from collections import deque
# n = 3
# with open("sample.txt", "r") as f:
#     print("".join(deque(f, maxlen=n)))

# Q76 Read line by line into a list
# with open("sample.txt", "r") as f:
#     lines = f.readlines()
# print(lines)

# Q77 Read line by line into a variable
# with open("sample.txt", "r") as f:
#     text = ""
#     for line in f:
#         text += line
# print(text)

# Q78 Find longest words
# with open("sample.txt", "r") as f:
#     words = f.read().split()
# longest = max(words, key=len)
# print(longest)

# Q79 Count lines
# with open("sample.txt", "r") as f:
#     print(sum(1 for _ in f))

# Q80 Frequency of words in a file
# with open("sample.txt", "r") as f:
#     words = f.read().split()
# print(Counter(words))

# Q81 Write a list to a file
# values = ["Python", "SQL", "Excel"]
# with open("output.txt", "w") as f:
#     f.write("\n".join(values))

# Q82 Copy contents to another file
# with open("sample.txt", "r") as source, open("copy.txt", "w") as target:
#     target.write(source.read())

# Q90 Accept only odd numbers, otherwise raise exception
num = int(input("Enter an odd number: "))
if num % 2 == 0:
    raise ValueError("Only odd numbers are allowed.")
print("Accepted:", num)
