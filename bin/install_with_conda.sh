#!/bin/bash -e

read -p "Want to install conda env named 'xhec-mlops-crashcourse-2023-project'? (y/n)" answer
if [ "$answer" = "y" ]; then
  echo "Installing conda env..."
  conda create -n xhec-mlops-crashcourse-2023-project python=3.10 -y
  source $(conda info --base)/etc/profile.d/conda.sh
  conda activate xhec-mlops-crashcourse-2023-project
  echo "Installing requirements..."
  pip install -r requirements-developer.txt
  python3 -m ipykernel install --user --name=xhec-mlops-crashcourse-2023-project
  conda install -c conda-forge --name xhec-mlops-crashcourse-2023-project notebook -y
  echo "Installing pre-commit..."
  make install_precommit
  echo "Installation complete!";
else
  echo "Installation of conda env aborted!";
fi
