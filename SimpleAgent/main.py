
import os, math, functools

from mulac import *

class SimpleAgent(Agent) :
    def __init__(self, id) :
        super(SimpleAgent, self).__init__(id = id)
        self.done = False

    def process(self, msgs) :
        result = {"msgs" : []}
        if self.done == False :
            self.logger.log("agent %s done." % self.id)
            self.done = True
        elif self.id == "0" :
            result["msgs"].append(Message(src = self.id, dest = None, content = None))
        return result

if __name__ == "__main__" :
    agents = [SimpleAgent(id = str(i)) for i in range(5)]
    monitor = Monitor()
    print("Time cost: %s" % monitor.run(agents = agents, timeout = 1))
    combine_logs(logs = [monitor.logger.path] + [agent.logger.path for agent in agents],
        path = "logs/%s_combined_logs.log" % get_datetime_stamp())
