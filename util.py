import pickle
import json
import numpy as np

__data_columns = None
__model = None

def get_gender():
    return {"gender": __data_columns["data_columns"][4:6]}

def get_regions():
    return {"locations":__data_columns["data_columns"][6:]}

def get_insurance_price(age,bmi,n_children,smoker,sex,region):
    columns = __data_columns["data_columns"]
    loc_sex = columns.index(sex)
    loc_region = columns.index(region)
    x = np.zeros(len(columns))
    x[0] = age
    x[1] = bmi
    x[2] = n_children
    x[3] = smoker
    x[loc_sex] = 1
    x[loc_region] = 1
    return round(__model.predict([x])[0], 2)


def load_artifacts():
    global __data_columns
    global __model

    with open("artifacts/insurance_price_columns.json", "r") as f:
        __data_columns = json.loads(f.read())

    with open("artifacts/insurance_price_prediction_model.pickle", "rb") as f:
        __model = pickle.load(f)
        # print(__model)



if __name__ == "__main__":
    load_artifacts()
    print(get_insurance_price(19, 27.9, 0, 1, "female", "southwest"))
    # print(get_location())
    # get_gender()
