# Configuración del tablero GitHub Projects

## Objetivo

Reproducir el tablero de seguimiento del repositorio de referencia para el **Programa integral para fortalecer la permanencia estudiantil**. Este documento prepara la configuración sin afirmar que el tablero ya existe.

**Nombre sugerido:** Seguimiento - Programa integral para fortalecer la permanencia estudiantil

**Tipo:** GitHub Projects, vista **Board**.

## Columnas de estado

1. **Pendiente:** actividades todavía no iniciadas o sin información institucional.
2. **En curso:** actividades de formulación, organización o revisión que están en desarrollo.
3. **Validado:** entregables con comprobación documental o revisión efectuada. No usar si todavía no hay evidencia.
4. **Listo para GitHub:** insumos completamente preparados y revisados para su publicación.

## Issues que debes incorporar

| Issue | Actividad | Estado de trabajo inicial |
| --- | --- | --- |
| [#1](../../issues/1) | Diagnóstico institucional | Pendiente |
| [#16](../../issues/16) | Recopilar indicadores de permanencia | Pendiente |
| [#17](../../issues/17) | Identificar apoyos existentes | Pendiente |
| [#2](../../issues/2) | Formular problema y objetivos | En curso |
| [#12](../../issues/12) | Delimitar población objetivo | Pendiente |
| [#13](../../issues/13) | Precisar alcance y objetivos | En curso |
| [#3](../../issues/3) | Diseñar estrategias de permanencia | En curso |
| [#14](../../issues/14) | Priorizar alternativas | En curso |
| [#18](../../issues/18) | Revisar apoyos y duplicidades | Pendiente |
| [#4](../../issues/4) | Seguimiento y evaluación | Pendiente |
| [#15](../../issues/15) | Registrar avances, evidencias y riesgos | En curso |
| [#19](../../issues/19) | Definir indicadores de evaluación | Pendiente |

Estas ubicaciones son **iniciales y provisionales**, no certificados de ejecución.

## Cómo crear el tablero en la cuenta correcta

1. Abre [Projects del usuario karenlegro00-dot](https://github.com/users/karenlegro00-dot/projects).
2. Selecciona **New project** y luego **Board**.
3. Escribe el nombre sugerido arriba y crea el proyecto.
4. Abre su campo **Status** y configura las opciones **Pendiente**, **En curso**, **Validado** y **Listo para GitHub**.
5. Agrega los 12 Issues del repositorio `karenlegro00-dot/PROYECTO` usando la opción de añadir elementos de repositorio.
6. Ubica cada uno según la columna indicada en la tabla.
7. Vincula el tablero al repositorio y agrega **su URL real** en el apartado `## Seguimiento del proyecto` del README principal.

**Nota de permisos:** GitHub Projects es una función independiente del repositorio. La automatización normal con `GITHUB_TOKEN` no permite crear un Project de usuario ni editar sus campos sin un permiso específico de Projects. No almacenes contraseñas ni tokens en archivos de este repositorio.

## Finalización

La carpeta `04_Finalizacion/` se conserva sin documentos finales. Como GitHub no almacena carpetas completamente vacías, incluye solo un archivo `README.md` de un salto de línea, igual que el ejemplo. No añadir resultados ni actas hasta que el proyecto termine.
