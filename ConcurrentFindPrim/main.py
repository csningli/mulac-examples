
import os, math, functools
from multiprocessing import current_process

from mcf.agent import *
from mcf.utils import get_datetime_stamp, combine_logs
from examples.CosFindPrim.main import is_prim

class PrimAgent(ConcurrentAgent) :
    def __init__(self, id, pop) :
        super(PrimAgent, self).__init__(id = id, pop = pop)
        self.nums = [[int(self.id) * 100 + j * 10 + i for i in range(10)] for j in range(self.pop)]
        self.found = [[] for j in range(self.pop)]

    def process(self, msgs) :
        result = super(PrimAgent, self).process(msgs = msgs)
        self.logger.log("Found %s." % self.found)
        return result

    def thread_task(self, index, round) :
        if round >= 0 and round < len(self.nums[index]) :
            if is_prim(self.nums[index][round]) :
                self.found[index].append(self.nums[index][round])
        print("worker at process: %s" % current_process().pid)

if __name__ == "__main__" :
    agents = [ThreadPrimAgent(id = "0", pop = 10), ThreadPrimAgent(id = "1", pop = 10)]
    monitor = Monitor()
    print("Time cost: %s" % monitor.run(agents = agents, timeout = 3))
    combine_logs(logs = [monitor.logger.path] + [agent.logger.path for agent in agents],
        path = "logs/%s_combined_logs.log" % get_datetime_stamp())
