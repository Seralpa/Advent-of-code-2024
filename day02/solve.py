import os


def is_safe(report: list[int]) -> bool:
	steps = [a - b for a, b in zip(report, report[1:])]
	return all(0 < s < 4 for s in steps) or all(-4 < s < 0 for s in steps)


def is_safe2(report: list[int]) -> bool:
	for i in range(len(report)):
		if is_safe(report[:i] + report[i + 1:]):
			return True
	return False


cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	reports = [list(map(int, l.split(" "))) for l in f.read().splitlines()]

print(f"part 1: {len([r for r in reports if is_safe(r)])}")
print(f"part 2: {len([r for r in reports if is_safe2(r)])}")
