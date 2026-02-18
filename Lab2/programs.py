def insertion_sort(lst):
    for index in range(1, len(lst)):
        i = index
        while lst[i] < lst[i-1] and i > 0:
            lst[i], lst[i-1] = lst[i-1], lst[i]
            i -= 1
    return lst

def is_member_sorted(lst, key):
    l, r = 0, len(lst)

    while (l < r):
        m = (l + r) // 2

        if key == lst[m]:
            return True

        if key < lst[m]:
            r = m
        else:
            l = m + 1

    return False

def is_member(lst, key):
    return is_member_sorted(insertion_sort(lst), key)