FROM tiangolo/uvicorn-gunicorn:python3.9

RUN mkdir /trigger-view-fastapi

WORKDIR /trigger-view-fastapi

COPY requirements.txt /trigger-view-fastapi

RUN pip install -r requirements.txt -f https://download.pytorch.org/whl/torch_stable.html

COPY . /trigger-view-fastapi

EXPOSE 8000

CMD ["python", "start.py"]
