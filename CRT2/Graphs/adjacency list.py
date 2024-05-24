n,m=map(int,input().split())#n-nodes,m-edges
adj = [] 
for i in range(n + 1):
    adj.append([])
 

 
for i in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
 
print(adj)

#output
'''
4 5
1 3 
3 2
2 4
2 3
1 4
[[], [3, 4], [3, 4, 3], [1, 2, 2], [2, 1]]
'''
