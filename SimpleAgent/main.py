
import os, math, functools

from mulac import *

class SimpleAgent(Agent) :
    def __init__(self, id, mark = '0') :
        super(SimpleAgent, self).__init__(id = id)
        self.mark = mark
        self.done = False

    def process(self, msgs) :
        result = {'msgs' : []}
        if self.done == False :
            self.logger.log('agent %s done.' % self.id)
            self.done = True
        elif self.id == self.mark :
            result['msgs'].append(Message(src = self.id, dest = None, content = None))
        return result

if __name__ == "__main__" :
    n = 5
    agents = [SimpleAgent(id = str(i), mark = str(n - 1)) for i in range(n)]
    monitor = ProcessMonitor()
    print("Time cost [Process Monitor]: %s" % monitor.run(agents = agents, timeout = 2))
    monitor = ThreadMonitor()
    print("Time cost [Thread Monitor]: %s" % monitor.run(agents = agents, timeout = 2))
