set -eu

FILES_DIR=$1
SCRIPTS_DIR=$2
R_LIBS_DIR=$3

export HADOOP_CMD=/usr/bin/hadoop
export HADOOP_STREAMING=/usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar

R CMD INSTALL $FILES_DIR/rmr2_3.3.0.tar
R CMD INSTALL $FILES_DIR/rhdfs_1.0.8.tar.gz
R CMD INSTALL $FILES_DIR/plyrmr_0.5.0.tar.gz

for filename in $FILES_DIR/libs/*.tgz
do
  tar -xzvf $filename -C $R_LIBS_DIR
done
