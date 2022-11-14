
# Thyroid_Disease_Detection

Thyroid disease is a common cause of medical diagnosis and prediction, with an onset 
that is difficult to forecast in medical research. The thyroid gland is one of our body's 
most vital organs. Thyroid hormone releases are responsible for metabolic regulation. 
Hyperthyroidism and hypothyroidism are one of the two common diseases of the thyroid 
that releases thyroid hormones in regulating the rate of body's metabolism.
The main goal is to predict the estimated risk on a patient's chance of obtaining thyroid 
disease or not.
# Webpage Link
For Bulk Prediction
https://thyroid-prediction-project.herokuapp.com/

# Technical Aspect
This project is divided into three part:

  1.Training:

        a. When ever batch files recived from clients. dataset will validate and cleaned and then dataset first into clusters group.

        b. Based on number of clusters that many models will be created and store the models for prediction purpose.

  2.Prediction:

        a.When client enter prediction dataset batch file paths. first it will validate and cleaned.
        b.Then it will go for preiction with saved models. Finally predictions will show to client.

  3.Deployment :

        Deployment was done by using github and heroku.

# Project Pipline

1.Batch files

2.Data validation

3.Data Transformation

4.Data Inserstion

5.Data Preprocessing

6.Model creation

7.Hyper parameter tunning.

8.Model Evaluation

9.Deployment

# Technical Aspects

Python 3.7 and more

Important Libraries: sklearn, pandas, numpy, matplotlib & seaborn

Front-end: HTML, CSS

Back-end: Flask framework

IDE: Jupyter Notebook, Pycharm 

Database: sqlite

Deployment: Heroku

# Workflow

# Data Collection

Thyroid Disease Data Set from UCI Machine Learning Repository.

# Data Pre-processing

1.Missing values handling by Simple imputation (KNN Imputer)

2.Outliers detection and removal by boxplot and percentile methods

3.Categorical features handling by label encoding

4.Imbalanced dataset handled by SMOTE

5.Drop unnecessary columns

# Model Creation and Evaluation

1.Various classification algorithms like Random Forest, KNN tested.

2.Random Forest and KNN were all performed well. Random Forest was chosen for the final model training and testing.

3.Hyper parameter tuning was performed using RandomizedSearchCV

4.Model performance evaluated based on accuracy, confusion matrix, classification report.

# Database Connection

sqlite database was used for this project

# Model Deployment

The final model is deployed on Heroku using Flask framework.

# Project Documents
1.HLD:https://github.com/Archana271/Thyroid_Disease_Detection/blob/main/All%20Project%20Documents/HLD.pdf 
2.LLD:https://github.com/Archana271/Thyroid_Disease_Detection/blob/main/All%20Project%20Documents/LLD.pdf 
3.Architecture:https://github.com/Archana271/Thyroid_Disease_Detection/blob/main/All%20Project%20Documents/Architecture%20design.pdf 
4.Wireframe:https://github.com/Archana271/Thyroid_Disease_Detection/blob/main/All%20Project%20Documents/Wireframe_Documentation.pdf 
5.Detailed Project Report:https://github.com/Archana271/Thyroid_Disease_Detection/blob/main/All%20Project%20Documents/Detail%20Project%20Report.pdf

# Directory Tree

Thyroid-Disease-Detection-Predictions

|
├───.idea
│   │   .gitignore
|   |   .name
│   │   Thyroid_Disease_Detection.iml
│   │   misc.xml
│   │   modules.xml
│   │   vcs.xml
│   │   
│   │
│   └───inspectionProfiles
│           profiles_settings.xml
│           Project_Default.xml

│
├───.ipynb_checkpoints
│       Credit Card Default -checkpoint.ipynb

│
├───All Project Documents
│       Architecture design.pdf
│       Deatail Project Report.pdf
│       HLD.pdf
│       LLD.pdf
│       Project demo video.mp4
│       Wireframe_Documentaion.pdf

│
├───application_logging
│   │   logger.py
│   │
│   └───__pycache__
│           logger.cpython-37.pyc

│           
│
├───best_model_finder
│   │   tuner.py
│   │
│   └───__pycache__
│           tuner.cpython-37.pyc

│           
│
├───DataTransformation_Prediction
│   │   DataTransformationPrediction.py

│   │
│   └───__pycache__
│           DataTransformationPrediction.cpython-37.pyc

│           
│
├───DataTransform_Training
│   │   DataTransformation.py
│   │
│   └───__pycache__
│           DataTransformation.cpython-37.pyc

│           
│
├───DataTypeValidation_Insertion_Prediction
│   │   DataTypeValidationPrediction.py
│   │
│   └───__pycache__
│           DataTypeValidationPrediction.cpython-37.pyc

│           
│
├───DataTypeValidation_Insertion_Training
│   │   DataTypeValidation.py
│   │
│   └───__pycache__
│           DataTypeValidation.cpython-37.pyc

│           
│
├───data_ingestion
│   │   data_loader.py
│   │   data_loader_prediction.py
│   │
│   └───__pycache__
│           
│           data_loader.cpython-37.pyc
│           data_loader_prediction.cpython-37.pyc

│           
│
├───data_preprocessing
│   │   clustering.py
│   │   preprocessing.py
│   │
│   └───__pycache__
│           
│           clustering.cpython-37.pyc
│           preprocessing.cpython-37.pyc

│           
│           
│
├───file_operations
│   │   file_methods.py
│   │
│   └───__pycache__
│           file_methods.cpython-37.pyc

│           
│
├───models
│   ├───KMeans
│   │       KMeans.sav
│   │
│   ├───KNN1
│   │       KNN1.sav
│   │
│   ├───RandomForest0
│   │       RandomForest0.sav
│   │
│   ├───RandomForest2
│   │       RandomForest2.sav
│   │
│   └

│
├───PredictionArchivedBadData
│   ├───BadData_2022-11-07_213927
│   ├───BadData_2022-11-07_215028
│   ├───BadData_2020-11-07_221409
│   |   BadData_2020-11-07_222844
│   │   BadData_2020-11-11_205538

│   
│   
│
├───Prediction_Batch_files
│       CreditFraud_28011960_120210.xlsx
│       hypothyroid.csv
│       hypothyroid_25092022_120000.csv

│       
│
├───Prediction_Database
│       Prediction.db

│
├───Prediction_FileFromDB
│       InputFile.csv

│
├───Prediction_Logs
│       columnValidationLog.txt
│       DataBaseConnectionLog.txt
│       dataTransformLog.txt
│       DbInsertLog.txt
│       DbTableCreateLog.txt
│       ExportToCsv.txt
│       GeneralLog.txt
│       missingValuesInColumn.txt
│       nameValidationLog.txt
│       Prediction_Log.txt

│
├───Prediction_Output_File
│       Predictions.csv

│
├───Prediction_Raw_Data_Validation
│   │   predictionDataValidation.py
│   │
│   └───__pycache__
│           predictionDataValidation.cpython-37.pyc

│           
│
├───Prediction_Raw_Files_Validated

│       
│
├───preprocessing_data
│       K-Means_Elbow.PNG
|       null_values.csv

│
├───EncoderPickle
│       rfc.pkl

│
|
│
├───static
│   ├───images
│   │     
│   │       thyroi-min.jpg
│   │       
│   │
│   └───styles
│           style.css

│
├───templates
│       index.html
│       prediction.html
│       result.html
│       training.html

│
├───TrainingArchiveBadData
│   ├───BadData_2022-11-07_200056
│   │       
│   │
│   └───BadData_2022-11-11_203032

│           
│
├───Training_Batch_Files
│       CreditFraud_28011960_120210.xlsx
│       hypothyroid.csv
│       hypothyroid_25092022_120000.csv

│
├───Training_Database
│       Training.db

│
├───Training_FileFromDB

│
├───Training_Logs
│       columnValidationLog.txt
│       DataBaseConnectionLog.txt
│       dataTransformLog.txt
│       DbInsertLog.txt
│       DbTableCreateLog.txt
│       ExportToCsv.txt
│       GeneralLog.txt
│       missingValuesInColumn.txt
│       ModelTrainingLog.txt
│       nameValidationLog.txt
│       valuesfromSchemaValidationLog.txt

│
├───Training_Raw_data_validation
├───Training_Raw_files_validated
│   main.py
│   predictFromModel.py
│   prediction_Validation_Insertion.py
│   Procfile
│   requirements.txt
│   schema_prediction.json
│   schema_training.json
│   trainingModel.py
│   Training_Main_Log.txt
│   training_Validation_Insertion.py



# Author

Archana Bora
