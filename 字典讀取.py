a={
    "a": {
        "a1": "a-1",
        "a2": "a-1"
    },
    "b": {
        "b1": "b-1",
        "a2": "b-1"
    }
}
b=list(a.keys())
for i in range(len(b)):
    print(a[b[i]])
    print(b[i])
###########輸出###########
# {'a1': 'a-1', 'a2': 'a-1'}
# a
# {'b1': 'b-1', 'a2': 'b-1'}
# b
