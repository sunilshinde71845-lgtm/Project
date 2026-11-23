FROM python:3.14-slim 
WORKDIR /library_management
COPY management.py /library_management/management.py 
CMD ["python", "/library_management/management.py"]
