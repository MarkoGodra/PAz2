import sys
import queue
import enum

TIME = 0

class Color(enum.Enum) :
    """ Boja, odredjuje stanje cvora """
    black = 0
    gray = 127
    white = 255

class Vertex :
    """Cvor, ima boju(stanje), ime,
        roditelja, i data """
    def __init__(self, name):
        self.name = name
        self.color = Color.white
        self.parent = None
        self.data = None

    def __repr__(self):
        return "{2}:{0} Data: {1}".format(self.color, self.data, self.name)

    def reset(self) :
        self.color = Color.white
        self.parent = None
        self.data = {
            'Discovery' : None,
            'Finish' : None
        }
        

def BFS(graph, source) :
    source.reset()
    vertex_queue = queue.Queue()
    for vertex in graph.keys() :
        if vertex != source :
            vertex.reset()
    source.color = Color.gray
    time = 0
    source.data['Discovery'] = time
    source.parent = None
    vertex_queue.put(source)
    while not vertex_queue.empty() :
        vertex_source = vertex_queue.get()
        for vertex in graph[vertex_source] :
            if vertex.color == Color.white :
                vertex.color = Color.gray
                vertex.parent = vertex_source
                time += 1
                vertex.data['Discovery'] = time
                vertex_queue.put(vertex)
            time += 1
            vertex_source.color = Color.black
            vertex_source.data['Finish'] = time

def print_path(source, destination) :
    """ Printovanje puta izmedju 2 cvora """
    if source == destination :
        print(source)
    elif destination.parent == None :
        print("No path found")
    else :
        print_path(source, destination.parent)
        print(destination)

def DFS(graph, vertex, list = None) :
    for vertex in graph.keys() :
        vertex.reset()
    time = 0
    for vertex in graph.keys() :
        if vertex.color == Color.white :
            time = DFS_visit(graph, vertex, time, list)

def DFS_visit(graph, element, time, list = None) :
    time += 1
    element.data['Discovery'] = time
    element.color = Color.gray
    for vertex in graph[element] :
        if vertex.color == Color.white :
            vertex.parent = element
            time = DFS_visit(graph, vertex, time, list)
    element.color = Color.black
    time += 1
    element.data['Finish'] = time
    """ Kad god se zavrsi obrada nekog cvora, stavi ga u listu """
    if list != None :
        list.insert(0, element)
    return time

    


# Main
v1 = Vertex(1)
v2 = Vertex(2)
v3 = Vertex(3)
v4 = Vertex(4)
v5 = Vertex(5)

graph1 = {}

graph1[v1] = [v2, v5]
graph1[v2] = [v1, v3, v4, v5]
graph1[v3] = [v2, v4]
graph1[v4] = [v2, v3, v5]
graph1[v5] = [v1, v2, v4]

print("\nGraph 1")
BFS(graph1, v1)
print_path(v1, v3)

v6 = Vertex(6)

graph2 = {}
graph2[v1] = [v2, v4]
graph2[v2] = [v5]
graph2[v3] = [v5, v6]
graph2[v4] = [v2]
graph2[v5] = [v4]
graph2[v6] = [v6]

print("\nGraph 2, v1")
BFS(graph2, v1)
print_path(v1, v5)

print("\nGraph2, v3")
BFS(graph2, v3)
print_path(v3, v2)

graph3 = {}

vr = Vertex('r')
vv = Vertex('v')
vs = Vertex('s')
vw = Vertex('w')
vt = Vertex('t')
vx = Vertex('x')
vu = Vertex('u')
vy = Vertex('y')

graph3[vv] = [vr]
graph3[vr] = [vs, vv]
graph3[vs] = [vw, vr]
graph3[vw] = [vs, vt, vx]
graph3[vt] = [vw, vx, vu]
graph3[vx] = [vw, vt, vy, vu]
graph3[vu] = [vt, vy]
graph3[vy] = [vx, vu]

print("\nGraph3 v -> u")
BFS(graph3, vv)
print_path(vv, vu)

graph4 = {}
graph4[vw] = [vy, vr]
graph4[vu] = [vv, vx]
graph4[vx] = [vv]
graph4[vv] = [vy]
graph4[vy] = [vx]
graph4[vr] = [vr]

print("\nGraph4 w -> y")
DFS(graph4, vw)
print_path(vw, vv)

list = []

UNDERWEAR = Vertex('Underwear')
PANTS = Vertex('Pants')
BELT = Vertex('Belt')
TIE = Vertex('Tie')
SHIRT = Vertex('Shirt')
SHOES = Vertex('Shoes')
SOCKS = Vertex('Socks')
WATCH = Vertex('Watch')
JACKET = Vertex('Jacket')
GRAPH = {
    UNDERWEAR: [PANTS, SHOES],
    PANTS: [BELT, SHOES],
    BELT: [JACKET],
    JACKET: [],
    TIE: [JACKET],
    SOCKS: [SHOES],
    WATCH: [],
    SHOES: [],
    SHIRT: [BELT]
}

print("\nTopological sort")
DFS(GRAPH, WATCH, list)
for item in list :
    print(item.name)