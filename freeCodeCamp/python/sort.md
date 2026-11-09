# Quick Sort

```python
def quick_sort(list_of_elements):
    if len(list_of_elements) <= 1:
        return list_of_elements

    pivot = list_of_elements[0]

    right = [i for i in list_of_elements if i < pivot]
    mid = [i for i in list_of_elements if i == pivot]
    left = [i for i in list_of_elements if i > pivot]

    return quick_sort(right) + mid + quick_sort(left)

l = []
l_1 = [20, 3, 14, 1, 5]

print(quick_sort(l))
print(quick_sort(l_1))
```

# Selection Sort

```python
def selection_sort(arr: list):
    for i in range(len(arr) - 1):
        min_i = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_i]:
                min_i = j

        if min_i != i:
            arr[i], arr[min_i] = arr[min_i], arr[i]

    return arr

print(selection_sort([33, 1, 89, 2, 67, 245]))
```

# Luhn algorithm
Verify card number
```python
def verify_card_number(digits: str):
    digits = digits.replace(' ', '').replace('-', '')
    
    arr = [int(i) for i in digits]

    for i in range(len(arr[:-1]) - 1, -1, -2):
        arr[i] = arr[i] * 2
        if arr[i] > 9:
            arr[i] -= 9
        
    if sum(arr) % 10 != 0:
        return 'INVALID!'
    else:
        return 'VALID!'
```
