import os
from resource_management import *

def add_repos(repo_dir, install_dir):
  for repo in os.listdir(repo_dir):
    add_repo(repo_dir, repo, install_dir)

def add_repo(repo_dir, repo, install_dir):
  if not os.path.isfile(install_dir + repo):
    Execute('cp ' + repo_dir + repo + ' ' + install_dir)
