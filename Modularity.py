from cdlib import evaluation
from Stopwatch import *
from math import fabs


class Modularity:
    def __init__(self):
        self.watch = Stopwatch()
        self.elapsed_time = None
    def modularityOverlap(self,graph,nodeCliuster):
        self.watch.start()
        fitness = evaluation.modularity_overlap(graph, nodeCliuster)
        self.elapsed_time=self.watch.stop()
        return fitness
    def elapsedTime(self):
        if self.elapsed_time is None :
            raise TrackingError("Use a modularity function before tracking time taken by the function.")
        return self.elapsed_time
    def modularityChange(self,score1,score2):
        return fabs(score1.score-score2.score)
    def modularityAccuarcy(self,graph1,com1,graph2,com2):
        score1 = self.modularityOverlap(graph1, com1)
        score2 = self.modularityOverlap(graph2, com2)
        return 1-self.modularityChange(score1,score2)/score2.score