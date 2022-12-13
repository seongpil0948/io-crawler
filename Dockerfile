FROM python:3.10.8-slim

# This instructs Docker to use this path as the default location for all subsequent commands.
WORKDIR /app

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED=True \
    PYTHON_VERSION=3.10.8 \
    DOCKER_BUILDKIT=0 

RUN pip3 install --upgrade pip

# Copy files in to our working directory /app.
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# takes all the files located in the current directory and copies them into the image.
COPY . .
RUN echo -c "===> app directory structure:  $(find . -maxdepth 2)"

# ENTRYPOINT ["/bin/echo", "Hello"]
# CMD [ "python3", "-m" , "lib.crawler.sinsang"]
CMD [ "sh", "script/crawl_run.sh"]