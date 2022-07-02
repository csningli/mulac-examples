
import os, math, functools

from mcf.agent import *
from mcf.utils import get_datetime_stamp, combine_logs

class Task(object) :
    def __init__(self, count = 0) :
        self.count = count

    def step(self) :
        if self.count > 0 :
            self.count -= 1
        return self.count < 1

class SlaveAgent(Agent) :
    def __init__(self, id, master_id, task) :
        super(SlaveAgent, self).__init__(id = id)
        self.master_id = master_id
        self.task = task

    def process(self, msgs) :
        result = {"msgs" : []}
        if self.task.step() == True :
            result["msgs"].append(Message(src = self.id, dest = self.master_id, content = "done"))
        return result

class MasterAgent(Agent) :
    def __init__(self, id, slave_ids) :
        super(MasterAgent, self).__init__(id = id)
        self.status = {id : False for id in slave_ids}

    def process(self, msgs) :
        result = {"msgs" : []}
        for msg in msgs :
            if msg.dest == self.id and msg.content == "done" :
                self.status[msg.src] = True
        if False not in list(self.status.keys()) :
            result["msgs"].append(Message(src = self.id, dest = None, content = None))
        return result

if __name__ == "__main__" :
    agents = [MasterAgent(id = 0, slave_ids = list(range(1, 5))), ] + [SlaveAgent(id = i, master_id = 0, task = Task(count = i * 10)) for i in range(1, 5)]
    monitor = Monitor()
    print("Time cost: %s" % monitor.run(agents = agents, timeout = 1))
    combine_logs(logs = [monitor.logger.path] + [agent.logger.path for agent in agents],
        path = "logs/%s_combined_logs.log" % get_datetime_stamp())
