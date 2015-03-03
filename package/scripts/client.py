import sys, os
from resource_management import *

class Client(Script):
  def install(self, env):
    self.configure(env)
    import params

    # Get binaries from HDFS
    Execute('mkdir -p ' + params.root_dir)
    Execute('rm -rf ' + params.root_dir + '/*')
    prefix='cd ' + params.root_dir + '; export HADOOP_CMD=/usr/bin/hadoop; export HADOOP_STREAMING=/usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar; '
    Execute(prefix+'hadoop fs -get /apps/r/* .')

    # Install packages listed in metainfo.xml
    if not os.path.exists('/etc/yum.repos.d/epel.repo'): Execute(prefix+'mv resources/epel.repo /etc/yum.repos.d/')
    self.install_packages(env)

    # Install R libs
    Execute(prefix+'tar -xzvf resources/library.tgz')
    Execute(prefix+'cp -r library /usr/lib64/R/')
    #Execute('rm -rf /usr/lib64/R/library')
    #Execute(prefix+'mv library /usr/lib64/R/')
 
    # Most libs come pre-built. Upgrade and/or install additional usr R packages
    for rlib in params.r_libs: 
      if not os.path.exists('/usr/lib64/R/library/'+rlib): 
        Execute("Rscript -e 'install.packages(c(\""+rlib+"\"), repos=\"http://cran.us.r-project.org\");'")

    # Install R Hadoop packages
    #TODO: Pre-install & configure RHBase, and RHive
    Execute(prefix+'R CMD INSTALL resources/rmr2_3.3.0.tar')
    Execute(prefix+'R CMD INSTALL resources/rhdfs_1.0.8.tar.gz')
    Execute(prefix+'R CMD INSTALL resources/plyrmr_0.5.0.tar.gz')
    Execute(prefix+'R CMD javareconf -e')

  def configure(self, env):
    import params
    env.set_params(params)

  def status(self, env): raise ClientComponentHasNoStatus()

if __name__ == "__main__":
  Client().execute()
