import sys
from graph import Graph
from queue import MyQUEUE

class Route():

    def __init__(self):
        self.graph, self.graphWL = Graph().computeMatrix()
        self.q = MyQUEUE()
        self.count = 0

    def shortestpath(self,start,end,visited=[],distances={},predecessors={}):
        """Find the shortest path between start and end nodes in a graph"""
        if start==end:
            path=[]
            while end != None:
                path.append(end)
                end=predecessors.get(end,None)

            if distances.get(start,''):
                return distances.get(start,''), path[::-1]
            else:
                return 'NO SUCH ROUTE', path[::-1]
        # detect if it's the first time through, set current distance to zero
        if not visited: distances[start]=0
        for neighbor in self.graph[start]:
            if neighbor not in visited:
                neighbordist = distances.get(neighbor,sys.maxint)
                tentativedist = distances[start] + self.graph[start][neighbor]
                if tentativedist < neighbordist:
                    distances[neighbor] = tentativedist
                    predecessors[neighbor]=start
        # neighbors processed, now mark the current node as visited
        visited.append(start)
        unvisiteds = dict((k, distances.get(k,sys.maxint)) for k in self.graph if k not in visited)
        closestnode = min(unvisiteds, key=unvisiteds.get)
        return self.shortestpath(closestnode,end,visited,distances,predecessors)

    def BFS(self, start, end):
        count = 0
        temp_path = [start]
        self.q.enqueue(temp_path)
        while self.q.IsEmpty() == False:
            tmp_path = self.q.dequeue()
            last_node = tmp_path[len(tmp_path)-1]
            #print tmp_path
            if last_node == end:
                count += 1
                print "PATH {0} : {1} ".format(count, tmp_path)
            for link_node in self.graphWL[last_node]:
                if link_node not in tmp_path:
                    new_path = []
                    new_path = tmp_path + [link_node]
                    self.q.enqueue(new_path)
        self.count = count

# r = Route()
# print r.shortestpath('E','A')
# print r.BFS('E','A')
# print r.count