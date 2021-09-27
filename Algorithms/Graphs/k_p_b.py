import heapq
class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight
    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])
    def getConnections(self):
        return self.connectedTo.keys()
    def getId(self):
        return self.id
    def getWeight(self,nbr):
        return self.connectedTo[nbr]
class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
        self.front=[]
        self.back=[]
        self.depfs=[]
    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex
    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
    def __contains__(self,n):
        return n in self.vertList
    def addEdge(self,f,t,cost=0):  #f is from node, t is to node
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t],cost)
        self.vertList[t].addNeighbor(self.vertList[f],cost)
    def getVertices(self):
        return self.vertList.keys()
    
    
    def __iter__(self):
        return iter(self.vertList.values())
    """
    Write a method to generate an adjacency matrix representation of the graph
    """
    def createAdjMatrix(self):
        adjmat = list()
        
        for x in sorted(self.vertList):
            key = self.vertList[x]
            temp = []
            for y in sorted(self.vertList):
                anotherkey = self.vertList[y]
                if anotherkey in key.connectedTo:
                    temp.append(1)
                else:
                    temp.append(0)
            adjmat.append(temp)
        
    
    
    def find_component(self, com, i):
        if com[i] == i:
            return i
        return self.find_component(com, com[i])
    def union(self,com,rank,x,y):
        xr = self.find_component(com,x)
        yr = self.find_component(com,y)
        if rank[xr] < rank[yr]:
            com[xr] = yr
        elif rank[xr] > rank[yr]:
            com[yr] = xr
        else:
            com[yr] = xr
            rank[xr] += 1
        
    def mstKruskal(self):
        edged=[]
        for v in self.vertList:
            for w in self.vertList[v].getConnections():
                edged.append([self.vertList[v].getId(),w.getId(),self.vertList[v].connectedTo[w]])
        
        x=sorted(edged,key=lambda edge:edge[2])
        e=0
        com={}
        mst=[]
        for i in self.vertList:
            com[i] = i
            
        i=0
        minw=0
        while(e<self.numVertices-1):
            u=x[i][0]
            v=x[i][1]
            w=x[i][2]
            i += 1
            z=self.find_component(com,u)
            y=self.find_component(com,v)
            if z!=y:
                e=e+1
                mst.append([u,v,w])
                minw=minw+w
                com[y]=z
        print("\nKruskal's:\n")    
        print(mst)
        print("Minimum Weight: ",minw)
        return
    
    def mstPrims(self,sv):
        edged=[]
        for w in self.vertList[sv].getConnections():
            edged.append([self.vertList[sv].connectedTo[w],self.vertList[sv].getId(),w.getId()])
        mst = []
        visited = set([sv])
        heapq.heapify(edged)
        sum=0
        while edged:
            cost,frm,to= heapq.heappop(edged)
            if to not in visited:
                visited.add(to)
                mst.append([frm,to,cost])
                sum=sum+cost
                for to_next in self.vertList[to].getConnections():
                    if to_next.getId() not in visited:
                        heapq.heappush(edged,[self.vertList[to].connectedTo[to_next],to,to_next.getId()])
        print("\nPrim's:")
        print(mst)
        print("Cost of Prims MST: ",sum)
        return 
    def mstBoruvka(self):
        com = []
        rank = []
        c = []
        nT = self.numVertices
        """for i in self.vertList:
            com[i] = i"""
        
        for node in range(self.numVertices):
            com.append(node)
            rank.append(0)
            c = [-1]*self.numVertices
        edged = []
        for v in self.vertList:
            for w in self.vertList[v].getConnections():
                edged.append([self.vertList[v].getId(),w.getId(),self.vertList[v].connectedTo[w]])
        print("\nBoruvka's:")
        print("[",end="")
        sum=0
        while nT > 1:
            
            for i in range(len(edged)):
                u = int(edged[i][0])
                v = int(edged[i][1])
                w = int(edged[i][2])
                
                g1 = int(self.find_component(com,u))
                g2 = int(self.find_component(com,v))
                if(g1 != g2):
                    if c[g1] == -1 or c[g1][2] > w:
                        c[g1] = [u,v,w]
                    if c[g2] == -1 or c[g2][2] > w:
                        c[g2] = [u,v,w]
            for node in range(self.numVertices):
                
                if c[node] != -1:
                    u,v,w = c[node]
                    g1 = self.find_component(com,u)
                    g2 = self.find_component(com,v)
                    if g1 != g2:
                        self.union(com,rank,g1,g2)
                        
                        print("[",u,v,w,"]",end = ", ")
                        
                        nT -= 1
                        sum=sum+int(w)
            c=[-1]*self.numVertices
        print("]")
        print("Minimun Weight: ",sum)
        return
def testGraph():
    g = Graph()
    with open('D:\Algorithms\Graphs\input.txt') as f:
        data = f.readlines()
    n = int(data[0])
    print(n)
    for i in range(1,len(data)):
        inp = list(data[i].split())
        g.addEdge(int(inp[0]), int(inp[1]), int(inp[2]))
    for v in g:
        for w in v.getConnections():
            print("( %s , %s )" % (v.getId(), w.getId()))
    """n=int(input("Enter no of size: "))
    for i in range(n):
        inp=input('Enter from,to,wight  of the edge : ')
        inp=list(inp.split())
        g.addEdge(int(inp[0]), int(inp[1]), int(inp[2]))"""
    """for v in g:
        for w in v.getConnections():
            print("( %s , %s )" % (v.getId(), w.getId()))"""
    
    #start = g.getVertex('a')
    
    #print "Minimum Spanning Tree"
    g.mstKruskal()
    g.mstBoruvka()
    g.mstPrims(1)
def main():
    testGraph()
if __name__ == '__main__':
    main()
'''
5
0 1 5
0 3 40
0 2 35
3 4 50
1 5 40
2 4 10
2 5 30
4 5 25
4 6 35
6 5 20
5 9 20
9 8 20
8 7 50
6 7 20
'''