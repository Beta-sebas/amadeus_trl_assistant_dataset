import json

# Archivos de entrada y salida
input_file = 'TRL_EVALUATIONS_DATASET.jsonl'
output_file = 'amadeus_TRL_DATASET_LLAMA2_EVALUATION.jsonl'

# Lista para almacenar los datos formateados
formatted_data = []

# Leer y procesar el archivo de entrada
with open(input_file, 'r') as f:
    for line in f:
        conversation = json.loads(line.strip())
        messages = conversation["messages"]
        prompt = ""
        response = ""
        for message in messages:
            if message["role"] == "user":
                if prompt:  # Si ya hay un prompt, guardar la conversación anterior
                    formatted_data.append({"prompt": prompt, "response": response})
                    prompt = ""  # Reiniciar prompt y response para la siguiente conversación
                    response = ""
                prompt = message["content"]
            elif message["role"] == "assistant":
                response = message["content"]
        
        # Agregar la última conversación si no se ha agregado
        if prompt and response:
            formatted_data.append({"prompter": prompt, "assistant": response})

# Escribir los datos formateados en el archivo de salida
with open(output_file, 'w') as f:
    for item in formatted_data:
        f.write(json.dumps(item) + '\n')

print(f"Los datos han sido procesados y guardados en '{output_file}'.")
