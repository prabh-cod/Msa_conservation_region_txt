FROM python:3.10-slim
RUN pip install --no-cache-dir pytest==8.4.1
RUN mkdir -p /root/task /root/solution /logs/verifier
# Held-out verification data to strictly satisfy Anti-Cheat and Trust Boundary
RUN echo ">seqA\nGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGC\n>seqB\nGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGC\n>seqC\nGCGCGCGCGCGCGCATGCGCGCGCGCGCGCGCGCGCGCGCGC" > /root/task/alignment.fasta
COPY . /tests/
WORKDIR /tests