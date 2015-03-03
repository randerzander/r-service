#!/usr/bin/env python
from resource_management.libraries.functions.version import format_hdp_stack_version, compare_versions
from resource_management import *

# server configurations
config = Script.get_config()

root_dir =  '/r/scratch'
r_libs = filter(lambda x: len(x.strip()) > 0, config['configurations']['r-config']['r.libs'].split(','))
