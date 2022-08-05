import mlflow
import os
#from tqdm import tqdm
import logging


import sys
sys.path.append('../')
from src.utils.common import read_yaml, create_directories

STAGE = "MAIN" ## <<< change stage name 

logging.basicConfig(
    filename=os.path.join("../logs", 'running_logs.log'), 
    level=logging.INFO, 
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a"
    )


def main():
    with mlflow.start_run() as run:
        mlflow.run(".","get_data",use_conda=False)
        mlflow.run(".","base_model_creation",use_conda=False)



if __name__ == '__main__':
    try:
        logging.info("\n********************")
        logging.info(f">>>>> stage {STAGE} started <<<<<")
        main()
        logging.info(f">>>>> stage {STAGE} completed!<<<<<\n")
    except Exception as e:
        logging.exception(e)
        raise e