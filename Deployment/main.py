from fastapi import FastAPI, File
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import numpy as np
import dill
from operator import itemgetter
from io import BytesIO


app = FastAPI(title="Penguin Classifier")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Import model:
with open('./model.dill', 'rb') as fopen:
    model = dill.load(fopen)

# Define target categories' dictionary:
cats = {0: 'Adelie', 1: 'Chinstrap', 2: 'Gentoo'}


# Define penguin model:
class Penguin(BaseModel):
    culmen_length: float
    culmen_depth: float
    flipper_length: float


# Define the prediction response model:
class PenguinSpeciesPrediction(BaseModel):
    features: Penguin
    prediction: str


@app.get('/', response_model=PenguinSpeciesPrediction)
def get_func(cl: float, cd: float, fl: float):
    """
    Serves predictions given query parameters specifying the penguin's
    features.

    Inputs:
        - cl: culmen length in millimeters
        - cd: culmen depth in millimeters
        - fl: flipper length in millimeters
    """

    return {
        'features': {
            'culmen_length': cl,
            'culmen_depth': cd,
            'flipper_length': fl
        },

        'prediction': cats[model.predict([[cl, cd, fl]])[0]]
    }


@app.post('/json', response_model=PenguinSpeciesPrediction)
def post_json(penguin: Penguin):
    """
    Serves predictions given a request body specifying the penguin's features.

    Inputs:
        - penguin: request body of type `Penguin` with culmen_length,
                   culmen_depth, and flipper_length attributes
    """

    cl = penguin.culmen_length
    cd = penguin.culmen_depth
    fl = penguin.flipper_length

    return {
        'features': penguin,
        'prediction': cats[model.predict([[cl, cd, fl]])[0]]
    }


@app.post('/file', response_class=StreamingResponse)
def post_file(file: bytes = File(...)):
    """
    Serves predictions given a CSV file with no header and three columns
    specifying each penguin's features in the order culmen length, culmen
    depth, and flipper_length. Returns a streaming response with a new CSV file
    that contains a column with the predictions.

    Inputs:
        - file: bytes from a CSV file as described above.
    """

    # Decode the bytes as text and split the lines:
    input_lines = file.decode().split()
    # Split each line as a list of the three features and gather them in an
    # array of floats:
    X = np.array([p.split(',') for p in input_lines], dtype=float)

    # Get predicted categories:
    pred = itemgetter(*model.predict(X))(cats)

    # Append the prediction to each input line:
    output = [p + ',' + c for p, c in zip(input_lines, pred)]
    # Join the output as a single string:
    output = '\n'.join(output)
    # Encode output as bytes:
    output = output.encode()

    return StreamingResponse(
        BytesIO(output),
        media_type='text/csv',
        headers={'Content-Disposition': 'attachment;filename="prediction.csv"'}
    )


if __name__ == '__main__':
    import uvicorn

    # For local development:
    # uvicorn.run("main:app", port=3000, reload=True)

    # For Docker deployment:
    uvicorn.run("main:app", host='0.0.0.0', port=80)
