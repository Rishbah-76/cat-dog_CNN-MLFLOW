# MLflow-project-template
Cat and Dog classification Project with MLflow for automataion as a part of AIops

## STEPS -

### STEP 01- Create a repository by using template repository

### STEP 02- Clone the new repository

### STEP 03- Create a conda environment after opening the repository in VSCODE

```bash
conda create --prefix ./env python=3.7 -y
```

```bash
conda activate ./env
```
OR
```bash
source activate ./env
```

### STEP 04- install the requirements
```bash
pip install -r requirements.txt
```

### STEP 05 - Create conda.yaml file -
```bash
conda env export > conda.yaml
```

### STEP 06- commit and push the changes to the remote repository</br></br>

## MLFLOW Commands

### command to run the MLflow project file
```bash
mlflow run . --env-manager=local
```

### Run any specific entry point in MLProject file 
```bash
mlflow run . -e get_data --env-manager=local
```
### Run MLflow project file with diffrent config file
```bash
mlflow run . -e __yourentrypoint__ -P config=configs/__yourconfig.yaml --env-manager=local
```
