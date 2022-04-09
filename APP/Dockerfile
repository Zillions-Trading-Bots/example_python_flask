FROM python:3.9.10
# Set application working directory
WORKDIR /usr/src/app
# Install requirements
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
# Install application
COPY * ./

EXPOSE 5000
# Run application
CMD python entry_flask.py