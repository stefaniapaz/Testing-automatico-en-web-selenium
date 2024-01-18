# Testing-automatico-en-web-selenium
Este script de Python utiliza Selenium y Faker para automatizar el llenado de un formulario web. En este ejemplo, se ha utilizado la página de demostración de "text-box" de demoqa.com. El script llena los campos del formulario con datos aleatorios generados por Faker y envía el formulario.

## Requisitos

Antes de ejecutar el script, asegúrate de tener instalados los siguientes paquetes:

- Selenium: Puedes instalarlo usando `pip install selenium`
- Faker: Puedes instalarlo usando `pip install faker`
- Webdriver: Necesitas tener un controlador del navegador, en este caso, se ha utilizado ChromeDriver. Asegúrate de descargar la versión compatible con tu navegador desde [la página oficial](https://sites.google.com/chromium.org/driver/).

## Integración con Jenkins
Este script puede ser integrado con Jenkins para realizar pruebas de estrés de manera automatizada.Para configurar un trabajo en Jenkins para ejecutar el script en diferentes entornos y evaluar el rendimiento de la aplicación a cierta hora deberas hacer lo siguiente:

1.Crea un nuevo trabajo en Jenkins:

- Ve a tu panel de Jenkins y haz clic en "Nuevo trabajo" o "Nueva tarea".
- Ingresa un nombre para tu trabajo y selecciona "Crear un proyecto de estilo libre".
- Busca la sección llamada "Construir Triggers" o "Build Triggers".
- Marca la opción "Build periodically" o similar.
- En el campo de entrada, ingresa la expresión cron correspondiente a las 6 de la mañana todos los días. En la expresión cron, el formato típico sería: `H 6 * * *`

2.Configura el trabajo:

- En la sección "Configuración del trabajo", ve a la parte inferior donde dice "Construir" o "Build".
- Añade un paso de construcción "Ejecutar script de shell" o "Execute Windows batch command", según tu entorno.
- Escribe el comando para ejecutar tu script de prueba

   ```bash
    python /ruta/a/tu/script.py
