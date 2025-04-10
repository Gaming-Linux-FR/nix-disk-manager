subdir('dialogs')
subdir('utils')
subdir('views')
subdir('widgets')
subdir('cli')

moduledir = 'nixdiskmanager'

sources = [
  '__init__.py',
  'main.py',
]

configure_file(
  input: 'constants.py.in',
  output: 'constants.py',
  configuration: conf,
  install_dir: PY_INSTALLDIR.get_install_dir() / moduledir
)

PY_INSTALLDIR.install_sources(sources, subdir: moduledir)

configure_file(
  input: 'nix-disk-manager.in',
  output: 'nix-disk-manager',
  configuration: conf,
  install_dir: get_option('bindir')
)
