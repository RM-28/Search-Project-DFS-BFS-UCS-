
from collections import deque
INITAL_MOVES = [(2,0), (1,1), (0,2), (1,0), (0,1)]

p = []

def read_state():
    file=open("input.txt","r")
    text=file.read()
    file.close()
    p=text.split(",")
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

def successor(state):
    ml,cl,mr,cr,side=state
    childern=[]

    if side == "L":
        # 1 missionary
        if is_valid((ml-1, cl, mr+1, cr, "R")):
            childern.append((ml-1, cl, mr+1, cr, "R"))

        # 1 cannibal
        if is_valid((ml, cl-1, mr, cr+1, "R")):
            childern.append((ml, cl-1, mr, cr+1, "R"))

        # 2 missionaries
        if is_valid((ml-2, cl, mr+2, cr, "R")):
            childern.append((ml-2, cl, mr+2, cr, "R"))

        # 2 cannibals
        if is_valid((ml, cl-2, mr, cr+2, "R")):
            childern.append((ml, cl-2, mr, cr+2, "R"))

        # 1 missionary and 1 cannibal
        if is_valid((ml-1, cl-1, mr+1, cr+1, "R")):
            childern.append((ml-1, cl-1, mr+1, cr+1, "R"))

    if side == "R":
        # 1 missionary
        if is_valid((ml+1, cl, mr-1, cr, "L")):
            childern.append((ml+1, cl, mr-1, cr, "L"))

        # 1 cannibal
        if is_valid((ml, cl+1, mr, cr-1, "L")):
            childern.append((ml, cl+1, mr, cr-1, "L"))

        # 2 missionaries
        if is_valid((ml+2, cl, mr-2, cr, "L")):
            childern.append((ml+2, cl, mr-2, cr, "L"))

        # 2 cannibals
        if is_valid((ml, cl+2, mr, cr-2, "L")):
            childern.append((ml, cl+2, mr, cr-2, "L"))

        # 1 missionary and 1 cannibal
        if is_valid((ml+1, cl+1, mr-1, cr-1, "L")):
            childern.append((ml+1, cl+1, mr-1, cr-1, "L"))

    return childern

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





#BFS
def BFS():
    start=read_state()

    #this variable keeps track of the expansions that happens
    expansions=0


    #I am going to format it as (state, cost, path to that node)
    q = deque()
    q.append((start, 0, [start]))
    while q:
        state, cost, path_list=q.popleft()
        
        if state==(0,0,3,3,"R"):
            
            print("The solution of Q1.1.b (BFS) is:")
            print("Solution Path:", path_list)
            print("Total cost =", cost)
            print("Number of node expansions =", expansions)
            break

        expansions+=1

        for node in get_valid_chidern(state):
            q.append((node, cost+1, path_list+[node]))

        
  