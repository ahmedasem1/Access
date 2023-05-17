FROM python:3.10

ENV PYTHONUNBUFFERD=1

WORKDIR /CODE

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python3","manage.py","runserver"]
# # setup environment variable  
# ENV DockerHOME=/home/app/webapp  

# # set work directory  
# RUN mkdir -p $DockerHOME  

# # where your code lives  
# WORKDIR $DockerHOME  

# # set environment variables  
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1  

# # install dependencies  
# RUN pip install --upgrade pip  

# # copy whole project to your docker home directory. 
# COPY . $DockerHOME  
# # run this command to install all dependencies  
# RUN pip install -r requirements.txt  
# # port where the Django app runs  
# EXPOSE 8000  
# # start server  
# CMD python manage.py runserver  