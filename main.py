import networkx
from cdlib import evaluation
from cdlib.benchmark import LFR as t

from CommunityDiscovery_SLPA import *
from Modularity import *

from LFRTestGraph import *
def applyingSLPA(graph,specs):
    slpa=CommunityDiscovery_SLPA()
    com,elapsedTime=slpa.slpaSingle(graph)
    modularity=Modularity()
    fitness=modularity.modularityOverlap(graph,com)
    comTime = modularity.elapsedTime()
    print("Node = ", spec[0])
    print("Tau1 = ", spec[1])
    print("Tau2 = ", spec[2])
    print("Mu   = ", spec[3])
    print("Result--> Modularity = ", fitness.score, " Graph Generated in = ", elapsedTime, " ns,",
          "Comunities generated in = ",comTime, " ns.")
    print(
        "----------------------------------------------------------------------------------------------------------------------\n")
def handleGraph(graph,benchmarkComm,spec):
    slpa = CommunityDiscovery_SLPA()
    resultCom,elaspedTime = slpa.slpaSingle(graph)
    mod=Modularity()
    modularityAcc = mod.modularityAccuarcy(graph,resultCom,graph,benchmarkComm)

    print("Node = ",spec[0])
    print("Tau1 = ",spec[1])
    print("Tau2 = ",spec[2])
    print("Mu   = ",spec[3])
    print("Result-- Modularity Accurarcy = ",modularityAcc, " Time Elapsed = ",elaspedTime," ns,",elaspedTime/1000_000_000," sec.")
    print("----------------------------------------------------------------------------------------------------------------------\n")


nodeLB = 1000
nodeChange = 100
nodeUB = 2500
tau1LB = 3
tau1Change = 0.1
tau1UB = 3.5
tau2LB = 1.5
tau2Change = 0.1
tau2UB = 1.5
muLB = 0.5
muChange = 0.1
muUB = 0.8
averageDegree= 5
minCommunity = 20
infoArray = [nodeLB,nodeChange,nodeUB,tau1LB,tau1Change,tau1UB,tau2LB,tau2Change,tau2UB,muLB,muChange,muUB,averageDegree,minCommunity]
graphGenerator = LFRGenerate()
g,com=t(nodeLB,tau1LB,tau2LB,muLB,average_degree=averageDegree,min_community=minCommunity)
print(g,com)
#arrays of graph based on change in single variable
nodeV,specs1 = graphGenerator.nodeChange(infoArray)
print("node done")
tau1V,specs2 = graphGenerator.tau1Change(infoArray)
print("tau1 done")
tau2V,specs3 = graphGenerator.tau2Change(infoArray)
print("tau2 done")
muV,specs4   = graphGenerator.muChange(infoArray)
print("mu done")


print("------Node Variance ( ",nodeLB," to ",nodeUB," )------- \n")
for (graph,spec) in zip(nodeV,specs1)  :
   applyingSLPA(graph,spec)
print("------Tau1 Variance ( ", tau1LB, " to ", tau1UB, " )------- \n")
for (graph,spec) in zip(tau1V,specs2)  :
   applyingSLPA(graph,spec)
print("------Tau2 Variance ( ", tau2LB, " to ", tau2UB, " )------- \n")
for (graph,  spec) in zip(tau2V,  specs3):
    applyingSLPA(graph,  spec)
print("------Mu Variance ( ", muLB, " to ", muUB, " )------- \n")
for (graph,spec) in zip(muV,specs4)  :
   applyingSLPA(graph,spec)


# print("------Node Variance ( ",nodeLB," to ",nodeUB," )------- \n")
# for (graph,comBench,spec) in zip(nodeV,comBench1,specs1)  :
#    handleGraph(graph,comBench,spec)
# print("------Tau1 Variance ( ", tau1LB, " to ", tau1UB, " )------- \n")
# for (graph,comBench,spec) in zip(tau1V,comBench2,specs2)  :
#    handleGraph(graph,comBench,spec)
# print("------Tau2 Variance ( ", tau2LB, " to ", tau2UB, " )------- \n")
# for (graph, comBench, spec) in zip(tau2V, comBench3, specs3):
#     handleGraph(graph, comBench, spec)
# print("------Mu Variance ( ", muLB, " to ", muUB, " )------- \n")
# for (graph,comBench,spec) in zip(muV,comBench4,specs4)  :
#    handleGraph(graph,comBench,spec)