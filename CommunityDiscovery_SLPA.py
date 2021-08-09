from cdlib import algorithms
from Stopwatch import *
class CommunityDiscovery_SLPA:
    def __init__(self):
        self.watch=Stopwatch()
    def slpaSingle(self,graph,itr=20,mu=0.2):
        self.watch.start()
        com=algorithms.slpa(graph,itr,mu)
        self.watch.stop()
        return com,self.watch.elapsed()
    def slpaArray(self,graph,itr=20,mu=0.2):
        com= []
        elapsedTimes=[]
        for g in graph:
            self.watch.reset()
            community,elapse =self.slpaSingle(g,itr,mu)
            com.append(community)
            elapsedTimes.append(elapse)
        return com,elapsedTimes
