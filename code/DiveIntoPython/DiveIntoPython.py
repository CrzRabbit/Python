file = open("test.txt", "r+")

s = "100 NORTH MAIN ROAD"

print(s[:-4] + s[-4:].replace(r"ROAD", "RD"))