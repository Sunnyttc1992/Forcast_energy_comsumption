import os
import sys
import numpy as np
import pandas as pd
from src.exception import CustomException
import pickle
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        
        os.makedirs(dir_path, exist_ok=True)
        
        with open(file_path, 'wb') as file_obj:
            pickle.dump(obj, file_obj)
    
    except Exception as e:
        raise CustomException(e, sys)

def evaluate_models(X_train, y_train, X_test, y_test, models):
    """Train each model and return a report mapping model name -> test R2 score.

    The models dict is mutated in-place (models are fitted) so callers can use
    the fitted estimator afterwards.
    """
    try:
        report = {}

        for i in range(len(models)):
            model_name = list(models.keys())[i]
            model = list(models.values())[i]

            # Train the model
            model.fit(X_train, y_train)

            # Predict the test set
            y_test_pred = model.predict(X_test)

            # Calculate r2 score on test data
            test_model_score = r2_score(y_test, y_test_pred)

            report[model_name] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)