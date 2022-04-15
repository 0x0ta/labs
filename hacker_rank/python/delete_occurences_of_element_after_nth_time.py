def delete_nth(order, max_e):
    o = []
    print(max_e)
    for each in order:
        if o.count(each) < max_e:
            o.append(each)
    return o
