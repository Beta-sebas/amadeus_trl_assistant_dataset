# AMADEUS_TRL_DATASET
**AMADEUS_TRL_DATASET** es un conjunto de datos diseñado para entrenar asistentes inteligentes en la evaluación del Nivel de Preparación Tecnológica (TRL) en el campo de la agricultura, utilizando la métrica TRL desarrollada por la NASA. El dataset está organizado en dos partes:

* Dataset de Conocimiento Conceptual: Incluye información sobre los conceptos y definiciones del TRL, los niveles, objetivos y metas de cada nivel, así como las actividades de desarrollo tecnológico relacionadas. Este dataset proporciona una base de conocimiento esencial para entender y aplicar la métrica TRL.

* Dataset de Evaluación: Contiene flujos de conversación diseñados para simular evaluaciones del TRL en todos sus niveles. Estos flujos consisten en pares de pregunta-respuesta, permitiendo al asistente virtual ofrecer evaluaciones, estimaciones y recomendaciones sobre el nivel TRL de una tecnología en el ámbito agrícola.

La estrategia para la estimación inicial del TRL se llevó a cabo mediante un algoritmo desarrollado con base en los resultados del artículo [1] titulado "Development of a Telegram Bot to Determine the Level of Technological Readiness".

![diagrama_flujo_evaluacion_inicial](https://github.com/user-attachments/assets/9f9eb3c5-496e-407d-9eaa-867ae7206b59)

Los datos incluidos en este proyecto provienen de diversas fuentes confiables, como entidades gubernamentales, universidades así como herramientas de cálculo del TRL y la NASA. Estas fuentes garantizan la veracidad y la calidad de la información proporcionada.

>Este dataset fue utilizado para entrenar el asistente virtual [AMADEUS](https://github.com/afcoral124/chatbot-telegram-gpt3.5) utilizado para evaluar el nivel de madures de tecnologías en el campo de la agricultura.
## Formato del dataset

Se adoptaron dos tipos de formato para ofrecer compatibilidad con todo tipo de modelos y librerías, Los datasets de prueba y validación se publican en el formato JSON Lines.

* Compatible con [llama-2-7b-chat-hf](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf) y similares
```
amadeus_TRL_DATASET_LLAMA2_CONCEPTUAL.jsonl
├── [i]
│   ├── "prompt" : "user request"
│   └── "response": "model response"    
``` 

* Compatible con [GPT-3.5-turbo](https://platform.openai.com/docs/models/gpt-3-5-turbo)
```
amadeus_TRL_DATASET_GPT3.5TURBO.jsonl
├── [i]
|   └── "messages"
│        ├── [0]
│        │   ├── "role": "system"
│        │   └── "content": "System message content."
│        ├── [1]
│        |   ├── "role": "user"
│        |   └── "content": "User message content."
│        └── [2]
│            ├── "role": "assistant"
│            └── "content": "Assistant response content."
```
## Referencias

[1] D. I. Suntsova, V. A. Pavlov, Z. V. Makarenko, P. P. Bakholdin, A. S. Politsinsky, A. S. Kremlev, A. A. Margun., “Development of a Telegram Bot to Determine the Level of Technological Readiness,”  Economics of Science. 2022;8(1):22-30. (In Russ.), doi:  10.22394/2410-132X-2022-8-1-22-30.

[2] MinCiencias and Actores del Sistema Nacional de Ciencia, Tecnología e Innovación, "EL MINISTERIO DE CIENCIA, TECNOLOGÍA E INNOVACIÓN CONVOCATORIA PARA EL APOYO A PROYECTOS DE I+D+i QUE CONTRIBUYAN A RESOLVER LOS DESAFÍOS ESTABLECIDOS EN LA MISIÓN 'COLOMBIA HACIA UN NUEVO MODELO PRODUCTIVO, SOSTENIBLE Y COMPETITIVO'-ÁREA ESTRATÉGICA ENER," 2022. Available: https://minciencias.gov.co/sites/default/files/upload/convocatoria/anexo_9_-_niveles_de_madurez_tecnologica_y_de_manufactura-_trl_y_mrl.pdf. [Accessed: Jan. 27, 2024].

[3] J. M. I. de A. Quintana, "NIVELES DE MADUREZ DE LA TECNOLOGÍA. TECHNOLOGY READINESS LEVELS. TRLS," 2015. Available: https://www.mintur.gob.es/publicaciones/publicacionesperiodicas/economiaindustrial/revistaeconomiaindustrial/393/notas.pdf. [Accessed: Jan. 27, 2024].

[4] NASA, "Technology Readiness Level Definitions," 2015. Available: https://www.nasa.gov/wp-content/uploads/2017/12/458490main_trl_definitions.pdf. [Accessed: Jan. 27, 2024].

[5] Universidad Nacional de Colombia, "GUÍA PARA LA IDENTIFICACIÓN DEL GRADO DE MADUREZ (TRL)," 2019. Available: https://minas.medellin.unal.edu.co/cdi/images/Procedimientos/MCDIIFMiGU001_Guia_para_la_identificacion_del_grado_de_madurez_TRL.pdf. [Accessed: Jun. 22, 2023].

[6] Universidad de Caldas, "ANEXO 1. TECHNOLOGY READINESS LEVELS-TRL," 2016. Available: https://www.nasa.gov/directorates/heo/scan/engineering/technology/txt_accordion1.html. [Accessed: Jan. 27, 2024].