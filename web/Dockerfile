FROM python:3.10.0a2-slim
ENV PYTHONUNBUFFERED 1
# create root directory for our project in the container
RUN mkdir /django
# Set the working directory to /django
WORKDIR /django
# Copy the current directory contents into the container at /django
ADD . /django/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8000
WORKDIR /django/validity
CMD python  ./manage.py runserver 0.0.0.0:8000
