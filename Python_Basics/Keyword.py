import keyword

print("Total Python Keywords: ", len(keyword.kwlist))
print("List of Keywords: ")
for i, kw in enumerate(keyword.kwlist,start=1):
    print(f"{i:2d}, {kw:12}", end="" if i%4!=0 else "")
print()