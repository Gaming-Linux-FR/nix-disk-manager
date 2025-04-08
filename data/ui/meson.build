blueprints = custom_target('blueprints',
  input: files(
    'disk.blp',
    'disks.blp',
    'manage_disk_add_mount_row.blp',
    'manage_disk_mount_expander.blp',
    'manage_disk_mount_row.blp',
    'manage_disk.blp',
    'save_dialog.blp',
    'window.blp',
    'welcome_dialog.blp'
  ),
  output: '.',
  command: [find_program('blueprint-compiler'), 'batch-compile', '@OUTPUT@', '@CURRENT_SOURCE_DIR@', '@INPUT@'],
)
