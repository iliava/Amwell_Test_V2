FROM python:alpine
WORKDIR /app
RUN mkdir /app/templates
COPY app.py /app
COPY Bad.html /app/templates
COPY Good.html /app/templates
RUN pip install -U Flask
RUN pip install requests
CMD python /app/app.py
