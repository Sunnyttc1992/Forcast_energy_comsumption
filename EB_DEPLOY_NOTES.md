Why we added prebuild hooks and updated .ebextensions/python.config

- Problem observed: pip failed during deployment with "No space left on device" and failed to install dependencies.
- Changes made:
  - `.ebextensions/python.config` now upgrades pip/setuptools/wheel and installs requirements using `--no-cache-dir` to avoid filling disk with wheel caches.
  - Added container cleanup commands to clean yum caches and /tmp.
  - Added `.platform/hooks/prebuild/01_install_build_deps.sh` to install native build tools (gcc, g++, make, python3-devel, openblas-devel, lapack-devel, libgomp) and to clean caches.

Next steps for deployment:
1. Re-deploy the application (create a new application version and deploy). This should fix pip install failures caused by missing build tools or lack of disk space.
2. If deployment still fails, fetch `eb-engine.log` and `eb-activity.log` from the instance (Elastic Beanstalk console -> Logs -> Request full logs) and paste the first 200 lines here for analysis.
