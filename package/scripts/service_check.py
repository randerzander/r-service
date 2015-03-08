#!/usr/bin/env python
from __future__ import print_function
from resource_management import *
import  sys,subprocess,os

class ServiceCheck(Script):
    def service_check(self, env):
        import params
        env.set_params(params)
        prefix='export HADOOP_CMD=/usr/bin/hadoop; export HADOOP_STREAMING=/usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar; '
        Execute('R --file=' + params.scripts_dir + 'smoke_test.r', user='ambari-qa')

if __name__ == "__main__":
    ServiceCheck().execute()
