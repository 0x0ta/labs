def first_non_consecutive(arr):
    for index, each in enumerate(arr):
        print(each)
        try:
            if each + 1 == arr[index +1]:
                pass
            else:
                return arr[index+1]
        except:
            pass