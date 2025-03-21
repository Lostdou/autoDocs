# autoDocs by lostdou

## Descripción

autoDocs es una herramienta para la generación automática de documentos a partir de datos ingresados por el usuario.
Sirve para generar documentos simples como notas, solicitudes y demas.

## Características

- Generación automática de documentos.
- Interfaz gráfica de usuario (GUI) para la entrada de datos.
- Integración con plantillas de documentos de Word.

## Instalación

Para instalar las dependencias necesarias, ejecuta el siguiente comando:

```bash
pip install -r requirements.txt
```

## Uso

Para ejecutar la aplicación, utiliza el siguiente comando:

```bash
python app.py
```

## Estructura del Proyecto

- `app.py`: Archivo principal que inicia la interfaz gráfica de usuario.
- `scripts/planilla_asistencia.py`: Script para generar planillas de asistencia.
- `planillas-asistencia/`: Carpeta donde se guardan las planillas de asistencia generadas.

## Contribuir

Si deseas contribuir a este proyecto (agregando mas tipos de documentos, o no se), por favor sigue los siguientes pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añadir nueva funcionalidad'`).
4. Sube tus cambios (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.
