from NetworkSec.components.data_ingestion import DataIngestion
from NetworkSec.exception.exception import NetworkSecurityException
from NetworkSec.logging.logger import logging
from NetworkSec.entity.config_entity import DataIngestionConfig
from NetworkSec.entity.config_entity import TrainingPipelineConfig

import sys

if __name__ == "__main__":
    try:
        logging.info("Starting data ingestion process.")
        training_pipeline_config = TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(training_pipeline_config)
        data_ingestion = DataIngestion(data_ingestion_config)
        dataingestionartifact = data_ingestion.initiate_data_ingestion()
        print(dataingestionartifact)
        logging.info("Data ingestion process completed successfully.")
    except Exception as e:
        raise NetworkSecurityException(e, sys)