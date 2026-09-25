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

def heuristic_one(state):
    ml,cl,mr,cr,side=state
    return 2*ml+cl

def heuristic_two(state):
    ml,cl,mr,cr,side=state
    return (2*ml +cl + 2)//3

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


def A_star(start, model):

    
    expand = 0
    tie_breaker = 0

    

    q = []
    
    #(f cost, tie breaker, actual cost, state, path)
    heapq.heappush(q, (model(start), tie_breaker, 0, start, [start]))

    while q:
        i = heapq.heappop(q)

        f_cost = i[0]
        state = i[3]
        cost = i[2]
        path = i[4]

        if state == (0,0,3,3,"R"):

            if model == heuristic_one:
                print("The solution of Q3.1 (Heuristic 1) is:")
            else:
                print("The solution of Q3.1 (Heuristic 2) is:")

            print("Solution Path:", show(path))
            print("Total cost:", cost)
            print("Number of node expansions:", expand)
            break

        expand += 1
        for node, m, c in successor(state):
            if node not in path:
                action_cost= 2*m + c

                new_cost = cost +action_cost

                tie_breaker+= 1

                f_cost= new_cost + model(node)

                heapq.heappush(q, (f_cost, tie_breaker, new_cost, node, path +[node]))

start = read_state()
A_star(start, heuristic_one)
print()
A_star(start, heuristic_two)