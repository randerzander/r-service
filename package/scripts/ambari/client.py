from resource_management import *
import ambari_helpers as helpers

class Client(Script):
  def install(self, env):
    # Install repos & packages listed in metainfo.xml
    helpers.add_repos()
    self.configure(env)

  def configure(self, env):
    import params
    env.set_params(params)

    self.install_packages(env)
    for command in params.commands: Execute(command)

  def status(self, env): raise ClientComponentHasNoStatus()

if __name__ == "__main__":
  Client().execute()
