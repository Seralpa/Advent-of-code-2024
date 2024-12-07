import os

cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	data = [list(l) for l in f.read().splitlines()]

dirs = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]
tgt1 = "XMAS"
tgt2 = "MAS"

n_XMAS = 0
n_X_MAS = 0
for i, l in enumerate(data):
	for j, c in enumerate(l):
		# part 1
		for d in dirs:
			if not ((0 <= i + (d[0] * 3) < len(data)) and (0 <= j + (d[1] * 3) < len(l))):
				# word direction goes out of matrix
				continue
			if "".join(data[i + (d[0] * n)][j + (d[1] * n)] for n in range(4)) == tgt1:
				n_XMAS += 1

		# part 2
		if not ((1 <= i < len(data) - 1) and (1 <= j < len(l) - 1)):
			# X goes out of matrix
			continue
		w1 = "".join([data[i - 1][j - 1], c, data[i + 1][j + 1]])
		w2 = "".join([data[i - 1][j + 1], c, data[i + 1][j - 1]])
		if (w1 in (tgt2, reversed(tgt2))) and (w2 in (tgt2, reversed(tgt2))):
			n_X_MAS += 1

print(f"part 1: {n_XMAS}")
print(f"part 2: {n_X_MAS}")
