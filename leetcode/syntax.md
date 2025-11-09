# Python Syntax

```python
# to make a hashmap you just do:

hash = {}


```

## Stacks: deque

deque stands for double ended queue

```python
from collections import deque # reccomended use of stacks

dq = deque()
dq = deque([1, 2, 3])

dq.append(4)  # [1, 2, 3, 4]

dq.appendleft(0)  # [0, 1, 2, 3, 4]

dq.pop()  # returns 4, deque becomes [0, 1, 2, 3]

dq.popleft()  # returns 0, deque becomes [1, 2, 3]


# peek at ends without popping.

dq[0]      # front element → 1
dq[-1]     # back element → 3

```

## HashSet

```python

# Creating sets
empty_set = set()
my_set = {1, 2, 3, 4}
from_list = set([1, 2, 3, 3, 4])  # Duplicates removed: {1, 2, 3, 4}

# Adding elements
my_set.add(5)          # Add single element
my_set.update([6, 7])  # Add multiple elements

# Removing elements
my_set.remove(5)       # Raises KeyError if not found
my_set.discard(5)      # No error if not found
popped = my_set.pop()  # Remove and return arbitrary element

# Checking membership
if 3 in my_set:
    print("3 is in the set")

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union = set1 | set2           # {1, 2, 3, 4, 5}
intersection = set1 & set2    # {3}
difference = set1 - set2      # {1, 2}
symmetric_diff = set1 ^ set2  # {1, 2, 4, 5}

# Length and iteration
print(len(my_set))
for item in my_set:
    print(item)

# Converting back to list
my_list = list(my_set)

# Common use cases in coding problems
seen = set()
duplicates = set()

for num in [1, 2, 2, 3, 3, 4]:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)
```
