Colors = {"Sam":"Blue", "Amy":"Red", "Sarah": "Yellow"}
print(Colors["Sarah"])
print(Colors.keys())

for item in Colors.keys():
    print("{0} like the color {1}".format(item, Colors[item]))

Colors["Sarah"] = "Purple"
Colors.update({"Harry":"Orange"})
del Colors['Sam']

print(Colors)