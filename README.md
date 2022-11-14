
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

Credit-Card-Default-Predictions
│
├───.github
│   └───workflows
│           main.yaml
│
├───.idea
│   │   .gitignore
│   │   creditcarddefault.iml
│   │   misc.xml
│   │   modules.xml
│   │   vcs.xml
│   │   workspace.xml
│   │
│   └───inspectionProfiles
│           profiles_settings.xml
│           Project_Default.xml
│
├───.ipynb_checkpoints
│       Credit Card Default -checkpoint.ipynb
│
├───All Project Documents
│       architecture design.pdf
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
│           logger.cpython-36.pyc
│           logger.cpython-37.pyc
│
├───best_model_finder
│   │   tuner.py
│   │
│   └───__pycache__
│           tuner.cpython-36.pyc
│           tuner.cpython-37.pyc
│
├───DataTransformation_Prediction
│   │   DataTransformationPrediction.py
│   │
│   └───__pycache__
│           DataTransformationPrediction.cpython-36.pyc
│           DataTransformationPrediction.cpython-37.pyc
│
├───DataTransform_Training
│   │   DataTransformation.py
│   │
│   └───__pycache__
│           DataTransformation.cpython-36.pyc
│           DataTransformation.cpython-37.pyc
│
├───DataTypeValidation_Insertion_Prediction
│   │   DataTypeValidationPrediction.py
│   │
│   └───__pycache__
│           DataTypeValidationPrediction.cpython-36.pyc
│           DataTypeValidationPrediction.cpython-37.pyc
│
├───DataTypeValidation_Insertion_Training
│   │   DataTypeValidation.py
│   │
│   └───__pycache__
│           DataTypeValidation.cpython-36.pyc
│           DataTypeValidation.cpython-37.pyc
│
├───data_ingestion
│   │   data_loader.py
│   │   data_loader_prediction.py
│   │
│   └───__pycache__
│           data_loader.cpython-36.pyc
│           data_loader.cpython-37.pyc
│           data_loader_prediction.cpython-36.pyc
│           data_loader_prediction.cpython-37.pyc
│
├───data_preprocessing
│   │   clustering.py
│   │   preprocessing.py
│   │
│   └───__pycache__
│           clustering.cpython-36.pyc
│           clustering.cpython-37.pyc
│           preprocessing.cpython-36.pyc
│           preprocessing.cpython-37.pyc
│           preprocessing_pred.cpython-36.pyc
│
├───file_operations
│   │   file_methods.py
│   │
│   └───__pycache__
│           file_methods.cpython-36.pyc
│           file_methods.cpython-37.pyc
│
├───models
│   ├───KMeans
│   │       KMeans.sav
│   │
│   ├───XGBoost0
│   │       XGBoost0.sav
│   │
│   ├───XGBoost1
│   │       XGBoost1.sav
│   │
│   ├───XGBoost2
│   │       XGBoost2.sav
│   │
│   └───XGBoost3
│           XGBoost3.sav
│
├───PredictionArchivedBadData
│   ├───BadData_2020-02-19_165637
│   ├───BadData_2020-02-19_173611
│   ├───BadData_2020-04-12_215100
│   │       creditCardFraud_28011961_12.csv
│   │       creditCardFraud_28011963_120213.csv
│   │
│   └───BadData_2022-07-26_230649
│           creditCardFraud_28011961_12.csv
│           creditCardFraud_28011963_120213.csv
│
├───Prediction_Batch_files
│       creditCardFraud_28011960_120210.csv
│       creditCardFraud_28011961_12.csv
│       creditCardFraud_28011962_120212.csv
│       creditCardFraud_28011963_120213.csv
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
│           predictionDataValidation.cpython-36.pyc
│           predictionDataValidation.cpython-37.pyc
│
├───Prediction_Raw_Files_Validated
│       sample.txt
│
├───preprocessing_data
│       K-Means_Elbow.PNG
│
├───SingleValueModels
│       rfc.pkl
│
├───SinglrValuePredictionLogs
│       SingleValuePredictionLogs.txt
│
├───static
│   ├───images
│   │       github.png
│   │       image4.gif
│   │       linkden.jpg
│   │       logo.jpg
│   │
│   └───styles
│           style.css
│
├───templates
│       index.html
│       prediction.html
│       result.html
│       singlevalueprediction.html
│       training.html
│
├───TrainingArchiveBadData
│   ├───BadData_2022-07-18_191749
│   │       CreditFraud_28011960_120210.xlsx
│   │       file_seperator.ipynb
│   │
│   └───BadData_2022-07-26_220500
│           CreditFraud_28011960_120210.xlsx
│           file_seperator.ipynb
│
├───Training_Batch_Files
│       creditCardFraud_28011960_120210.csv
│       creditCardFraud_28011961_120211.csv
│       creditCardFraud_28011962_120212.csv
│       creditCardFraud_28011963_120213.csv
│       creditCardFraud_28011964_120214.csv
│       CreditFraud_28011960_120210.xlsx
│       file_seperator.ipynb
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
│   app.py
│   Credit Card Default .ipynb
│   Dockerfile
│   predictFromModel.py
│   prediction_Validation_Insertion.py
│   Procfile
│   requirements.txt
│   schema_prediction.json
│   schema_training.json
│   trainingModel.py
│   Training_Main_Log.txt
│   training_Validation_Insertion.py
│   tree.txt
│   UCI_Credit_Card.csv


# Author

Archana Bora
