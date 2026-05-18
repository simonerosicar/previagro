# PREVIAGRO - Product Requirements Document (PRD)

## Problema

Agricultores e técnicos têm dificuldade para acessar informações de previsão agrícola de forma organizada, segura e centralizada. Os dados de produtores e previsões estão dispersos, o que prejudica o tomada de decisão operacional.

## Solução

Uma API backend simples e modular que permite o cadastro de usuários, autenticação segura com JWT e gerenciamento de dados agrícolas pelo CRUD de produtores. A solução organiza previsões e dados em um único ponto de acesso.

## Objetivo do produto

Oferecer um serviço backend que centralize previsões agrícolas e dados de produtores para apoiar o planejamento da safra, a logística e a gestão técnica.

## Usuários

* Agricultores
* Técnicos agrícolas
* Administradores

## Funcionalidades

* Cadastro de usuários
* Login seguro com JWT
* CRUD de produtores
* Consulta pública de produtores

## Tecnologias

* Flask
* SQLAlchemy
* Flask-JWT-Extended
* SQLite
* Pytest
