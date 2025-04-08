subdir('ui')
subdir('icons')

gnome = import('gnome')

gnome.compile_resources(
    'nix-disk-manager', 'nix-disk-manager.gresource.xml',
    gresource_bundle: true,
    dependencies: blueprints,
    install: true,
    install_dir: pkgdatadir
)

configure_file(
  input: 'org.glfos.nixdiskmanager.in',
  output: 'org.glfos.nixdiskmanager.policy',
  configuration: conf,
  install_dir: datadir / 'polkit-1' / 'actions'
)

configure_file(
  input: 'nix-disk-manager.desktop.in',
  output: 'nix-disk-manager.desktop',
  configuration: conf,
  install_dir: datadir / 'applications'
)