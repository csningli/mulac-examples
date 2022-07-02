
import os, sys, math, functools, psutil
from examples.CrossNode.cross import *

if __name__ == "__main__" :
    agents = [
        CrossSubAgent(id = "0", bb = Backbone("examples/CrossNode/bb.json")),
        CrossPubAgent(id = "2", bb = Backbone("examples/CrossNode/bb.json")),
    ]
    monitor = Monitor()
    print("\nTime cost: %s" % monitor.run(agents = agents, timeout = 5))
    combine_logs(logs = [monitor.logger.path] + [agent.logger.path for agent in agents],
        path = "logs/%s_combined_logs.log" % get_datetime_stamp())
