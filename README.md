# ProyectoU
# Documento de Diseño de la Solución: Generador de Configuración para Plataforma A

## Arquitectura del Sistema

El sistema utiliza una arquitectura hexagonal (puertos y adaptadores) para lograr una separación clara de responsabilidades y facilitar la extensibilidad y mantenibilidad del código.

```
                 +-------------------+
                 |                   |
    +------------+  Interfaz de      |
    |            |  Usuario          |
    |            |  (Streamlit)      |
    |            |                   |
    |            +--------+----------+
    |                     |
    |            +--------v----------+
    |            |                   |
    |            |  Adaptadores      |
    |            |                   |
    |            +--------+----------+
    |                     |
    |            +--------v----------+
    |            |                   |
    |            |  Puertos          |
    |            |                   |
    |            +--------+----------+
    |                     |
    |            +--------v----------+
    |            |                   |
    |            |  Dominio          |
    |            |                   |
    |            +--------+----------+
    |                     |
    |            +--------v----------+
    |            |                   |
    +------------>  Adaptadores      |
                 |  Externos         |
                 |                   |
                 +-------------------+
```

## Componentes Principales

1. **Interfaz de Usuario (Streamlit)**
   - Implementado en `main.py`
   - Proporciona la interfaz web para la interacción del usuario

2. **Adaptadores**
   - `StreamlitAdapter`: Conecta la interfaz de Streamlit con el dominio
   - `FileAdapter`: Maneja las operaciones de lectura/escritura de archivos
   - `ClaudeAdapter`: Interactúa con la API de Claude para generar configuraciones

3. **Puertos**
   - Definen interfaces para los adaptadores, permitiendo la inversión de dependencias

4. **Dominio**
   - `ConfigurationService`: Contiene la lógica principal para generar prompts y configuraciones

5. **Adaptadores Externos**
   - API de Claude: Servicio externo para generación de texto

## Flujo de Datos

1. El usuario carga archivos y configura parámetros a través de la interfaz Streamlit.
2. Los datos se pasan al `ConfigurationService` a través de los adaptadores.
3. El `ConfigurationService` genera un prompt utilizando los datos de entrada.
4. El prompt se envía al `ClaudeAdapter` para generar la configuración.
5. La respuesta se devuelve al usuario a través de la interfaz Streamlit.

## Ventajas de la Arquitectura

- **Separación de Responsabilidades**: Cada componente tiene una función específica y bien definida.
- **Flexibilidad**: Fácil de adaptar a cambios en la interfaz de usuario o en servicios externos.
- **Testabilidad**: La estructura permite probar cada componente de forma aislada.
- **Mantenibilidad**: Los cambios en un componente tienen un impacto mínimo en otros componentes.

# Propuesta de Pruebas para el Generador de Configuración de la Plataforma A

## 1. Pruebas Unitarias

### 1.1 FileAdapter
- Probar el método `read_file` con diferentes tipos de contenido
- Verificar el manejo de errores para archivos no existentes o inaccesibles

### 1.2 ClaudeAdapter
- Probar el método `generate_response` con diferentes prompts
- Verificar el manejo de errores de la API (uso de mocks)
- Comprobar la correcta aplicación de los parámetros de temperatura y max_tokens

### 1.3 ConfigurationService
- Probar el método `generate_prompt` con diferentes contenidos de archivo
- Verificar la correcta formación del prompt final
- Probar el método `generate_configuration` con diferentes inputs

## 2. Pruebas de Integración

### 2.1 Integración FileAdapter - ConfigurationService
- Verificar la correcta lectura de archivos y generación de prompts

### 2.2 Integración ClaudeAdapter - ConfigurationService
- Comprobar la correcta comunicación entre el servicio y la API de Claude

### 2.3 Integración StreamlitAdapter - ConfigurationService
- Verificar la correcta presentación de datos en la interfaz de usuario

## 3. Pruebas de Aceptación del Usuario

### 3.1 Funcionalidad completa
- Cargar archivos de entrada, plantilla y reglas
- Generar una configuración
- Verificar que la configuración generada cumpla con las reglas especificadas

### 3.2 Usabilidad de la interfaz
- Comprobar la facilidad de uso de la carga de archivos
- Verificar la claridad de la presentación de resultados

### 3.3 Manejo de errores
- Probar el comportamiento del sistema con archivos de entrada inválidos
- Verificar mensajes de error claros y útiles

## 4. Pruebas de Rendimiento

### 4.1 Tiempo de respuesta
- Medir el tiempo de generación de configuraciones para diferentes tamaños de entrada

### 4.2 Concurrencia
- Probar el comportamiento del sistema con múltiples usuarios simultáneos

## 5. Pruebas de Seguridad

### 5.1 Manejo seguro de API keys
- Verificar que la API key de Claude no se exponga en la interfaz de usuario

### 5.2 Validación de entradas
- Comprobar que el sistema valide y sanitize adecuadamente las entradas del usuario

## Herramientas Recomendadas

- Pruebas Unitarias: pytest
- Pruebas de Integración: pytest con fixtures
- Pruebas de Aceptación: Selenium para automatización de UI
- Pruebas de Rendimiento: Locust para pruebas de carga
- Pruebas de Seguridad: OWASP ZAP para análisis de vulnerabilidades

## Plan de Ejecución

1. Desarrollar y ejecutar pruebas unitarias durante el desarrollo de cada componente
2. Realizar pruebas de integración al completar grupos de componentes relacionados
3. Ejecutar pruebas de aceptación del usuario antes de cada release
4. Realizar pruebas de rendimiento y seguridad antes del despliegue a producción
5. Implementar integración continua para ejecutar pruebas automáticamente en cada commit

   # Manual de Usuario: Generador de Configuración para Plataforma A

## 1. Introducción

El Generador de Configuración para Plataforma A es una herramienta que permite crear archivos de configuración personalizados basados en plantillas y reglas predefinidas. Esta guía le ayudará a utilizar la plataforma de manera efectiva.

## 2. Preparación de Archivos

Antes de comenzar, prepare los siguientes archivos:

1. **entrada.txt**: Contiene los datos de entrada para la configuración.
2. **plantilla.txt**: Define la estructura base del archivo de configuración.
3. **reglas.txt**: Especifica las reglas para asignar valores a los campos de la plantilla.

Asegúrese de que estos archivos estén en formato .txt y contengan la información correcta según las especificaciones del sistema.

## 3. Acceso a la Plataforma

1. Abra su navegador web y vaya a la URL proporcionada para la aplicación.
2. Verá la interfaz del Generador de Configuración para Plataforma A.

## 4. Carga de Archivos

1. En la barra lateral izquierda, busque la sección "📁 Cargar Archivos".
2. Haga clic en "Seleccionar archivos" o arrastre y suelte los archivos entrada.txt, plantilla.txt y reglas.txt.
3. Asegúrese de que los tres archivos estén cargados correctamente.

## 5. Configuración de Parámetros

1. En la barra lateral, encuentre la sección "⚙️ Configuración de Hiperparámetros".
2. Ajuste el parámetro "Temperature" según sus necesidades:
   - Valores más bajos (cerca de 0) producen resultados más deterministas.
   - Valores más altos (cerca de 1) producen resultados más variados y creativos.
3. Configure "Max Tokens" para establecer el límite máximo de tokens en la respuesta generada.

## 6. Generación de la Configuración

1. Una vez cargados los archivos y configurados los parámetros, haga clic en el botón "🚀 Generar Configuración" en la columna derecha de la pantalla principal.
2. Espere mientras el sistema procesa su solicitud. Verá un indicador de "Generando configuración...".

## 7. Revisión de Resultados

1. Una vez completado el proceso, verá el archivo de configuración generado en el área de texto de la columna derecha.
2. Revise cuidadosamente el contenido generado para asegurarse de que cumple con sus expectativas y requisitos.

## 8. Visualización del Prompt

1. Si desea ver el prompt utilizado para generar la configuración, puede expandir la sección "🔍 Ver Prompt Generado" en la parte superior de la pantalla.
2. Esto le permitirá entender mejor cómo se procesaron sus datos de entrada.

## 9. Descarga del Archivo de Configuración

1. [Nota: Esta funcionalidad no está implementada en el código actual, pero se sugiere como una mejora futura]
2. Debería haber un botón o enlace para descargar el archivo de configuración generado.
3. Haga clic en este botón/enlace para guardar el archivo en su dispositivo.

## 10. Manejo de Errores

- Si encuentra algún error durante el proceso, se mostrará un mensaje en rojo explicando el problema.
- Verifique que los archivos de entrada sean correctos y estén en el formato adecuado.
- Asegúrese de que todos los archivos necesarios (entrada.txt, plantilla.txt, reglas.txt) estén cargados.

## 11. Consejos Adicionales

- Para obtener los mejores resultados, asegúrese de que sus archivos de entrada sean claros y sigan el formato esperado.
- Experimente con diferentes valores de "Temperature" para encontrar el balance adecuado entre consistencia y creatividad en las configuraciones generadas.
- Si no está satisfecho con el resultado, puede ajustar los parámetros y generar una nueva configuración.

## 12. Soporte

Si encuentra problemas o tiene preguntas adicionales sobre el uso de la plataforma, por favor contacte al equipo de soporte técnico.
 
