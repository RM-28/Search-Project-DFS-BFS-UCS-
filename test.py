from collections import deque




def is_valid(state):
    ml,cl,mr,cr,side=state

    if ml < 0 or ml > 3 or cl < 0 or cl > 3 or mr < 0 or mr > 3 or cr < 0 or cr > 3:
        return False
    if cl>ml and ml>0:
        return False
    if cr>mr and mr>0:
        return False
    return True

def get_valid_chidern(state):
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

def main():

    file=open("input.txt","r")
    text=file.read()
    file.close()

    parts=text.split(",")

    ml=int(parts[0])
    cl=int(parts[1])
    mr=int(parts[2])
    cr=int(parts[3])
    side=parts[4].strip()

    start=(ml,cl,mr,cr,side)

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

        

if __name__ == "__main__":
    main()