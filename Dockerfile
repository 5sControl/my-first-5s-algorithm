FROM python:3.11-slim
RUN apt-get update
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install torch==1.13.1+cpu torchvision==0.14.1+cpu --extra-index-url https://download.pytorch.org/whl/cpu


RUN pip install -r requirements.txt
RUN apt-get install ffmpeg libsm6 libxext6  -y

WORKDIR /var/www/5scontrol
COPY . .
ENTRYPOINT ["python", "-u", "vest.py"]
