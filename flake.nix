{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };
  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem
      (system:
        let
          pkgs = import nixpkgs {
            inherit system;
          };
        in
        with pkgs;
        {
          devShells.default = mkShell {
            buildInputs = [
              pkgs.gtk4
              pkgs.blueprint-compiler
              pkgs.gobject-introspection
              pkgs.libadwaita
              (pkgs.python3.withPackages (python-pkgs: [
                python-pkgs.pygobject3
              ]))
            ];
          };
        }
      );
}
