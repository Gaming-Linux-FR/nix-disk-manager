#!/usr/bin/env python3

import subprocess, sys, os

def mkdir(path):
    os.makedirs(path, exist_ok=True)

def write_nix_config_from_tmp(config_path, nix_config_path):
    nix_config = open(nix_config_path, 'w')
    tmp_config = open(config_path, 'r')
    
    nix_config.write(tmp_config.read())
    
    tmp_config.close()
    nix_config.close()

def rebuild_config(rebuild_cmd):
    return subprocess.call(rebuild_cmd, shell=True)

def write_and_rebuild(config_path, nix_path, rebuild_cmd):
    write_nix_config_from_tmp(config_path, nix_path)
    return rebuild_config(rebuild_cmd)

if __name__ == '__main__':
    print(sys.argv)
    match sys.argv[1]:
        case 'write':
            config_path = sys.argv[2]
            nix_config_path = sys.argv[3]
            rebuild_cmd = sys.argv[4]

            sys.exit(write_and_rebuild(config_path, nix_config_path, rebuild_cmd))

        case 'mkdir':
            mkdir(sys.argv[2])