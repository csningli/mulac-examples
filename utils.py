
import os, datetime, doctest

def get_current_time() :
    return datetime.datetime.now().strftime("%Y/%m/%d_%H:%M:%S.%f")

def get_datetime_stamp() :
    return datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

def dtest(topic = None) :
    result = doctest.testmod()
    print("-" * 50)
    print("[%s Test] attempted/failed tests: %d/%d" % (topic, result.attempted, result.failed))
