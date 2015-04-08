#!/usr/bin/env python
import os
from resource_management.libraries.functions.version import format_hdp_stack_version, compare_versions
from resource_management import *

# server configurations
config = Script.get_config()

r_libs = filter(lambda x: len(x.strip()) > 0, config['configurations']['r-config']['r.libs'].split(','))
r_repo_url = config['configurations']['r-config']['r.repo_url']

package_dir = os.path.realpath(__file__).split('/package')[0]
files_dir = package_dir + '/package/files/'
scripts_dir = package_dir + '/package/scripts/'
repo_dir = files_dir+'/repos/'

r_libs_dir = '/usr/lib64/R/library/'

#TODO: make dynamic based on OS
distribution = platform.linux_distribution()[0].lower()
if distribution in ['centos', 'redhat'] :
  repo_dir += 'rhel6'
  os_repo_dir = '/etc/yum.repos.d/'

commands = []
commands.append('sh ' + scripts_dir + 'r_lib_setup.sh ' + files_dir + ' ' + scripts_dir + ' ' + r_libs_dir)

for lib in r_libs:
  command = ' '.join(['sh', scripts_dir+'r_lib_install.sh', files_dir, lib, r_libs_dir, r_repo_url])
  commands.append(command)
