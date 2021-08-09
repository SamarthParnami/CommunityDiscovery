from networkx.generators.community import LFR_benchmark_graph

class LFRGenerate:

    def nodeChange(self,infoArray):
        #infoArray has a build of [nodeLB,nodeChange,nodeUB , tau1LB,tau1Change,tau1UB, tau2LB,tau2Change,tau2UB,  muLB,muChange,muUB ,averageDegree, minCommunity]
        graph=[]
        nodeLB=infoArray[0]
        nodeUB=infoArray[2]
        node_change=infoArray[1]
        tau1=infoArray[3]
        tau2=infoArray[6]
        mu=infoArray[9]
        averageDegree=infoArray[12]
        minCommunity=infoArray[13]
        while nodeLB<=nodeUB:
            graph.append(LFR_benchmark_graph(nodeLB,tau1,tau2,mu,averageDegree,minCommunity))
            nodeLB+=node_change
        return graph
    def tau1Change(self,infoArray):
        #infoArray has a build of [nodeLB,nodeChange,nodeUB , tau1LB,tau1Change,tau1UB, tau2LB,tau2Change,tau2UB,  muLB,muChange,muUB ,averageDegree, minCommunity]
        graph=[]
        nodeLB=infoArray[0]

        tau1LB=infoArray[3]
        tau1UB=infoArray[5]
        tau1_change=infoArray[4]
        tau2=infoArray[6]
        mu=infoArray[9]
        averageDegree=infoArray[12]
        minCommunity=infoArray[13]
        while tau1LB<=tau1UB:
            graph.append(LFR_benchmark_graph(nodeLB,tau1LB,tau2,mu,averageDegree,minCommunity))
            tau1LB+=tau1_change
        return graph
    def tau2Change(self,infoArray):
        #infoArray has a build of [nodeLB,nodeChange,nodeUB , tau1LB,tau1Change,tau1UB, tau2LB,tau2Change,tau2UB,  muLB,muChange,muUB ,averageDegree, minCommunity]
        graph=[]
        nodeLB=infoArray[0]

        tau1LB=infoArray[3]

        tau2LB=infoArray[6]
        tau2UB = infoArray[8]
        tau2_change = infoArray[7]
        mu=infoArray[9]
        averageDegree=infoArray[12]
        minCommunity=infoArray[13]
        while tau2LB<=tau2UB:
            graph.append(LFR_benchmark_graph(nodeLB,tau1LB,tau2LB,mu,averageDegree,minCommunity))
            tau2LB+=tau2_change
        return graph
    def muChange(self, infoArray):
        # infoArray has a build of [nodeLB,nodeChange,nodeUB , tau1LB,tau1Change,tau1UB, tau2LB,tau2Change,tau2UB,  muLB,muChange,muUB ,averageDegree, minCommunity]
        graph = []
        nodeLB = infoArray[0]
        tau1LB = infoArray[3]
        tau2LB = infoArray[6]

        muLB = infoArray[9]
        muUB = infoArray[11]
        mu_change = infoArray[10]
        averageDegree = infoArray[12]
        minCommunity = infoArray[13]
        while muLB <= muUB:
            graph.append(LFR_benchmark_graph(nodeLB, tau1LB, tau2LB, muLB, averageDegree, minCommunity))
            muLB += mu_change
        return graph
    def Graph(self,infoArray):
        node=infoArray[0]
        tau1=infoArray[3]
        tau2=infoArray[6]
        mu=infoArray[9]
        averageDegree=infoArray[12]
        minCommunity=infoArray[13]
        return LFR_benchmark_graph(node,tau1,tau2,mu,averageDegree,minCommunity)