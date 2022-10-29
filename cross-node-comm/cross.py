
import os, sys, math, functools

from mulac import *

class CrossAgent(Agent) :
    def __init__(self, id, pub, sub) :
        super(CrossAgent, self).__init__(id = id, pub = pub, sub = sub)
        self.buffer = ["hi %d from %s" % (i, self.id) for i in range(5)] if self.pub is not None else []

    def process(self, msgs) :
        result = {'msgs' : []}
        if self.pub is not None and len(self.buffer) > 0 :
            content = self.buffer.pop()
            result['msgs'].append(Message(src = self.id, dest = self.pub, content = content))
            result['msgs'].append(Message(src = self.id, dest = None, topic = 'log', content = "agent %s (pub: %s, sub: %s)buffer: %s" % (self.id, self.pub, self.sub, self.buffer)))
        if self.sub is not None and len(msgs) > 0 :
            for msg in msgs :
                self.buffer.append(msg_to_raw(msg))
            result['msgs'].append(Message(src = self.id, dest = None, topic = 'log', content = "agent %s (pub: %s, sub: %s)buffer: %s" % (self.id, self.pub, self.sub, self.buffer)))
        return result

if __name__ == "__main__" :
    agents = [
        CrossAgent(id = sys.argv[1], pub = sys.argv[3], sub = None),
        CrossAgent(id = sys.argv[2], pub = None, sub = sys.argv[4]),
    ]
    monitor = ProcessMonitor(path = 'logs/%s.log' % get_datetime_stamp())
    print("\nTime cost: %s" % monitor.run(agents = agents, timeout = 3))
