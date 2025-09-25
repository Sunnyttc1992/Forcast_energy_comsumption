#!/bin/bash
set -ex

# Install build tools and libraries commonly required to build ML packages
# Works on Amazon Linux 2 platform
if command -v yum >/dev/null 2>&1; then
  yum -y update || true
  yum -y install gcc gcc-c++ make python3-devel openblas-devel lapack-devel libgomp || true
fi

# Upgrade pip tools in the instance Python environment
python3 -m pip install --upgrade pip setuptools wheel || true

# Clean package manager caches and tmp to reduce disk usage
yum clean all || true
rm -rf /tmp/* || true
