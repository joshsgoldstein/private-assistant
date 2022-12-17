#Deriving the latest base image
FROM python:3.9


#Labels as key value pair
LABEL Maintainer="joshsgoldstein"

#  Add operating system dependencies
RUN apt-get update -y
RUN apt install espeak -y
RUN apt-get install libasound-dev libportaudio2 libportaudiocpp0 portaudio19-dev -y


# Any working directory can be chosen as per choice like '/' or '/home' etc
# i have chosen /usr/app/src
WORKDIR /usr/app/src

#to COPY the remote file at working directory in container
COPY private-assistant.py ./
COPY requirements.txt ./
RUN pip install -r requirements.txt
# Now the structure looks like this '/usr/app/src/test.py'


#CMD instruction should be used to run the software
#contained by your image, along with any arguments.

CMD [ "python", "./private-assistant.py"]