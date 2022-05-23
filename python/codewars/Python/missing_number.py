def missing_no(nums):
    i = 0
    while i <= len(nums):
        if i not in nums:
            missing_number = i
        i += 1
    return missing_number