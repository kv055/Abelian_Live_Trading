FROM ubuntu
RUN apt update -y && apt upgrade -y
RUN apt install python3.8 python3-pip -y
WORKDIR /AbelianLiveTrading
COPY . /AbelianLiveTrading
RUN pip install -r req.txt
CMD ["python3","App.py"]