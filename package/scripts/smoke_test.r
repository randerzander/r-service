Sys.setenv(HADOOP_STREAMING="/usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar")
Sys.setenv(HADOOP_CMD="/usr/bin/hadoop")

require('rmr2')
rmr.options (
   backend.parameters = list (
     hadoop = list (
       D = "mapreduce.map.java.opts=-Xmx800M",
       D = "mapreduce.reduce.java.opts=-Xmx800M",
       D = "mapreduce.map.memory.mb=4096",
       D = "mapreduce.reduce.memory.mb=4096",
       D = "mapreduce.task.io.sort.mb=64"
     )
   )
)

groups = rbinom(100, n = 500, prob = 0.5)
tapply(groups, groups, length)

groups = rbinom(100, n = 500, prob = 0.5)
groups = to.dfs(groups)
result = mapreduce(input = groups, map = function(k,v) keyval(v, 1), reduce = function(k,vv) keyval(k,length(vv)))
print(result())
print(from.dfs(result))
