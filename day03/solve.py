import os, re

mul = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
cond_mul = re.compile(r"(?:mul\((\d{1,3}),(\d{1,3})\))|((?:do\(\))|(?:don't\(\)))")

cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	data = f.read()
print(f"part 1: {sum(int(a)*int(b) for a,b in mul.findall(data))}")

active = True
total = 0
for m in cond_mul.findall(data):
	match m:
		case ["", "", "do()"]:
			active = True
		case ["", "", "don't()"]:
			active = False
		case [a, b, ""]:
			if active:
				total += int(a) * int(b)
		case _:
			raise ValueError(f"Error unexpected match result {m}")
print(f"part 2: {total}")
