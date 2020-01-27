# informs docker what version(s) of python to use
FROM python:3

# informs docker where in the directory to copy the files to
WORKDIR /root

# source of files that need copying --> destination
COPY . /root

# run command to install python dependencies from requirements.txt file
RUN python -m pip install -r requirements.txt
