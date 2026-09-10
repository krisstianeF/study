# Hanoi algorithm

```python
def hanoi_solver(n):
    rods = [list(range(n, 0, -1)), [], []]
    states = []

    def record():
        states.append(" ".join(str(rod) for rod in rods))

    def move_one(source, target):
        disk = rods[source].pop()
        rods[target].append(disk)
        record()

    def solve(disks, source, auxiliary, target):
        if disks == 1:
            move_one(source, target)
        else:
            solve(disks - 1, source, target, auxiliary)
            move_one(source, target)
            solve(disks - 1, auxiliary, source, target)

    record()
    solve(n, 0, 1, 2)
    return "\n".join(states)


print(hanoi_solver(4))
```
