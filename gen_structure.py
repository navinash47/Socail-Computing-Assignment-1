import sys
import snap
FIn = snap.TFIn(sys.argv[1])
Fb_graph = snap.TNGraph.Load(FIn)

no_of_nodes = snap.CntNonZNodes(Fb_graph)
print("Number of Nodes: "+str(no_of_nodes))
no_of_edges = snap.CntUniqUndirEdges(Fb_graph)
print("Number of Edges: "+str(no_of_edges))
max_degree=-1
for i in range(1,no_of_nodes-1):
	degree=snap.CntDegNodes(Fb_graph, i)
	max_degree=max(degree,max_degree)
	print("Number of nodes with degree="+str(i)+": "+str(degree))

print("Max degree:"+str(max_degree))
print("Node id(s) with highest degree:",end=" ")
for NI in Fb_graph.Nodes():
	if(NI.GetInDeg()==max_degree):
		print(NI.GetId(),end=",")


snap.PlotInDegDistr(Fb_graph, "example.png", "Undirected graph - in-degree Distribution")
