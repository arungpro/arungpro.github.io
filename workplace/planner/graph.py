from input import routeList

# import pdb;pdb.set_trace()
class Graph():
	def __init__(self):
		self.graph = {}
		self.graphWL = {}

	def computeMatrix(self):
		if routeList:
			for ele in routeList:
				src = ele[0]
				dest = ele[1]
				weight = ele[2]
				self.constructDirectedGraph(src, dest, weight)
				self.constructGraphWeightLess(src, dest, weight)
		return self.graph, self.graphWL

	def constructDirectedGraph(self, src, dest, weight):
		if not self.graph.get(src,''):
			self.graph[src] = {dest: int(weight)}
		else:
			self.graph[src].update({dest: int(weight)})

	def constructGraphWeightLess(self, src, dest, weight):
		if not self.graphWL.get(src,''):
			self.graphWL[src] = [dest]
		else:
			self.graphWL[src].append(dest)