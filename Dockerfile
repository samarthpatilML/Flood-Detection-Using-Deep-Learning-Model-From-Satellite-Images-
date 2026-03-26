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
CMD ["python", "app.py"]FROM python:3.10

WORKDIR /app

COPY . .

# 🔥 ADD THIS LINE (fix for cv2)
RUN apt-get update && apt-get install -y libgl1

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]