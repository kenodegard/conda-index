# normally run with "conda index" or bin/conda-index
# CONDA_DEBUG=1 python -m conda_build index --verbose ...
import logging

from . import logutil

# sets up timestamped log lines nicely but can conflict with conda logging by
# printing messages twice
# conda resets logging on each subdir
logutil.configure()
logging.getLogger("conda_build.index").setLevel(logging.DEBUG)
import conda_build.cli.main_index  # must import *after* logging config

# assert that filtering is happening; remove conda DuplicateFilter
assert len(logging.getLogger("conda_build.index").filters)
logging.getLogger("conda_build.index").filters = []
conda_build.cli.main_index.main()