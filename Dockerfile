FROM python:3.9-slim



COPY . /


RUN pip install --no-cache-dir -r requirements.txt

# Specify the command to run on container start
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]