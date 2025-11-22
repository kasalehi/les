

import sys
from pathlib import Path

from flask import logging
import src.exception as ex
from src.logs import logger
import pandas as pd



class DataIngestor:
    def __init__(self, data_source):
        self.data_source = data_source
        
    def ingest(self):
        try:
            logger.info(f"Starting data ingestion from {self.data_source}")
            # Simulate data ingestion logic
            if not self.data_source:
                raise ex.CustomException("Data source path is invalid.")
            # Assume data is ingested successfully
            df=pd.read_csv(self.data_source)
            logger.info(f"Data ingested successfully with {len(df)} records.")
            logger.info(f"Data ingestion completed successfully from {self.data_source}")
        except ex.CustomException as die:
            logger.error(f"Data ingestion error: {die}")
            sys.exit(1)
            
    def validate(self, df):
        try:
            logger.info("Starting data validation.")
            # Simulate data validation logic
            if df.empty:
                raise ex.CustomException("Ingested data is empty.")
            # Assume data is validated successfully
            logger.info("Data validation completed successfully.")
        except ex.CustomException as dve:
            logger.error(f"Data validation error: {dve}")
            sys.exit(1)
        except Exception as e:
            logger.error(f"An unexpected error occurred during data validation: {e}")
            sys.exit(1)
    def transform(self, df):
        try:
            logger.info("Starting data transformation.")
            # Simulate data transformation logic
            df_transformed = df.copy()  # Placeholder for actual transformation logic
            # Assume data is transformed successfully
            logger.info("Data transformation completed successfully.")
            return df_transformed
        except Exception as e:
            logger.error(f"An unexpected error occurred during data transformation: {e}")
            sys.exit(1)              
            
    def save(self, df, destination):
        try:
            logger.info(f"Starting to save data to {destination}.")
            # Simulate data saving logic
            df.to_csv(destination, index=False)
            logger.info(f"Data saved successfully to {destination}.")
        except Exception as e:
            logger.error(f"An unexpected error occurred while saving data: {e}")
            sys.exit(1)
if __name__ == "__main__":   
    destination_path = Path(__file__).parent.parent.parent / "datasets" / "processed" / "processed_data.csv"  
    data_ingestor = DataIngestor(data_source="C:\\Users\\ksale\\OneDrive\\Desktop\\les\\les\\datasets\\raw_data\\titanic.csv")
    data_ingestor.ingest()
    df = pd.read_csv(data_ingestor.data_source)
    data_ingestor.validate(df)
    df_transformed = data_ingestor.transform(df) 
    data_ingestor.save(df_transformed, destination=destination_path)         