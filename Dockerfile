
MAGNA-FLOW (E-LAB-09) Dockerfile

FROM python:3.11-slim

LABEL maintainer="Samir Baladi <gitdeeper@gmail.com>"
LABEL description="MAGNA-FLOW: Neural MHD Dissipation Control"
LABEL version="1.0.0"
LABEL doi="10.5281/zenodo.19893462"

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY magna_flow/ ./magna_flow/
COPY bin/ ./bin/
COPY configs/ ./configs/

RUN pip install -e .

ENTRYPOINT ["python", "bin/run_control.py"]
CMD ["--help"]
