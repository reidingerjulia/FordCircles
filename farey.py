import math
import itertools

class Farey:

    ord = 3 #order of farey sequence

    p = [0,1] #p_i
    q = [1] #q_i Nenner
    seq = []



    def __init__(self, ord):
        assert ord > 2
        self.ord = ord
        self.q.append(ord)

        #generate elements
        while self.p[-1]/self.q[-1] != 1:
            coeff = math.floor((self.q[-2]+ord)/self.q[-1])
            p = coeff*self.p[-1]-self.p[-2]
            q = coeff*self.q[-1] - self.q[-2]
            self.p.append(p)
            self.q.append(q)

        def take_radius(elem):
            return round(1 / (2 * elem[1] * elem[1]),4)

        self.seq = list(zip(self.p,self.q))
        self.seq.sort(key=take_radius)
        self.seq = [(k, list(g)) for k, g in itertools.groupby(self.seq, take_radius)]


    def print(self):
        for i in range(len(self.p)):
            print(f"({self.p[i]},{self.q[i]})")

