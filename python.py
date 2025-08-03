from fastapi import FastAPI
from sklearn.preprocessing import StandardScaler
from pymongo import MongoClient
from pydantic import BaseModel
from model import K_means_model
import pandas as pd
import numpy as np
app = FastAPI()


class PredictRequest(BaseModel):
    BALANCE: float
    BALANCE_FREQUENCY: float
    PURCHASES: float
    ONEOFF_PURCHASES: float
    INSTALLMENTS_PURCHASES: float
    CASH_ADVANCE: float
    PURCHASES_FREQUENCY: float
    ONEOFF_PURCHASES_FREQUENCY: float
    PURCHASES_INSTALLMENTS_FREQUENCY: float
    CASH_ADVANCE_FREQUENCY: float
    CASH_ADVANCE_TRX: int
    PURCHASES_TRX: int
    CREDIT_LIMIT: float
    PAYMENTS: float
    MINIMUM_PAYMENTS: float
    PRC_FULL_PAYMENT: float
    TENURE: int
   
# MongoDB connection
URL = 'mongodb+srv://admin:nHLfecsVHTG3Hkgu@cluster0.4pvvsk6.mongodb.net/k_means?retryWrites=true&w=majority'
client = MongoClient(URL)
collection = client['k_means']
def fix_id(doc):
    doc.pop("_id",None)
    doc.pop("CUST_ID",None)
    doc.pop("__v",None)

    return doc

Model = K_means_model()
@app.get('/data')
def get_data():
    data=list(collection['segment'].find())
    return [fix_id(doc)for doc in data]
@app.post('/train_model')
def train():
    data=list(collection["segment"].find())
    data=[fix_id(doc)for doc in data]

    Model.dataproces(data)
  
    
    Model.applying_elbow()
    Model.train_model()
    score=Model.evaluate_model()
    return {"status": "success", "message": "Model trained successfully",'score':score}

@app.post('/predict')
def predictions():
    data=list(collection['predicts'].find())
    data=[fix_id(doc)for doc in data]
    predict = Model.prediction(data)
    return {"prediction": predict}

    