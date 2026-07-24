FROM python:3.10-slim

WORKDIR /app

# Upgrade base tooling to patch vendored vulnerabilities (CVE-2026-23949 & CVE-2026-24049)
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
