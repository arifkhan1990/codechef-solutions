class Node:
    def __init__(self, data, idx):
        self.data = data
        self.left = None
        self.right = None
        self.idx = idx
        
    
    # Insert new node
def insert(node, data, idx = 0):
    # Return new node if the node empty
    if node is None:
        return Node(data, idx)
    
    #Find the right place and insert the new node
    if data < node.data:
        node.left = insert(node.left, data,idx)
    else:
        node.right = insert(node.right, data, idx)
    return node


def inorderPrint(node, ans):
    if node:
        
        # Traversal left
        inorderPrint(node.left,ans)
        
        # Traversal root
        # print(str(node.idx) + "->", end=' ')
        ans.append(node.idx)
        
        #Traversal right
        inorderPrint(node.right,ans)
    return ans
    # print(ans)


T = int(input())
for i in range(T):
    n = int(input())

    g1 = list(map(int,input(' ').strip().split()))[:n]
    w1 = list(map(int,input(' ').strip().split()))[:n]
    
    g = None
    for i in range(0,n):
        g = insert(g, g1[i], i)


    w = None
    for i in range(0,n):
        w = insert(w, w1[i], i)
        
    ans = [0]*n
    gS = wS = []

    gS = inorderPrint(g, [])
    wS = inorderPrint(w, [])

    for i in range(n):
        ans[gS[i]] += i
        wl = wS.index(gS[i])
        ans[gS[i]] +=   len(wS[0:wl]) - (len(set(wS[0:wl]) - set(gS[i+1:])))
        # print(gS[i+1:])
        # print(wS[0:wl], wl, len(wS[0:wl]) - len(gS[i+1:]), sep=' ')
    maximum = max(ans)
    qualify = ans.count(maximum)
    print(qualify)
