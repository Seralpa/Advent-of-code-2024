import os


def is_ordered(update: list[int]) -> bool:
	for i, page in enumerate(update):
		if page not in rule_dict.keys():
			continue
		if len(set(update[:i]) & rule_dict[page]) > 0:
			return False
	return True


cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	rules, updates = f.read().split("\n\n")

rule_dict: dict[int, set[int]] = dict()
for rule in rules.splitlines():
	l, r = map(int, rule.split("|"))
	if l in rule_dict.keys():
		rule_dict[l].add(r)
	else:
		rule_dict[l] = {r}

updates = [list(map(int, u.split(","))) for u in updates.splitlines()]
correct = [u for u in updates if is_ordered(u)]
wrong = [u for u in updates if not is_ordered(u)]

print(f"part 1: {sum(u[len(u) // 2] for u in correct)}")

for u in wrong:
	i = 0
	while i < len(u):
		page = u[i]
		if page not in rule_dict.keys():
			i += 1
			continue
		offending_pages = set(u[:i]) & rule_dict[page]
		if len(offending_pages) == 0:
			i += 1
			continue
		offender_index = min(u.index(p) for p in offending_pages)
		u.pop(i)
		u.insert(offender_index, page)
		i = offender_index + 1

print(f"part 2: {sum(u[len(u) // 2] for u in wrong)}")
