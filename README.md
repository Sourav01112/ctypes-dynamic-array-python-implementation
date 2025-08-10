# Dynamic Array Implementation in Python

A custom implementation of a dynamic array (similar to Python lists) using C-style arrays via the `ctypes` library. This project demonstrates low-level memory management concepts and dynamic resizing in Python.

## Description

This implementation creates a dynamic array from scratch without using Python's built-in list type. Instead, it uses `ctypes.py_object` to create C-style arrays that can grow dynamically as elements are added. The array automatically resizes itself when it reaches capacity, doubling in size each time.

## Features

- **Dynamic Resizing**: Automatically doubles capacity when full
- **Basic Operations**: Append, pop, indexing, length calculation
- **Memory Management**: Uses C-style arrays for underlying storage
- **Error Handling**: Index bounds checking with custom error messages
- **Clear Functionality**: Reset array to initial state

## Key Methods

- `append(item)` - Add element to end of array
- `pop()` - Remove and return last element  
- `clear()` - Reset array to empty state
- `len()` - Get current number of elements
- `[index]` - Access element by index
- `str()` - String representation of array

## Usage Example

```python
# Create a new dynamic array
L = mylist()

# Add elements
L.append("Apple")
L.append(True)
L.append(2025)

# Access elements
print(L[0])  # Output: Apple
print(len(L))  # Output: 3

# Remove elements
L.pop()
print(L)  # Output: [Apple,True]

# Clear array
L.clear()
```

## Implementation Details

- Initial capacity: 1 element
- Resize strategy: Double capacity when full
- Uses `ctypes.py_object` for storing Python objects in C-style arrays
- Maintains separate counters for capacity (`size`) and actual elements (`n`)

## Educational Purpose

This implementation is designed to illustrate:
- How dynamic arrays work internally
- Memory allocation and reallocation concepts
- The difference between array capacity and actual size
- Low-level array operations in Python

## Requirements

- Python 3.x
- `ctypes` library (included in Python standard library)
