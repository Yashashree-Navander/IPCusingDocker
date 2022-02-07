# Get the latest base image for python
FROM python:3.8-alpine
# Put files at the image '/server/' folder.
ADD producer.py /server/
# '/server/' is base directory
WORKDIR /server/
# Expose port 5000 in the container
EXPOSE 5000
# execute the command
CMD [ "python3", "/server/producer.py" ]
