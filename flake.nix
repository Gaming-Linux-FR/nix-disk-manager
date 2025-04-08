{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-24.11";
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
          packages = rec {
            nix-disk-manager = pkgs.callPackage ./package.nix {nix-disk-manager = nix-disk-manager.packages.${system}.default; };
            default = nix-disk-manager;
          };
          devShells.default = mkShell {
            buildInputs = with pkgs; [
              blueprint-compiler
              meson
              ninja
              libadwaita
              adwaita-icon-theme
              gtk4
              librsvg
              (pkgs.python3.withPackages (python-pkgs: [
                python-pkgs.pygobject3
                python-pkgs.pip
              ]))
            ];
          };
        }
      );
}
