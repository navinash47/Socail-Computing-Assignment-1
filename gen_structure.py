import sys
import snap
# FIn = snap.TFIn(sys.argv[1])
#!/usr/bin/env python
# coding: utf-8

FIn = snap.TFIn("facebook.elist")
Fb_graph = snap.TNGraph.Load(FIn)


# # 1 and 2 c(partial)




no_of_nodes = snap.CntNonZNodes(Fb_graph)
print("Number of Nodes: "+str(no_of_nodes))
no_of_edges = snap.CntUniqUndirEdges(Fb_graph)
print("Number of Edges: "+str(no_of_edges))
max_degree=-1
degdis_y=[]
degdis_x=[]
for i in range(1,no_of_nodes-1):
    degree=snap.CntDegNodes(Fb_graph, i)
    max_degree=max(degree,max_degree)
    degdis_x.append(i)
    degdis_y.append(degree)


# # 2 b



print("Max degree:"+str(max_degree))
print("Node id(s) with highest degree:",end=" ")
for NI in Fb_graph.Nodes():
	if(NI.GetInDeg()==max_degree):
		print(NI.GetId(),end=",")


# # 2 c plotting




from matplotlib import pyplot as plt 
plt.plot(degdis_x,degdis_y,color="black")
plt.xlabel('Degree')  
plt.ylabel('No of Nodes')  
  
# displaying the title 
plt.title("Degree Distribution")
plt.show()
# plt.savefig("deg_dist_"+"facebook"+".png")


# # 3a



full_diam_list=[]
for i in range(1,4):
    no_nodes=10**i
    full_diam = snap.GetBfsFullDiam(Fb_graph, no_nodes, False)
    full_diam_list.append(full_diam)
    print("Approximate full diameter by sampling "+str(no_nodes)+ " nodes: "+str(round(full_diam, 4)))
    
mean = sum(full_diam_list) / len(full_diam_list) 
res = sum((i - mean) ** 2 for i in full_diam_list) / len(full_diam_list) 
print("Approximate full diameter (mean and variance): "+str(round(mean, 4))+","+str(round(res, 4)))




eff_diam_list=[]
for i in range(1,4):
    no_nodes=10**i
    eff_diam = snap.GetBfsEffDiam(Fb_graph, no_nodes, False)
    eff_diam_list.append(eff_diam)
    print("Approximate effective  diameter by sampling "+str(no_nodes)+ " nodes: "+str(round(eff_diam, 4)))
    
mean = sum(eff_diam_list) / len(eff_diam_list) 
res = sum((i - mean) ** 2 for i in eff_diam_list) / len(eff_diam_list) 
print("Approximate effective  diameter (mean and variance): "+str(round(mean,4))+","+str(round(res,4)))





snap.PlotShortPathDistr(Fb_graph, "exa", "Directed graph - shortest path")






