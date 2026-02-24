def insertion_sort(lst):
    for i in range(1, len(lst)):
        # Mutation 3: while lst[i] < lst[i-1] and i >= 0:
        # Mutation 4: while lst[i] > lst[i-1] and i > 0:
        while lst[i] < lst[i-1] and i > 0:
            lst[i], lst[i-1] = lst[i-1], lst[i]
            i -= 1
    return lst

def is_member_sorted(lst, key):
    # Mutation 5: r, l = 0, len(lst)
    l, r = 0, len(lst)

    # Mutation 6: while (l <= r):
    while (l < r):
        # Mutation 1: m = (l - r) // 2
        m = (l + r) // 2

        if key == lst[m]:
            return True

        if key < lst[m]:
            # Mutation 2: r = m - 1
            r = m - 1
        else:
            l = m + 1

    return False

def is_member(lst, key):
    return is_member_sorted(insertion_sort(lst[:]), key)