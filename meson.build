project('nix-disk-manager', 'c')

python = import('python')
gnome = import('gnome')

bindir = get_option('prefix') / get_option('bindir')
datadir = get_option('prefix') / get_option('datadir')
pkgdatadir = datadir / meson.project_name()
srcdir = pkgdatadir / 'src'

conf = configuration_data()
conf.set('PKGDATA_DIR', pkgdatadir)
conf.set('BINDIR', bindir)
conf.set('ROOT_DIR', get_option('prefix'))
conf.set('DATA_DIR', join_paths(get_option('prefix'), get_option('datadir')))
conf.set('LOCALE_DIR', join_paths(get_option('prefix'), get_option('localedir')))
conf.set('LOGOIMAGE', datadir / 'icons' / 'hicolor' / '128x128' / 'apps' / 'nix-disk-manager.png')

PY_INSTALLDIR = python.find_installation('python3', required: true, modules: ['gi'])

conf.set('PYTHON_BIN', PY_INSTALLDIR.full_path())

subdir('nixdiskmanager')
subdir('po')
subdir('data')
