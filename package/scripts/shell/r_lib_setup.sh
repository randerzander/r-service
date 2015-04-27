set -eu

FILES_DIR=$1
SCRIPTS_DIR=$2
R_LIBS_DIR=$3

export HADOOP_CMD=/usr/bin/hadoop
export HADOOP_STREAMING=/usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar

for filename in $FILES_DIR/libs/*.tgz
do
  tar -xzvf $filename -C $R_LIBS_DIR
done
