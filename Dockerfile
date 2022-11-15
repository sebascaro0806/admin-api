FROM python:3.9
COPY ./ /api-admin
RUN pip install --no-cache-dir --upgrade -r /api-admin/requirements.txt
COPY ./ /api-admin
WORKDIR /api-admin
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]