#!/bin/bash

# Archivo de entrada con datos (uno por línea)
INPUT="datos.txt"

# Expresiones regulares
regex_email='^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
regex_tel='^[0-9]{3}-[0-9]{3}-[0-9]{4}$'

while IFS= read -r line; do
  if [[ $line =~ $regex_email ]]; then
    echo "EMAIL válido: $line"
  elif [[ $line =~ $regex_tel ]]; then
    echo "TELÉFONO válido: $line"
  else
    echo "Formato desconocido: $line"
  fi
done < "$INPUT"

