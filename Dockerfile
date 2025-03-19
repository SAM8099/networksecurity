FROM python:3.10-slim-buster
WORKDIR /app
COPY . /app

#Installing required packages
RUN pip install --trusted-host pypi.python.org -r requirements.txt

#Open port 5000
EXPOSE 5000

#Set environment variable
ENV NAME OpentoAll

CMD [ "python", "app.py" ]