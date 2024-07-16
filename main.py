from fastapi import FastAPI
from pydantic import BaseModel
import util as util


app = FastAPI()
util.load_artifacts()

class InsuranceParam(BaseModel):
    age:int
    bmi:float
    children:int
    smoker:int
    sex:str
    location:str

@app.get("/")
async def home():
    return {"status" : "Everything OK!"}

@app.get("/get_gender")
async def get_gender():
    return util.get_gender()

@app.get("/get_region")
async def get_locay():
    return util.get_regions()

@app.post("/predict_insurance")
def predict_price(param: InsuranceParam):
    age = param.age
    bmi = param.bmi
    children = param.children
    smoker = param.smoker
    sex = param.sex
    location = param.location
    return util.get_insurance_price(age, bmi, children, smoker, sex, location)