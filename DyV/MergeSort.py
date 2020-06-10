def mergesort(elements):
    if len(elements) < 2:
        return

    mid = len(elements) // 2
    left = elements[:mid]
    right = elements[mid:]
    mergesort(left)
    mergesort(right)
    merge(left, right, elements)


def merge(first, second, output):

    k = f = s = 0
    while f < len(first) and s < len(second):
        if first[f] <= second[s]:
            output[k] = first[f]
            f += 1
        else:
            output[k] = second[s]
            s += 1
        k += 1

    # if we run out of elements either in "first"
    # or "second" then we copy the remaining elements
    r = f if s == len(second) else s
    remaining = first if s == len(second) else second
    for i in range(r, len(remaining)):
        output[k] = remaining[i]
        k += 1



N = int(input().strip())
numeros = list(map(int, input().strip().split()))

mergesort(numeros)
print(*numeros)