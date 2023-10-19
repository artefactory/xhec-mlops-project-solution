<div align="center">

# xhec-mlops-project-solution

[![CI status](https://github.com/artefactory/xhec-mlops-project-solution/actions/workflows/ci.yaml/badge.svg)](https://github.com/artefactory/xhec-mlops-project-solution/actions/workflows/ci.yaml?query=branch%3Amain)
[![Python Version](https://img.shields.io/badge/python-3.9%20%7C%203.10-blue.svg)]()

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Linting: ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-informational?logo=pre-commit&logoColor=white)](https://github.com/artefactory/xhec-mlops-project-solution/blob/main/.pre-commit-config.yaml)
</div>

This repository contains the solution for the X-HEC MLOps Project on the industrialization of [Abalone age prediction](https://www.kaggle.com/datasets/rodolfomendes/abalone-dataset) model.

## Table of Contents

- [xhec-mlops-project-solution](#xhec-mlops-project-solution)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Training the model](#training-the-model)

## Installation

Build the image docker with the following command:

```bash
docker build -t abalone:solution -f Dockerfile.app .
```

## Usage

1. Run the prediction API:

```bash
docker run -dp 0.0.0.0:8000:8001 abalone:solution
```

> [!NOTE]
> The `-d` flag is used to run the container in detached mode. The container will thus run in the background.

If you want to get the logs of the container, you can:

i. Get the container ID:

```bash
docker ps
```

ii. Copy/paste the container ID

iii. Get the logs:

```bash
docker logs <container_id> --follow
```

2. Go to http://localhost:8000/docs

3. In the /predict section, click on "Try it out".

4. Replace the Request body with the data of your choice.

Example:

```json
[
    {
        "sex": "M",
        "length": 0.455,
        "diameter": 0.365,
        "height": 0.095,
        "whole_weight": 0.514,
        "shucked_weight": 0.2245,
        "viscera_weight": 0.101,
        "shell_weight": 0.15
    },
    {
        "sex": "M",
        "length": 0.35,
        "diameter": 0.265,
        "height": 0.09,
        "whole_weight": 0.2255,
        "shucked_weight": 0.0995,
        "viscera_weight": 0.0485,
        "shell_weight": 0.07
    }
]
```

5. Click on "Execute" to get the prediction. You should get a 201 response with the prediction in the Response body, like this:

```json
{
  "predicted_abalone_ages": [
    9.28125,
    7.90625
  ]
}
```


6. When done with the API, you can stop the container with:

```bash
docker kill <container_id>
```

## Training the model

This repository comes with a pre-trained model and pre-fitted encoder (`src/web_service/local_objects`). If you want to train the model yourself, you can:

1. Install the dependencies in a virtual environment (python 3.9 or higher):

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

1. Put your data in the `data` folder. The data should be a CSV file with the same columns as the [Abalone dataset](https://www.kaggle.com/datasets/rodolfomendes/abalone-dataset).

2. Run the training script:

```bash
python3 src/modelling/main.py data/abalone.csv
```

This command will override the pre-trained model and encoder in the `src/web_service/local_objects` folder.

You can finally rebuild the docker image and run it again to use your new model.
