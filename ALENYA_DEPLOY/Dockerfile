# ALENYA Docker Image
# MELANO INC - Versión 3.0.0

FROM python:3.11-slim

# Metadata
LABEL maintainer="MELANO INC <dev@melano-inc.com>"
LABEL version="3.0.0"
LABEL description="ALENYA - El Agente IA Más Avanzado del Mundo"

# Variables de entorno
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV FLASK_APP=app.py
ENV FLASK_ENV=production
ENV PORT=5000

# Crear directorio de trabajo
WORKDIR /app

# Crear usuario no-root para seguridad
RUN groupadd -r alenya && useradd -r -g alenya alenya

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements y instalar dependencias Python
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copiar código de la aplicación
COPY . .

# Crear directorio para logs
RUN mkdir -p /app/logs && \
    chown -R alenya:alenya /app

# Cambiar a usuario no-root
USER alenya

# Healthcheck
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:${PORT}/api/status || exit 1

# Exponer puerto
EXPOSE $PORT

# Comando por defecto
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "--timeout", "120", "--access-logfile", "-", "--error-logfile", "-", "app:app"]
