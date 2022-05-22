FROM python:alpine
WORKDIR /app
RUN mkdir /app/templates
COPY app.py /app
COPY BadR.html /app/templates
COPY BadR.html /app/templates
COPY base.html /app/templates
RUN pip install -U Flask
RUN pip install Turbo-Flask
RUN pip install requests
CMD python /app/app.py
