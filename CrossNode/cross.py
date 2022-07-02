
import os, sys, math, functools, psutil

from mcf.agent import *
from mcf.comp import *
from mcf.utils import get_datetime_stamp, combine_logs

class CrossPubAgent(PubAgent) :
    def __init__(self, id, bb) :
        super(CrossPubAgent, self).__init__(id = id, bb = bb)
        self.initialized = False

    def process(self, msgs) :
        if self.initialized == False :
            dest = "0" if self.id == "3" else "1"
            for i in range(5) :
                msgs.append(Message(src = "-1", dest = self.id, topic = "zero", content = "-1/%s/zero/message %s from -1." % (dest, i)))
            self.initialized = True
        for raw, stamp in self.buffer :
            self.logger.log("agent %s buffer message: %s (%s)." % (self.id, raw, stamp))
        result = super(CrossPubAgent, self).process(msgs = msgs)
        return result

class CrossSubAgent(SubAgent) :
    def __init__(self, id, bb) :
        super(CrossSubAgent, self).__init__(id = id, bb = bb)

    def process(self, msgs) :
        result = super(CrossSubAgent, self).process(msgs = msgs)
        for msg in result.get("msgs", []) :
            self.logger.log("agent %s receive message %s/%s/%s." % (self.id, msg.src, msg.dest, msg.content))
        return result
