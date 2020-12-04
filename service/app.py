import json
import os
import boto3
import pickle
import sklearn
from sklearn.linear_model import LogisticRegression

model_bucket = "serverless-ml-workshop-modelbucket-11be8460mjrb1"
model_key = "pickled_model.p"    # env
model_local_path = "/tmp/pickled_model.p"


def lambda_handler(event, context):
    # s3_client = boto3.client('s3')
    # # model_bucket = os.environ['ModelBucket']

    # if not os.path.exists(model_local_path):
    #     print(s3_client.head_object(Bucket=model_bucket, Key=model_key))
    #     s3_client.download_file(model_bucket, model_key, model_local_path)

    s3 = boto3.resource('s3')
    s3.Bucket(model_bucket).download_file(model_key, model_local_path)

    body = event['body']
    input = json.loads(body)['data']
    input = float(input)

    with open(model_local_path, 'rb') as f:
        model = pickle.load(f)
    # Predict class
    prediction = model.predict([[input]])[0]

    response = {
        "statusCode": 200,
        "body": json.dumps({
            "prediction": str(prediction),
        }),
    }

    return response
