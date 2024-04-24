C:\Users\TologonovAB\Desktop\Cython-0.29.32>Python setup.py install
Unable to find pgen, not compiling formal grammar.
C:\Users\TologonovAB\AppData\Local\Programs\Python\Python38\lib\site-packages\setuptools\config\__init__.py:28: SetuptoolsDeprecationWarning: As setuptools moves its configuration towards `pyproject.toml`,
`setuptools.config.parse_configuration` became deprecated.

For the time being, you can use the `setuptools.config.setupcfg` module
to access a backward compatible API, but this module is provisional
and might be removed in the future.

  warnings.warn(dedent(msg), SetuptoolsDeprecationWarning)
running install
running bdist_egg
running egg_info
writing Cython.egg-info\PKG-INFO
writing dependency_links to Cython.egg-info\dependency_links.txt
writing entry points to Cython.egg-info\entry_points.txt
writing top-level names to Cython.egg-info\top_level.txt
reading manifest file 'Cython.egg-info\SOURCES.txt'
reading manifest template 'MANIFEST.in'
warning: no files found matching 'Doc\*'
warning: no files found matching '*.pyx' under directory 'Cython\Debugger\Tests'
warning: no files found matching '*.pxd' under directory 'Cython\Debugger\Tests'
warning: no files found matching '*.pxd' under directory 'Cython\Utility'
warning: no files found matching 'pyximport\README'
writing manifest file 'Cython.egg-info\SOURCES.txt'
installing library code to build\bdist.win-amd64\egg
running install_lib
running build_py
running build_ext
building 'Cython.Plex.Scanners' extension
C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\14.31.31103\bin\HostX86\x64\cl.exe /c /nologo /Ox /W3 /GL /DNDEBUG /MD -IC:\Users\TologonovAB\AppData\Local\Programs\Python\Python38\include -IC:\Users\TologonovAB\AppData\Local\Programs\Python\Python38\include "-IC:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\14.31.31103\include" "-IC:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\VS\include" /TcC:\Users\TologonovAB\Desktop\Cython-0.29.32\Cython\Plex\Scanners.c /Fobuild\temp.win-amd64-3.8\Release\Users\TologonovAB\Desktop\Cython-0.29.32\Cython\Plex\Scanners.obj
Scanners.c
C:\Users\TologonovAB\AppData\Local\Programs\Python\Python38\include\pyconfig.h(59): fatal error C1083: Cannot open include file: 'io.h': No such file or directory
error: command 'C:\\Program Files (x86)\\Microsoft Visual Studio\\2022\\BuildTools\\VC\\Tools\\MSVC\\14.31.31103\\bin\\HostX86\\x64\\cl.exe' failed with exit status 2
