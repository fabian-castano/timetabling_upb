# Tesis: Un nuevo proceso secuencial para la asignación de clases y docentes en la UPB Palmira


## Resumen


## 1. Introducción

1. El problema de programación académica
2. Problemas combinatorios parecidos
3. Características de los problemas de proramación académica:

   1. Qué se decide?
   2. cuáles son los componentes del problema de optimización implícito:
      * conjuntos
      * variables
      * Restriccciones
      * objetivo
   3. Complejidad de los problemas de programación académica
4. El problema de programación académica en la UPB:

   * Características de la planeación en la UPB.
   * Qué lo hace restrictivo: disponibilidad de salores, disponibilidad docentes.
   * Qué lo hace diferente?
     * Clases que se programan en bloques una vez por semana
     * lo que se le ocurrra a William
   * Cómo se hace actualmente?
     * Método manual
     * consume mucho tiempo
     * conduce a reprogramaciones
5. Objetivo del proyecto:

   1. Proponer un nuevo proceso de progrramación que permita facilitar el proceso de programación académica
   2. El nuevo proceso se compone de múltiples etapas y formalizan, además de complementarse mediante modelos d eprogramación matemática, la programación académica en la UPB:
      * Preprocesamiento:  Estruturación de la informaicón no estructurada para su consumo en los modelos de optimización. (Nosotros lo llevamos a archivos json)
      * Asignación de docentes a cursos: Etapa en la que se busca que los docentes sean asignados a cursos para los que estén capacitados, al tiempo que se busca balancear el número de horas asignadas y cumplir con las especificaciones reglamentarias de la universidad.
      * Asignación de cursos a salones:  Se busca asignar el espacio para las clases que respete los requerimientos de la clase y los horarios del docente que debe dictar el curso
      * Eliminación de infactibilidades: El proceso de optimización incluye una fase de identificación de potenciales causantes de infactibilidad para proceder, de manera iterativa, a mejorar la calidad de las asignaciones.
6. _Descripción de la estructura del documento de tesis. Qué se presenta en cada sección._

# 2. Estado del Arte

Incluyendo el análisis de redes con VosViewer, temas de moda y recientes investigaciones -*SER JUICIOSO CON LAS REFERENCIAS*

## 3. Descripción del problema

1. Detalles del procesamiento y programación de clases en la UPB
2. Descripción detallada de las restricciones (no matemática) de la programación en la UPB

### 4. Descricpión matemática del problema y Modelo matemático

* Enumeración de las fases de programación académica (propuestas)
* *Fase II Modelo  asignación profes a clases (ModeloWilliam)* Descripción matemática de:

  * Conjuntos sobre los que se decide
  * variables de decisión
  * Restricciones que se deben cumplir
  * Objetivo (s)
  * Modelo matemático completo
* *Fase III Modelo asignación de cursos a salones*

  * Conjuntos sobre los que se decide
  * variables de decisión
  * Restricciones que se deben cumplir
  * Objetivo (s)
  * Modelo matemático completo

# 5. Detalles experimentales y resultados

# 6. Conclusiones
