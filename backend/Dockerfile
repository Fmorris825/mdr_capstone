FROM python:alpine3.17
WORKDIR /user/src/app
COPY requirements.txt ./
# RUN apk add --no-cache mariadb-dev
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


# FROM python:latest

# WORKDIR /user/src/app

# COPY requirements.txt .
# RUN pip install -r requirements.txt

# COPY . .

# EXPOSE 8000

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
