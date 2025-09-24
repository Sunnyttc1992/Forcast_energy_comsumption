import re
import sys
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object


import sys
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features: pd.DataFrame):
        """Load preprocessor and model from artifacts and return predictions as a list.

        `features` is expected to be a pandas DataFrame with the same columns used during training.
        """
        try:
            model_path = 'artifacts/model.pkl'
            preprocessor_path = 'artifacts/preprocessor.pkl'

            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)

            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)

            # return a Python list for easier templating/serialization
            return preds.tolist() if hasattr(preds, 'tolist') else list(preds)

        except Exception as e:
            raise CustomException(e, sys)


class CustomData:
    def __init__(self,
                 age: int,
                 sex: str,
                 bmi: float,
                 children: int,
                 smoker: str,
                 region: str):
        try:
            self.age = int(age) if age is not None and age != '' else None
            self.sex = sex
            self.bmi = float(bmi) if bmi is not None and bmi != '' else None
            self.children = int(children) if children is not None and children != '' else None
            self.smoker = smoker
            self.region = region
        except Exception as e:
            raise CustomException(e, sys)

    def get_data_as_data_frame(self) -> pd.DataFrame:
        try:
            custom_data_input_dict = {
                "age": [self.age],
                "sex": [self.sex],
                "bmi": [self.bmi],
                "children": [self.children],
                "smoker": [self.smoker],
                "region": [self.region],
            }
            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise CustomException(e, sys)
