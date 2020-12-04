FROM python:3.7

# Install dependencies:
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
RUN rm ./requirements.txt

RUN mkdir model

# COPY envs.py ./envs.py
# COPY generate_data.py ./generate_data.py
# COPY utils.py ./utils.py

ENV AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}
ENV AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}
ENV AWS_REGION=eu-central-1

ENV MODEL_DIR=/model
ENV MODEL_FILE=ml_mod.joblib
ENV METADATA_FILE=metadata.json
ENV S3BUCKET=serverless-ml-workshop-modelbucket-1ow1ixyw8bfta

COPY train.py ./train.py
# COPY inference.py ./inference.py

RUN python3 train.py
# RUN aws s3 cp pickled_model.p ${S3BUCKET}
