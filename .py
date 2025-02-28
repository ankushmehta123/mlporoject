import pickle

with open("C:/Users/ANKUSH/Desktop/mlproject/artifacts/proprocessor.pkl", "rb") as f:
    obj = pickle.load(f)
    print(type(obj))  # Should print the type of the object, like <class 'sklearn.preprocessing.StandardScaler'>

import os

print("Current Working Directory:", os.getcwd())

import os

preprocessor_path = "C:/Users/ANKUSH/Desktop/mlproject/artifacts/model.pkl"
print("Readable:", os.access(preprocessor_path, os.R_OK))

import os

preprocessor_path = "C:/Users/ANKUSH/Desktop/mlproject/artifacts/proprocessor.pkl"
print("Readable:", os.access(preprocessor_path, os.R_OK))
