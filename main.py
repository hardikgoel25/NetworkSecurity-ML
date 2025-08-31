from NetworkSec.components.data_ingestion import DataIngestion
from NetworkSec.components.data_validation import DataValidation
from NetworkSec.exception.exception import NetworkSecurityException
from NetworkSec.logging.logger import logging
from NetworkSec.entity.config_entity import DataIngestionConfig
from NetworkSec.entity.config_entity import DataValidationConfig
from NetworkSec.entity.config_entity import TrainingPipelineConfig

import sys

if __name__ == "__main__":
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data Initiation Completed")
        print(dataingestionartifact)
        data_validation_config=DataValidationConfig(trainingpipelineconfig)
        data_validation=DataValidation(dataingestionartifact,data_validation_config)
        logging.info("Initiate the data Validation")
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info("data Validation Completed")
        print(data_validation_artifact)
    except Exception as e:
        raise NetworkSecurityException(e, sys)