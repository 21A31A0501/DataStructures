def initiateDFSTraversal(node, visited, adj, result):
    result.append(node)
    visited[node] = True 
    
    for neighbour in adj[node]:
        if visited[neighbour] == False:
            initiateDFSTraversal(neighbour, visited, adj, result)
 
 
def printDFSTraversal(adj, n):
    result = []
    visited = [False] * n 
    for node in range(n):
        if visited[node] == False:
            initiateDFSTraversal(node, visited, adj, result)
            
    print("DFS Traversal is: ", result)
 
 
 
n, m = map(int, input().split())
# n is no.of nodes 
# m is no.of edges 
adj = [] 
for i in range(n):
    adj.append([])
 
for i in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

#printBFSTraversal(adj, n)
printDFSTraversal(adj, n)

#output
'''
5 5 --
1 3 less than n and m
2 4
1 4
2 3
1 2
DFS Traversal is:  [0, 1, 3, 2, 4]
'''
