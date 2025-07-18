FROM python:3.11-slim

# Install Gemini CLI
RUN apt-get update && apt-get install -y curl bash \
 && curl -sSL https://g.co/cli/install | bash

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["python", "kernel.py"]
