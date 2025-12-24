from src.Wine_Quality_Prediction.config.configuration import ConfigurationManager
from src.Wine_Quality_Prediction.components.model_evaluation import Modelevaluation
from src.Wine_Quality_Prediction import logger
from pathlib import Path
import dagshub
import mlflow

STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        dagshub.init(repo_owner='XuanHoangee2', repo_name='Wine-Quality-Prediction', mlflow=True)
        config= ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = Modelevaluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e