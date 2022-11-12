
from flask import Flask, request, render_template
import pickle
from flask import Response
import os
import pandas as pd
from flask_cors import CORS, cross_origin
from prediction_Validation_Insertion import pred_validation
from trainingModel import trainModel
from training_Validation_Insertion import train_validation

from predictFromModel import prediction



app = Flask(__name__,template_folder="templates")


@app.route("/", methods=['POST','GET'])
@cross_origin()
def Home():
    return render_template('index.html')


@app.route("/Prediction", methods=['POST', 'GET'])
def Prediction():
    try:
        if request.method == "POST":
            if request.form is not None:
                path = request.form['filepath']
                # object initialization for prediction ingestion
                pred_val = pred_validation(path)
                pred_val.prediction_validation()  # calling the prediction_validation function
                # object initialization for Prediction
                pred = prediction(path)
                path = pred.predictionFromModel()  # predicting for dataset present in database
                return Response(path)
        else:
            return render_template("prediction.html")

    except ValueError:
        return Response("Error Occurred! %s" % ValueError)
    except KeyError:
        return Response("Error Occurred! %s" % KeyError)
    except Exception as e:
        return Response("Error Occurred! %s" % e)


@app.route("/Training", methods=['POST', 'GET'])
def Training():
    try:
        if request.method == "POST":
            path = request.form['filepath']
            if len(path) == 0:
                return Response("Please Enter a Path to do Training..!!")
            elif path == "Training_Batch_files":
                # object initialization for training ingestion
                train_valObj = train_validation(path)
                train_valObj.train_validation()  # calling the training_validation
                # object initialization for model training
                trainModelObj = trainModel()
                trainModelObj.trainingModel()  # training the model for the files in the table
                return Response("Default File Training completed successfully")
            else:
                train_valObj = train_validation(path)  # object initialization
                train_valObj.train_validation()  # calling the training_validation
                trainModelObj = trainModel()  # object initialization
                trainModelObj.trainingModel()  # training the model for the files in the table
                return Response("Training completed successfully By Using" + path)
        else:
            return render_template("training.html")
    except ValueError:
        return Response("Error Occurred! %s" % ValueError)
    except KeyError:
        return Response("Error Occurred! %s" % KeyError)
    except Exception as e:
        return Response("Error Occurred! %s" % e)

@app.route("/Predictionscsvtohtml")
def Predictionscsvtohtml():
    try:
        data = pd.read_csv("Prediction_Output_File/Predictions.csv")
        return render_template("result.html", tables=[data.to_html(columns=["Predictions"])], titles=[''])
    except:
        return render_template("prediction.html",Error="Do Predication to see Prediction..!")
        return render_template("index.html")


# port = int(os.getenv("PORT"))
if __name__ == "__main__":
    app.run(debug=True,port=5000)




