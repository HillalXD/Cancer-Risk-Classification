from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.openapi.utils import get_openapi
from fastapi.responses import JSONResponse
from fastapi import Request
import pickle

# Define the FastAPI app
app = FastAPI(title="Cervical Cancer Detection API", version="1.0")

# Load the trained logistic regression model
model = pickle.load(open("regression.pkl", "rb"))

# Define a request model
class CancerDetectionRequest(BaseModel):
    Schiller: bool
    Hinselmann: bool
    Citology: bool
    STDs: bool
    hormonal_contraceptives_years: int
    Smokes_years: int
    iud: bool
    age: int
    hormonal_contraceptives: bool
    iud_years: int

# Define the prediction endpoint
@app.post("/predict")
def predict_cervical_cancer(request: CancerDetectionRequest):
    # Prepare the input features for prediction
    features = [
        int(request.Schiller),
        int(request.Hinselmann),
        int(request.Citology),
        int(request.STDs),
        request.hormonal_contraceptives_years,
        request.Smokes_years,
        int(request.iud),
        request.age,
        int(request.hormonal_contraceptives),
        request.iud_years
    ]

    # Perform the prediction using the logistic regression model
    result = model.predict([features])[0]

    if result == 0:
        prediction = "Low risk of cervical cancer"
    else:
        prediction = "High risk of cervical cancer"

    return {"prediction": prediction}

# Override the OpenAPI schema to include examples in the documentation
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://yourdomain.com/logo.png"
    }
    # Add example requests and responses to the documentation
    openapi_schema["paths"]["/predict"]["post"]["requestBody"]["content"]["application/json"]["example"] = {
         "Schiller": True,
         "Hinselmann": True,
         "Citology": False,
         "STDs": True,
         "hormonal_contraceptives_years": 0,
         "Smokes_years": 0,
         "iud": True,
         "age": 28,
         "hormonal_contraceptives": True,
         "iud_years": 3
    }
    openapi_schema["paths"]["/predict"]["post"]["responses"]["200"]["content"]["application/json"]["example"] = {
        "prediction": "High risk of cervical cancer"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi


