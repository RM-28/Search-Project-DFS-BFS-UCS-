
INITAL_MOVES = [(2,0), (1,1), (0,2), (1,0), (0,1)]

p = []

def read_state():
    line = open("input.txt").readline().strip()
    for x in line.split(","):
        p.append(x.strip())

    return (int(p[0]), int(p[1]), int(p[2]), int(p[3]), p[4].upper())

def is_valid(s):
    m_left, c_left, m_right, c_right, boat = s
    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False
    if m_left > 0 and c_left > m_left:
        return False
    if m_right > 0 and c_right > m_right:
        return False
    return True

def successor(s):
    m_left, c_left, m_right, c_right, boat = s
    results = []

    for m, c in INITAL_MOVES:
        if boat == "L":
            next = (m_left - m, c_left - c, m_right + m, c_right + c, "R")
        else:
            next = (m_left + m, c_left + c, m_right - m, c_right - c, "L")

        if is_valid(next):
            results.append(next)
    return results

def show(path):
    steps = []
    for s in path:
        string = "(%d, %d, %d, %d, %s)" %s
        steps.append(string)

    return " -> ".join(steps)


def dfs(start):
    fringe = [[start]]
    expand = 0

    while fringe:
        p = fringe.pop()
        s = p[-1]

        if s[0] == 0 and s[1] == 0:
            return p, expand
        expand += 1

        for next in reversed(successor(s)):
            if next not in p:
                fringe.append(p + [next])

    return None, expand

#question 1.1a print answer
start = read_state()
path, expand = dfs(start)

print("The solution of 1.1.a (DFS) is:")
print("Solution Path: ", show(path))
print("Total cost =", len(path) - 1)
print("Number of node expansions = ",expand)