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
    def addNode(self):
        if node in self.edges:
            raise ValueError('Duplicate Node')
        else:
            self.edges[node]=[]# Each node is saved a key which is associated with a list of destination nodes
    def addEdge(self):
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
                result=result+ src.getName()+'->'+ dest.getName()
        return result


class Graph(Digraph): #an graph can have edges both ways(directions)
    def addEdge(self,edge):
        Digraph.addEdge(self,edge)
        #create an edge in other directions
        rev=Edge(edge.getDest(),edge.getSrc())
        Digraph.addEdge(self,rev)
#Why dont we make Digraph to be a subclass of Graph,because every Digraph is a graph but every graph is not a Digraph.
#That means anything that works for digraph will work for Graph, but anything that works for Graph may or may not work for Digraphs.
