
from math import floor

from cdlib.benchmark import LFR as gen

class LFRGenerate:
    def nodeChange(self, infoArray):
        # infoArray has a build of [nodeLB,nodeChange,nodeUB , tau1LB,tau1Change,tau1UB, tau2LB,tau2Change,tau2UB,  muLB,muChange,muUB ,averageDegree, minCommunity]
        graphs = []
        communities=[]
        specifications = []
        nodeLB = infoArray[0]
        nodeUB = infoArray[2]
        node_change = infoArray[1]
        tau1 = infoArray[3]
        tau2 = infoArray[6]
        mu = infoArray[9]

        print("here")
        while nodeLB <= nodeUB:

            averageDegree = nodeLB/50#infoArray[12]
            minCommunity = floor(nodeLB/12.5)#infoArray[13]
            g,com,specs=self.Graph(nodeLB,tau1,tau2,mu,averageDegree,minCommunity)
            graphs.append(g)
            communities.append(com)
            specifications.append(specs)
            nodeLB += node_change
        return graphs,communities,specifications

    def tau1Change(self, infoArray):
        # infoArray has a build of [nodeLB,nodeChange,nodeUB , tau1LB,tau1Change,tau1UB, tau2LB,tau2Change,tau2UB,  muLB,muChange,muUB ,averageDegree, minCommunity]
        graphs = []
        communities=[]
        specifications = []
        nodeLB = infoArray[0]

        tau1LB = infoArray[3]
        tau1UB = infoArray[5]
        tau1_change = infoArray[4]
        tau2 = infoArray[6]
        mu = infoArray[9]

        while tau1LB <= tau1UB:
            averageDegree = nodeLB / 50  # infoArray[12]
            minCommunity = floor(nodeLB / 12.5)  # infoArray[13]
            g,com,specs=self.Graph(nodeLB,tau1LB,tau2,mu,averageDegree,minCommunity)
            graphs.append(g)
            communities.append(com)
            specifications.append(specs)
            tau1LB += tau1_change
        return graphs,communities,specifications

    def tau2Change(self, infoArray):
        # infoArray has a build of [nodeLB,nodeChange,nodeUB , tau1LB,tau1Change,tau1UB, tau2LB,tau2Change,tau2UB,  muLB,muChange,muUB ,averageDegree, minCommunity]
        graphs = []
        communities = []
        specifications= []
        nodeLB = infoArray[0]

        tau1LB = infoArray[3]

        tau2LB = infoArray[6]
        tau2UB = infoArray[8]
        tau2_change = infoArray[7]
        mu = infoArray[9]

        while tau2LB <= tau2UB:
            averageDegree = nodeLB / 50  # infoArray[12]
            minCommunity = floor(nodeLB / 12.5)  # infoArray[13]
            g, com, specs = self.Graph(nodeLB, tau1LB, tau2LB, mu, averageDegree, minCommunity)
            graphs.append(g)
            communities.append(com)
            specifications.append(specs)
            tau2LB += tau2_change
        return graphs,communities,specifications

    def muChange(self, infoArray):
        # infoArray has a build of [nodeLB,nodeChange,nodeUB , tau1LB,tau1Change,tau1UB, tau2LB,tau2Change,tau2UB,  muLB,muChange,muUB ,averageDegree, minCommunity]
        graphs = []
        communities = []
        specifications = []
        nodeLB = infoArray[0]
        tau1LB = infoArray[3]
        tau2LB = infoArray[6]

        muLB = infoArray[9]
        muUB = infoArray[11]
        mu_change = infoArray[10]

        while muLB <= muUB:
            averageDegree = nodeLB / 50  # infoArray[12]
            minCommunity = floor(nodeLB / 12.5)  # infoArray[13]
            g, com, specs = self.Graph(nodeLB, tau1LB, tau2LB, muLB, averageDegree, minCommunity)
            graphs.append(g)
            communities.append(com)
            specifications.append(specs)
            muLB += mu_change
        return graphs,communities,specifications

    def Graph(self,node,tau1,tau2,mu,averageDegree,minCommunity):
        print("Generating Graph with specs ",node,tau1,tau2,mu,averageDegree,minCommunity)
        g,coms=gen(node, tau1, tau2, mu, average_degree=averageDegree, min_community=minCommunity,max_iters=500)
        print("Graph generated.")
        return g,coms,[node,tau1,tau2,mu]
