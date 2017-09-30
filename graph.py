class Vertex:
    def __init__(self,x:float,y:float,label):
        self.x = x
        self.y = y
        self.label = label

    def print(self):
        return '{}:({},{})' \
            .format(self.label, self.x, self.y)


class Edge:
    def __init__ (self, v1: Vertex, v2: Vertex, weight: int = 1):
        self.start = v1
        self.end = v2
        self.weight = weight
    def print(self):
        return '[{}-->{}:{}]'\
            .format(self.start.print(),self.end.print(),self.weight)

v1 = Vertex(1,2,'ala')
v2 = Vertex(2,3,'ala')
e1 = Edge(v1,v2)
print(e1.print())