# Module 7 – Theory Answers + Viva Notes

## Q1. Types of Applications
Common application types include desktop applications, web applications, mobile applications, database applications and enterprise applications.

**Viva:** An application is software designed to perform a specific user task.

## Q2. What is programming?
Programming is the process of writing instructions in a programming language so a computer can perform tasks.

**Viva:** A program is a set of instructions executed by a computer.

## Q3. What is Python?
Python is a high-level, interpreted, general-purpose programming language known for readable syntax and a large standard library.

**Viva:** Python is commonly used in data analysis, automation, web development, AI and machine learning.

## Q7. How is memory managed in Python?
Python manages memory automatically. Objects are stored in a private memory area and Python uses mechanisms such as reference counting and garbage collection to reclaim unused memory.

**Viva:** `del` removes a reference; it does not necessarily immediately destroy an object.

## Q8. Purpose of continue statement
`continue` skips the remaining statements in the current loop iteration and moves to the next iteration.

Example:
```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

## Q17. Negative indexes
Negative indexing accesses elements from the end of a sequence. `-1` means the last element, `-2` the second-last, and so on.

## Q25. What is a List? How do you reverse it?
A list is an ordered, mutable collection. It can be reversed with `list.reverse()` or `list[::-1]`.

## Q28. append() vs extend()
`append()` adds one object as a single element. `extend()` adds each element from an iterable.

```python
a = [1, 2]
a.append([3, 4])   # [1, 2, [3, 4]]

b = [1, 2]
b.extend([3, 4])   # [1, 2, 3, 4]
```

## Q43. Tuple and list vs tuple
A tuple is an ordered collection that is immutable.

| List | Tuple |
|---|---|
| Mutable | Immutable |
| Uses `[]` | Uses `()` |
| Can be changed | Cannot be changed after creation |

## Q65. Basic types of functions
Python functions can be classified as built-in functions and user-defined functions. Functions may also be anonymous (`lambda`) or recursive depending on how they are written/used.

## Q71. File function and keywords
Python uses `open()` to open files.

Common modes:
- `r` – read
- `w` – write
- `a` – append
- `x` – create

Example:
```python
with open("sample.txt", "r") as f:
    data = f.read()
```

## Q83. Exception handling and Error
Exception handling lets a program handle runtime problems without abruptly terminating. Python commonly uses `try`, `except`, `else` and `finally`.

An error is a problem in a program. Some runtime problems are represented as exceptions, such as `ValueError` or `ZeroDivisionError`.

## Q84. except statements and built-in exceptions
A `try` block can have multiple `except` clauses for different exception types.

Examples:
- `ValueError`
- `TypeError`
- `ZeroDivisionError`
- `FileNotFoundError`
- `IndexError`
- `KeyError`

## Q85. When does else execute?
The `else` block executes when the `try` block completes without raising an exception.

## Q86. Can one except handle multiple exceptions?
Yes.

```python
try:
    ...
except (ValueError, TypeError):
    ...
```

## Q87. When is finally executed?
`finally` normally executes whether an exception occurs or not, making it useful for cleanup such as closing resources.

## Q88. What happens when 1 == 1 is executed?
The expression compares the integer `1` with the integer `1`, so it evaluates to `True`.

## Q89. try/except/finally
```python
try:
    x = int(input("Enter a number: "))
    print(10 / x)
except ValueError:
    print("Enter a valid integer.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("Program finished.")
```

**How it works:** `try` contains risky code, `except` handles specific exceptions, and `finally` performs code that should run at the end.

## Q90. Only odd numbers
The program checks `num % 2`. If the remainder is `0`, the number is even and a `ValueError` is raised; otherwise the number is accepted.

### Quick viva cheat sheet
- `if/elif/else` → decision making
- `for` → repeated iteration over a sequence/range
- `%` → remainder/modulus
- `len()` → number of items/characters
- `split()` → breaks a string into a list
- `join()` → combines strings
- `dict` → key-value collection
- `set` → collection of unique values
- `def` → defines a function
- `return` → sends a value back from a function
- `import` → loads a module
- `with open()` → safely works with files and closes them automatically
- `try/except` → handles exceptions
