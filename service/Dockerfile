# multi-stage build

FROM public.ecr.aws/lambda/python:3.8 as base

FROM base AS train
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV MODEL_LOCAL_PATH=pickled_model.p
COPY train.py .
RUN python3 train.py

FROM base
RUN pip install scikit-learn==0.22.1
ENV MODEL_LOCAL_PATH=pickled_model.p
COPY --from=train ./var/task/pickled_model.p pickled_model.p
COPY app.py ./

# Command can be overwritten by providing a different command in the template directly.
CMD ["app.lambda_handler"]
