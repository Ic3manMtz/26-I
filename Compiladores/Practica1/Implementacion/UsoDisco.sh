#!/bin/bash

echo ""
echo "+------------------------+"
echo "|USO DE DISCO DEL SISTEMA|"
echo "+------------------------+"
df -h

echo ""
echo "+-------------------------------+"
echo "|Identificaciones de porcentajes|"
echo "+-------------------------------+"
df -h | grep -E "[0-9]{1,3}%"

echo ""
echo "+------------------------+"
echo "|USO DE DISCO MAYOR A 80%|"
echo "+------------------------+"
df -h | grep -E "([8-9][0-9]|100)%"




