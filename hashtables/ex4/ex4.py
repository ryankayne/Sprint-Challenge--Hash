# b = [ 1, -1, 2, 3, -4, -3, 4, -5, 6, 7 ]

def has_negatives(a):
    # neg = {}
    # pos = {}
    # result = []

    # for x in a:
    #     if x < 0:
    #         neg[x] = abs(x)
    #     elif x > 0:
    #         pos[x] = x
    # for x in neg:
    #     if neg[x] == pos[x]:
    #         result.append(neg[x]) 
    #     # (neg.get(abs(x)) + x) == 0:
    #     #         result.append(abs(x))
    #     #     else:
    #     #         neg[abs(x)] = x
    # print(neg)
    # print(pos)        

    d = {}
    result = []

    for x in a:
        d[x] = abs(x)
        if d[x] in range(len(a)):
            if x < 0:
                result.append(abs(x))
    return result
# for every item x in array a, I want to store x in a dictionary. If the dictionary already has the key/value, then append to results list.


# print(has_negatives(b))

if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
