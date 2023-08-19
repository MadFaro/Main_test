Collecting hydra
  Downloading Hydra-2.5.tar.gz (82 kB)
     ---------------------------------------- 82.4/82.4 kB 1.2 MB/s eta 0:00:00
  Preparing metadata (setup.py) ... done
Building wheels for collected packages: hydra
  Building wheel for hydra (setup.py) ... error
  error: subprocess-exited-with-error

  × python setup.py bdist_wheel did not run successfully.
  │ exit code: 1
  ╰─> [9 lines of output]
      running bdist_wheel
      running build
      running build_py
      creating build
      creating build\lib.win-amd64-cpython-38
      copying src\hydra.py -> build\lib.win-amd64-cpython-38
      running build_ext
      building '_hydra' extension
      error: Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/
      [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for hydra
  Running setup.py clean for hydra
Failed to build hydra
ERROR: Could not build wheels for hydra, which is required to install pyproject.toml-based projects

