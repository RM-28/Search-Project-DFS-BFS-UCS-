from collections import deque
import heapq
p = []

def read_state():
    file=open("input.txt","r")
    text=file.read()
    file.close()
    p=text.split(",")
    return (int(p[0]), int(p[1]), int(p[2]), int(p[3]), p[4].strip().upper())

def is_valid(s):
    m_left, c_left, m_right, c_right, boat = s
    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False
    if m_left > 0 and c_left > m_left:
        return False
    if m_right > 0 and c_right > m_right:
        return False
    return True

def model_a(m, c, boat):
    return 2*m + c

def model_b(m, c, boat):
    if boat == "L":
        return 2
    else:
        return 1

def successor(state):
    ml,cl,mr,cr,side=state
    childern=[]

    if side == "L":
        # 1 missionary
        if is_valid((ml-1, cl, mr+1, cr, "R")):
            childern.append(((ml-1, cl, mr+1, cr, "R"), 1, 0))

        # 1 cannibal
        if is_valid((ml, cl-1, mr, cr+1, "R")):
            childern.append(((ml, cl-1, mr, cr+1, "R"), 0, 1))

        # 2 missionaries
        if is_valid((ml-2, cl, mr+2, cr, "R")):
            childern.append(((ml-2, cl, mr+2, cr, "R"), 2, 0))

        # 2 cannibals
        if is_valid((ml, cl-2, mr, cr+2, "R")):
            childern.append(((ml, cl-2, mr, cr+2, "R"), 0, 2))

        # 1 missionary and 1 cannibal
        if is_valid((ml-1, cl-1, mr+1, cr+1, "R")):
            childern.append(((ml-1, cl-1, mr+1, cr+1, "R"), 1, 1))

    if side == "R":
        # 1 missionary
        if is_valid((ml+1, cl, mr-1, cr, "L")):
            childern.append(((ml+1, cl, mr-1, cr, "L"), 1, 0))

        # 1 cannibal
        if is_valid((ml, cl+1, mr, cr-1, "L")):
            childern.append(((ml, cl+1, mr, cr-1, "L"), 0, 1))

        # 2 missionaries
        if is_valid((ml+2, cl, mr-2, cr, "L")):
            childern.append(((ml+2, cl, mr-2, cr, "L"), 2, 0))

        # 2 cannibals
        if is_valid((ml, cl+2, mr, cr-2, "L")):
            childern.append(((ml, cl+2, mr, cr-2, "L"), 0, 2))

        # 1 missionary and 1 cannibal
        if is_valid((ml+1, cl+1, mr-1, cr-1, "L")):
            childern.append(((ml+1, cl+1, mr-1, cr-1, "L"), 1, 1))

    return childern

def show(path):
    steps = []
    for s in path:
        string = "(%d, %d, %d, %d, %s)" %s
        steps.append(string)

    return " -> ".join(steps)


def ucs(state, model):

    start = read_state()
    expand = 0
    tie_breaker = 0

    fringe = [(0, tie_breaker, state, [state])]

    q = []
    heapq.heappush(q, (0, tie_breaker, state, [state]))

    while q:
        i = heapq.heappop(q)
        cost = i[0]
        state = i[2]
        path = i[3]

        if state[0] == 0 and state[1] == 0:
            if model == model_a:
                print("The solution of Q2.1 (UCS, cost model A) is:")
            if model == model_b:
                print("The solution of Q2.2 (UCS, cost model B) is:")
            print("Solution path:", show(path))
            print("Total cost:", cost)
            print("Number of node expansions:", expand)
            break

        expand += 1
        for node, m, c in successor(state):
            if node not in path:
                tie_breaker += 1
                heapq.heappush(q, (cost + model(m, c, state[4]), tie_breaker, node, path + [node]))

start = read_state()
ucs(start, model_a)
print()
ucs(start, model_b)