
#  Kata Bowling game

1. [Introducción](#introducción)
2. [Requisitos del Sistema](#requisitos-del-sistema)
3. [Diseño de la Solución](#diseño-de-la-solución)
4. [Arquitectura Basada en DDD (Domain‑Driven Design)](#arquitectura-basada-en-ddd-domain-driven-design)
5. [Implementación Paso a Paso](#implementación-paso-a-paso)
6. [Casos de Prueba](#casos-de-prueba)
7. [Refactorización](#refactorización)
8. [Conclusiones](#conclusiones)
9. [Recursos y Referencias](#recursos-y-referencias)

## Introducción
Tomas Santiago Orellano - @T0T11 Jorge Pazos Domiguez - @jrgeepd
Somos alumnos de Desarollo de Aplicaciones Multiplataforma del IES de Teis. Hicimos este kata de @emilybache con el fin de afianzar el dominio de la programacion orientada a objetos



## Requisitos del Sistema
Requiere python = >=3.11 requiere pipx 1.8.0 o mayor Entorno virtual ( opcional, pero muy recomedable).Con el entorno Virtual ya instalado (python3 -m venv venv) y activado, tienes que escribir 
'''git clone https://github.com/jrgeepdbowling-game-kata y instalas las dependencias con el comando '''pip install -r requirements.txt

## Diseño de la Solución
El proyecto implementa la lógica completa de puntuación de un juego de bolos siguiendo principios de POO.

Clases principales:

ScoreCard: interpreta la cadena de tiradas y calcula la puntuación total

Frame: representa cada turno y determina si es strike o spare

Roll: representa cada tiro individual

Principios aplicados:

Encapsulación

Responsabilidad única (SRP)

Abstracción

Código expresivo y alineado con el dominio

## Diseño de la Solución
El proyecto implementa la lógica completa de puntuación de un juego de bolos siguiendo principios de POO.

Clases principales:

ScoreCard: interpreta la cadena de tiradas y calcula la puntuación total

Frame: representa cada turno y determina si es strike o spare

Roll: representa cada tiro individual

Principios aplicados:

Encapsulación

Responsabilidad única (SRP)

Abstracción

Código expresivo y alineado con el dominio

## Implementación Paso a Paso
Interpretación de la cadena de tiradas (X, /, -, números)

Conversión a lista numérica (get_rolls())

Identificación de strikes y spares

Cálculo de bonus según reglas oficiales

Gestión del décimo frame y tiradas extra

Validación mediante tests unitarios

Refactorización para mejorar claridad y cohesión

## Casos de Prueba
Los  casos cubren tiradas normales, símbolos especiales, spares, strikes, dobles, triples y tiradas extra del décimo frame.

## Refactorización
Mejoras aplicadas:

Separación clara entre interpretación de tiradas y cálculo de puntuación

Eliminación de duplicación en strikes y spares

Métodos privados para mejorar legibilidad

Simplificación del décimo frame

Código más expresivo y alineado con el lenguaje del dominio

## Conclusiones
Este kata nos permitió:

Practicar POO de forma estricta

Aplicar DDD en un dominio pequeño pero real

Comprender la importancia del lenguaje ubicuo

Mejorar la calidad del código mediante refactorización continua

Validar el diseño mediante una batería completa de tests

## Recursos y Referencias
Kata original de Emily Bache

Documentación oficial de Python

Domain‑Driven Design — Eric Ev
