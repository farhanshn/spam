from pathlib import Path
import sys
#lets create the path
PROJECT_ROOT=Path(__file__).resolve().parent.parent

#define the paths 
DATA_DIR=PROJECT_ROOT/"data"
RAW_DIR=DATA_DIR/"raw"
PROCESSED_DIR=DATA_DIR/"processed"

#define the models and report folder
MODEL_DIR=PROJECT_ROOT/"models"
REPORTS=PROJECT_ROOT/"reports"
#define the path of data set
DATA_SET=RAW_DIR/"train.csv"