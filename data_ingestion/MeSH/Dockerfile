FROM python:3.7

RUN pip install requests
RUN pip install rdflib

# Packages that we need 
COPY requirements.txt /app/
WORKDIR /app
# instruction to be run during image build
RUN pip install -r requirements.txt
# Copy all the files from current source duirectory(from your system) to
# Docker container in /app directory 
COPY . /app

CMD [ "python", "./mesh_load.py" ]