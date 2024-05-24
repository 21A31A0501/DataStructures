n,m=map(int,input().split())#n-nodes,m-edges
adj=[]
for i in range(n+1):
    eachRow=[0]*(n+1)
    adj.append(eachRow)
for i in range(m):
    u,v=map(int,input().split())
    adj[u][v]=1
    adj[v][u]=1
print(adj)

#output
''''
5 5
1 4
2 4
3 5
3 2
4 5
[[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 1, 0], [0, 0, 1, 0, 0, 1], [0, 1, 1, 0, 0, 1], [0, 0, 0, 1, 1, 0]]
'''