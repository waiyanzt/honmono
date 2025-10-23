{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    (python311.withPackages (ps: with ps; [
      pandas
      numpy
      matplotlib
      scikit-learn
      jupyter
    ]))
    git
  ];

  shellHook = ''
    echo "========================================="
    echo "Project honmono(fake news classifier env)"
    echo "========================================="
    echo "Python: $(python --version)"
    echo ""
    echo "Available packages:"
    echo "  - pandas, numpy, matplotlib"
    echo "  - scikit-learn, jupyter"
    echo ""
    echo "Quick start:"
    echo "  1. Download dataset: kaggle datasets download -d <dataset-name>"
    echo "  2. Run: python src/load_data.py"
    echo "========================================="
  '';
}
