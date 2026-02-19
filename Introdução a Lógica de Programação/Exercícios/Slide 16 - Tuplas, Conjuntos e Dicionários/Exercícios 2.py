d = {}
d["a"] = 15
d["b"] = None
d["c"] = 3
d["d"] = d["a"] / d["c"]
print(d)
d["b"] = -2
d.pop("c")
print("c" in d)
print(d)

# a: 15, b : -2, d : 5.0