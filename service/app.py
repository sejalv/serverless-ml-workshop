import json
import pickle
import os

model_local_path = os.environ.get('MODEL_LOCAL_PATH', "pickled_model.pkl")


def lambda_handler(event, context):
    with open(model_local_path, 'rb') as f:
        model = pickle.load(f)

    body = event['body']
    if type(body) == str:
        data = json.loads(body)['data']
    else:
        data = body['data']
    input = float(data)

    # Predict class
    prediction = model.predict([[input]])[0]

    response = {
        "statusCode": 200,
        "body": json.dumps({
            "prediction": str(prediction),
        }),
    }

    return response
