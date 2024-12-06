import os

cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	right, left = zip(*[map(int, l.split("   ")) for l in f.read().splitlines()])

print(f"part 1: {sum(abs(r - l) for r, l in zip(sorted(right), sorted(left)))}")
print(f"part 2: {sum(e * right.count(e) for e in left)}")
