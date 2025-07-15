@echo off
:: ALENYA Deployment Script para Windows
:: MELANO INC - Versión 3.0.0

echo 🚀 Iniciando deployment de ALENYA...
echo ================================================

:: Configurar colores
for /F "tokens=1,2 delims=#" %%a in ('"prompt #$H#$E# & echo on & for %%b in (1) do rem"') do (set "DEL=%%a")

:: Función para logging
:log
echo [%time%] %~1
goto :eof

:error
echo [ERROR] %~1
pause
exit /b 1

:success
echo [SUCCESS] %~1
goto :eof

:warning
echo [WARNING] %~1
goto :eof

:: Verificar Python
call :log "Verificando Python..."
python --version >nul 2>&1
if %errorlevel% neq 0 (
    call :error "Python no está instalado o no está en PATH"
)

for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
call :log "Python encontrado: %PYTHON_VERSION%"

:: Verificar pip
call :log "Verificando pip..."
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    call :error "pip no está instalado"
)

:: Crear entorno virtual si no existe
if not exist "venv" (
    call :log "Creando entorno virtual..."
    python -m venv venv
    call :success "Entorno virtual creado"
) else (
    call :log "Entorno virtual ya existe"
)

:: Activar entorno virtual
call :log "Activando entorno virtual..."
call venv\Scripts\activate.bat

:: Actualizar pip
call :log "Actualizando pip..."
python -m pip install --upgrade pip

:: Instalar dependencias
call :log "Instalando dependencias..."
pip install -r requirements.txt
if %errorlevel% neq 0 (
    call :error "Error instalando dependencias"
)
call :success "Dependencias instaladas"

:: Crear archivo .env si no existe
if not exist ".env" (
    call :log "Creando archivo .env..."
    copy .env.example .env
    call :warning "Archivo .env creado desde template. Configura tus variables antes de production."
) else (
    call :log "Archivo .env ya existe"
)

:: Verificar archivos principales
call :log "Verificando archivos principales..."
if not exist "alenya_agent.py" call :error "Archivo requerido no encontrado: alenya_agent.py"
if not exist "app.py" call :error "Archivo requerido no encontrado: app.py"
if not exist "templates\index.html" call :error "Archivo requerido no encontrado: templates\index.html"
call :success "Todos los archivos principales encontrados"

:: Test de importación
call :log "Probando importación de ALENYA..."
python -c "from alenya_agent import AlenyaAgent; print('✅ ALENYA importada correctamente')"
if %errorlevel% neq 0 call :error "Error importando ALENYA"

:: Menu principal
echo.
echo Selecciona el tipo de deployment:
echo 1) Desarrollo (Flask dev server)
echo 2) Producción (Waitress)
echo 3) Solo preparar entorno
echo.
set /p choice=Opción [1-3]: 

if "%choice%"=="1" goto :deploy_development
if "%choice%"=="2" goto :deploy_production
if "%choice%"=="3" goto :prepare_only
call :error "Opción inválida"

:deploy_development
call :log "🔧 Deployment en modo DESARROLLO"
set FLASK_ENV=development
set DEBUG=True

call :log "Iniciando servidor de desarrollo..."
python app.py
goto :end

:deploy_production
call :log "🚀 Deployment en modo PRODUCCIÓN"
set FLASK_ENV=production
set DEBUG=False

call :log "Verificando waitress..."
pip show waitress >nul 2>&1
if %errorlevel% neq 0 (
    call :log "Instalando waitress..."
    pip install waitress
)

call :log "Iniciando servidor de producción con waitress..."
waitress-serve --host=0.0.0.0 --port=5000 app:app
goto :end

:prepare_only
call :success "Entorno preparado correctamente"
call :log "Para iniciar manualmente: python app.py"
goto :end

:end
echo.
echo ================================================
call :success "🎉 ALENYA deployment completado!"
echo 🌐 Accede a: http://localhost:5000
echo 📚 Documentación API: http://localhost:5000/api/status
echo 💬 Chat Interface: http://localhost:5000
echo ================================================
pause
