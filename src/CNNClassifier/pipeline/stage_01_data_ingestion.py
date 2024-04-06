from CNNClassifier.components import stage_01_data_ingestion
from CNNClassifier.config import COnfigurationManager
from CNNClassifier import logger

logger.info("Data ingestion stage started")
config = ConfigurationManager()
data_ingestion_config = config.get_data_ingestion_config()

data_ingeston = DataIngestion(config=data_ingestion_config)
logger.info("Downloading the dataset")
data_ingeston.download_file()
logger.info("Dataset downloaded")
logger.info("Extracting the dataset")
data_ingeston.unzip_and_clean()


