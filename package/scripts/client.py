import sys, os
import ambari_helpers as helpers
from resource_management import *

class Client(Script):
  def install(self, env):
    self.configure(env)
    import params

    # Install repos & packages listed in metainfo.xml
    helpers.add_repos(params.repo_dir, params.os_repo_dir)
    self.install_packages(env)

    for command in params.commands: Execute(command)

  def configure(self, env):
    import params
    env.set_params(params)

  def status(self, env): raise ClientComponentHasNoStatus()

if __name__ == "__main__":
  Client().execute()
