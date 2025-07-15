#!/bin/bash

# ALENYA Deployment Script para Linux/macOS
# MELANO INC - Versión 3.0.0

echo "🚀 Iniciando deployment de ALENYA..."
echo "================================================"

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Función para logging
log() {
    echo -e "${BLUE}[$(date +'%Y-%m-%d %H:%M:%S')]${NC} $1"
}

error() {
    echo -e "${RED}[ERROR]${NC} $1"
    exit 1
}

success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

# Verificar Python
log "Verificando Python..."
if ! command -v python3 &> /dev/null; then
    error "Python3 no está instalado"
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
log "Python encontrado: $PYTHON_VERSION"

# Verificar pip
log "Verificando pip..."
if ! command -v pip3 &> /dev/null; then
    error "pip3 no está instalado"
fi

# Crear entorno virtual si no existe
if [ ! -d "venv" ]; then
    log "Creando entorno virtual..."
    python3 -m venv venv
    success "Entorno virtual creado"
else
    log "Entorno virtual ya existe"
fi

# Activar entorno virtual
log "Activando entorno virtual..."
source venv/bin/activate

# Actualizar pip
log "Actualizando pip..."
pip install --upgrade pip

# Instalar dependencias
log "Instalando dependencias..."
pip install -r requirements.txt
success "Dependencias instaladas"

# Crear archivo .env si no existe
if [ ! -f ".env" ]; then
    log "Creando archivo .env..."
    cp .env.example .env
    warning "Archivo .env creado desde template. Configura tus variables antes de production."
else
    log "Archivo .env ya existe"
fi

# Verificar archivos principales
log "Verificando archivos principales..."
for file in "alenya_agent.py" "app.py" "templates/index.html"; do
    if [ ! -f "$file" ]; then
        error "Archivo requerido no encontrado: $file"
    fi
done
success "Todos los archivos principales encontrados"

# Test de importación
log "Probando importación de ALENYA..."
python3 -c "from alenya_agent import AlenyaAgent; print('✅ ALENYA importada correctamente')" || error "Error importando ALENYA"

# Función para deployment en desarrollo
deploy_development() {
    log "🔧 Deployment en modo DESARROLLO"
    export FLASK_ENV=development
    export DEBUG=True
    
    log "Iniciando servidor de desarrollo..."
    python3 app.py
}

# Función para deployment en producción
deploy_production() {
    log "🚀 Deployment en modo PRODUCCIÓN"
    export FLASK_ENV=production
    export DEBUG=False
    
    # Verificar gunicorn
    if ! command -v gunicorn &> /dev/null; then
        log "Instalando gunicorn..."
        pip install gunicorn
    fi
    
    log "Iniciando servidor de producción con gunicorn..."
    gunicorn --bind 0.0.0.0:5000 --workers 4 --timeout 120 app:app
}

# Función para deployment con Docker
deploy_docker() {
    log "🐳 Deployment con Docker"
    
    if ! command -v docker &> /dev/null; then
        error "Docker no está instalado"
    fi
    
    # Crear Dockerfile si no existe
    if [ ! -f "Dockerfile" ]; then
        log "Creando Dockerfile..."
        cat > Dockerfile << EOF
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "app:app"]
EOF
        success "Dockerfile creado"
    fi
    
    log "Construyendo imagen Docker..."
    docker build -t alenya:3.0.0 .
    
    log "Ejecutando contenedor..."
    docker run -d -p 5000:5000 --name alenya-container alenya:3.0.0
    
    success "ALENYA ejecutándose en Docker en puerto 5000"
}

# Menu principal
echo ""
echo "Selecciona el tipo de deployment:"
echo "1) Desarrollo (Flask dev server)"
echo "2) Producción (Gunicorn)"
echo "3) Docker"
echo "4) Solo preparar entorno"
echo ""
read -p "Opción [1-4]: " choice

case $choice in
    1)
        deploy_development
        ;;
    2)
        deploy_production
        ;;
    3)
        deploy_docker
        ;;
    4)
        success "Entorno preparado correctamente"
        log "Para iniciar manualmente: python3 app.py"
        ;;
    *)
        error "Opción inválida"
        ;;
esac

echo ""
echo "================================================"
success "🎉 ALENYA deployment completado!"
echo "🌐 Accede a: http://localhost:5000"
echo "📚 Documentación API: http://localhost:5000/api/status"
echo "💬 Chat Interface: http://localhost:5000"
echo "================================================"
