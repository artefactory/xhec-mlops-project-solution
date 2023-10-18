#!/bin/bash -e

read -p "Want to install conda env named 'xhec-mlops-project-solution'? (y/n)" answer
if [ "$answer" = "y" ]; then
  echo "Installing conda env..."
  conda create -n xhec-mlops-project-solution python=3.10 -y
  source $(conda info --base)/etc/profile.d/conda.sh
  conda activate xhec-mlops-project-solution
  echo "Installing requirements..."
  pip install -r requirements-developer.txt
  python3 -m ipykernel install --user --name=xhec-mlops-project-solution
  conda install -c conda-forge --name xhec-mlops-project-solution notebook -y
  echo "Installing pre-commit..."
  make install_precommit
  echo "Installation complete!";
else
  echo "Installation of conda env aborted!";
fi
