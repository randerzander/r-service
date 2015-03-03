Sys.setenv(HADOOP_STREAMING="/usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar")
Sys.setenv(HADOOP_CMD="/usr/bin/hadoop")

groups = rbinom(100, n = 500, prob = 0.5)
tapply(groups, groups, length)

require('rmr2')
groups = rbinom(100, n = 500, prob = 0.5)
groups = to.dfs(groups)
result = mapreduce(input = groups, map = function(k,v) keyval(v, 1), reduce = function(k,vv) keyval(k,length(vv)))
print(result())
print(from.dfs(result))
