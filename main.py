from Wine_Quality_Prediction.pipeline.stage_1_data_ingestion import DataIngestionPipeline
from Wine_Quality_Prediction.pipeline.stage_2_data_validation import DataValidationPipeline
from Wine_Quality_Prediction import logger

STAGE_NAME_1 = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> Stage {STAGE_NAME_1} started <<<<<<")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f">>>>>> Stage {STAGE_NAME_1} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME_2 = "Data Validation Stage"

try:
    logger.info(f">>>>>> Stage {STAGE_NAME_2} started <<<<<<")
    obj = DataValidationPipeline()
    obj.main()
    logger.info(f">>>>>> Stage {STAGE_NAME_2} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e