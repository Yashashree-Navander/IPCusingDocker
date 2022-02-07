FROM python:3.8-alpine
# Put files at the image '/client/' folder.
ADD consumer.py /client/
# '/client/' is base directory
WORKDIR /client/
# execute the command
CMD [ "python3", "/client/consumer.py" ]
