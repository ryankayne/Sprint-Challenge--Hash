def finder(files, queries):
    d = {}
    result = []

    for x in files:
        text = x.split("/")
        if text[-1] not in d:
            # d[text[-1]] = x
            d[text[-1]] = [x]
        else:
            # print("Not important")
            d[text[-1]].append(x)
            # return None
    for x in queries:
        if x in d:
            # for y in len(d[x]):
            for y in range(len(d[x])):
                # access length so you can always access the first value at index 0. For y in range of d[x], which would be "foo: [path]", [path] being index 0.
                result.append(d[x][y])
                # appending the full path value of the current key to the results list!
    return result

# w3
# txt = "/usr/local/share/foo.txt"
# x = txt.split("/")
# print(x)

# https://stackoverflow.com/questions/1950672/python-split-list-into-list-of-dicts
# result = [{}]
# for item in data:
#     key, val = item.split(":", 1)
#     if key in result[-1]:
#         result.append({})
#     result[-1][key] = val



if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
