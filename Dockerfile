# Build frontend
FROM node:20 AS frontend-build
WORKDIR /app
COPY frontend ./frontend
RUN cd frontend && npm install && npm run build

# Backend + static host
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY agents /app/agents
COPY --from=frontend-build /app/frontend/dist /app/frontend_dist
COPY start.sh .

CMD ["./start.sh"]
