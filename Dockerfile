FROM python:3.8

WORKDIR /AbelianLiveTrading
COPY . .
RUN pip install -r req.txt
# CMD ["python3","App.py"]

# # Use the official AWS Lambda Python image as the base image
# FROM public.ecr.aws/lambda/python:3.8
# WORKDIR /Abelian_Live_Trading
# # Copy your requirements file and install dependencies
# COPY req.txt .
# RUN pip install -r req.txt

# # Copy your Python script (App.py)
# COPY . .

# # Set the CMD to your handler
# CMD ["App.lambda_handler"]

