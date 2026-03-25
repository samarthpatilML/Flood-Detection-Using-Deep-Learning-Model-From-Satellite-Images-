FROM python:3.10

# set working directory
WORKDIR /app

# copy all files
COPY . .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# expose port
EXPOSE 5000

# run app
CMD ["python", "app.py"]