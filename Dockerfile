FROM python:3.8

WORKDIR /AbelianLiveTrading
COPY . .
RUN pip install -r req.txt
CMD ["python3","App.py"]

# RUN pip install debugpy
# CMD [ "-m debugpy --listen localhost:5678 --wait-for-client App.py" ]
# CMD ["debugpy", "run", "--listen", "5678:5678", "--wait-for-client", "App.py"]
