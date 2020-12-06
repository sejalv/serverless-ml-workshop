FROM public.ecr.aws/lambda/python:3.8

COPY app.py requirements.txt ./
RUN pip install -r requirements.txt
RUN rm ./requirements.txt && ls
COPY --from=serverless-ml-workshop_train model/pickled_model.p model/pickled_model.p

# Command can be overwritten by providing a different command in the template directly.
CMD ["app.lambda_handler"]
