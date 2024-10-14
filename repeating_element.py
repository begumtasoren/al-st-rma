def repeating_element(arr):

    seen = set()
    repeats = set()
    
    for num in arr:
        if num in seen:
            repeats.add(num)
        else:
            seen.add(num)

    return list(repeats) if repeats else -1
        
print(repeating_element([1,2,2,2,5,6,9,9,0,0,0,9]))