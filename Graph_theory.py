class Node(object):
    def __init__(self,name):
        self.name=name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name

class Edge(object):
    def __init__(self,src,dest):
        self.src=src
        self.dest=dest
    def getSrc(self):
        return self.src
    def getDest(self):
        return self.dest
    def __str__(self):
        return self.getName()+'->'+dest.getName()

class Digraph(object):
    def __init__(self):
        self.edges={} #edges is a dictionary,that maps each node to a list of its childrens/destinations
    def addNode(self,node):
        if node in self.edges:
            raise ValueError('Duplicate Node')
        else:
            self.edges[node]=[]# Each node is saved a key which is associated with a list of destination nodes
    def addEdge(self,edge):
        src=edge.getSrc()
        dest=edge.getDest()
        if not(src in self.edges and dest in self.edges):
            ValueError('Node not in Graph')
        else:
            self.edges[src].append(dest)
    def childrenOf(self,node): #Find all children of a node
        return self.edges[node]
    def hasNode(self,node): # Check if the node is present in the graph
        return node in self.edges
    def getNode(self,name): #Get a Node by its getName
        for n in self.edges:
            if n.getName()==name:
                return n
        raise NameError(name) # This line never gets called as long as the name is present in the dictionary.
    def __str__(self): #print information about the graph
        result=''
        for src in self.edges:
            for dest in self.edges[src]:
                result=result+ src.getName()+'->'+ dest.getName()+'\n'
        return result

class Graph(Digraph): #an graph can have edges both ways(directions)
    def addEdge(self,edge):
        Digraph.addEdge(self,edge)
        #create an edge in other directions
        rev=Edge(edge.getDest(),edge.getSrc())
        Digraph.addEdge(self,rev)
#Why dont we make Digraph to be a subclass of Graph,because every Digraph is a graph but every graph is not a Digraph.
#That means anything that works for digraph will work for Graph, but anything that works for Graph may or may not work for Digraphs.

def buildCityGraph(graphType):
    g = graphType()
    for name in ('Boston', 'Providence', 'New York', 'Chicago','Denver', 'Phoenix', 'Los Angeles'):
        g.addNode(Node(name))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('Providence')))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('Boston')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('New York'), g.getNode('Chicago')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Denver')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Los Angeles'), g.getNode('Boston')))
    return g

g=buildCityGraph(Digraph)
print(g)

def printPath(path):
    """Assumes path is a list of nodes"""
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '->'
    return result

def DFS(graph,start,end,path,shortest,toPrint=False):
    path=path+[start]
    if toPrint:
        print('Current DFS path',printPath(path))
    if start==end:
        return path
    for node in graph.childrenOf(start):
        if node not in path:
            if shortest==None or len(path)<len(shortest):
                newPath=DFS(graph,node,end,path,shortest,toPrint)
                if newPath!=None:
                    shortest=newPath
        elif toPrint:
            print('Already visited',node)
    return shortest

def shortestPath(graph,start,end,toPrint=False):
    return DFS(graph,start,end,[],None,toPrint)


def testSP(source, destination):
    g = buildCityGraph(Digraph)
    sp = shortestPath(g, g.getNode(source), g.getNode(destination),toPrint = True)
    if sp != None:
        print('Shortest path from', source, 'to',
              destination, 'is', printPath(sp))
    else:
        print('There is no path from', source, 'to', destination)

testSP('Chicago', 'Boston')
print()
