# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /AbelianLiveTrading

# Copy only the requirements file into the container at /AbelianLiveTrading
COPY req.txt /AbelianLiveTrading/

# Install any needed packages specified in req.txt
RUN pip install --no-cache-dir -r req.txt

# Copy the current directory contents into the container at /AbelianLiveTrading
COPY . /AbelianLiveTrading/

# Your additional commands or CMD can go here










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

