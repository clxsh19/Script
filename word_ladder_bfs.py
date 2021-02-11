from pythonds.graphs import Graph
from pythonds.basic import Queue
import ujson, os

def buildGraph(wdict):
	d = {}
	g = Graph()

	for word in wdict:
		for i in range(len(word)):
			bucket = word[:i] + '_' + word[i+1:]
			if bucket in d:
				d[bucket].append(word)
			else:
				d[bucket] = [word]

	for bucket in d.keys():
		for word1 in d[bucket]:
			for word2 in d[bucket]:
				if word1 != word2:
					g.addEdge(word1,word2)
	return g

def bfs(g, start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while (vertQueue.size() > 0):
        currentVert = vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if (nbr.getColor() == 'white'):
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColor('black')
    
def transverse(y):
    x = y
    while (x.getPred()):
        print(x.getId())
        x = x.getPred()
    print(x.getId())

# getting words from json file
fpath = os.path.abspath("4.json")
wfile = open(fpath, "r")
wdict = ujson.load(wfile)

g = buildGraph(wdict)
start = g.getVertex('tail')
end = g.getVertex('boat')

bfs(g,start)
transverse(end)

