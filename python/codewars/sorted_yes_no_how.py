def is_sorted_and_how(arr):
    return "yes, ascending" if sorted(arr) == arr else "yes, descending" if sorted(arr)[::-1] == arr else "no" 
