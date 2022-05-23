def sort_array(source_array):
    out = []
    even_list = {}
    for idx, each in enumerate(source_array):
        if each % 2 == 0:
            even_list[idx] = each
        elif each % 2 != 0:
            out.append(each)
            out = sorted(out)

    for k, each in even_list.items():
        print(f"pos = {each} value = {k}")
        out.insert(k, each)

    return out
