# 4-Agents-Engineering-Team - CrewAI

## Description / Description

**FR :**  
4-Agents-Engineering-Team est une équipe d’agents IA spécialisée dans le développement logiciel collaboratif. Chaque agent a un rôle clair : lead technique, développeur backend, développeur frontend et ingénieur QA. Ensemble, ils conçoivent, codent, testent et démontrent un projet Python complet, en suivant des exigences précises. Le système facilite la division du travail, l’automatisation et la qualité du code, pour accélérer le développement tout en restant la rigoureux.  
Ce projet utilise CrewAI.
Le modèle est entièrement paramétrable : chaque agent peut utiliser un modèle de langage différent, adapté à sa tâche spécifique, ce qui permet une meilleur flexibilité et une optimisation des performances.

**EN :**  
4-Agents-Engineering-Team is an AI-driven software engineering team where each agent has a defined role: engineering lead, backend developer, frontend developer, and QA engineer. They collaboratively design, implement, test, and demo a complete Python project based on clear requirements. This setup enables task division, automation, and ensures high code quality to speed up development with precision.  
This project uses Crew AI.
The system is fully configurable: each agent can use a different language model tailored to its specific task, allowing better flexibility and performance optimization.

## Fonctionnalités / Features

- **FR :**  
  - Gestion complète du cycle de développement logiciel en équipe d’agents  
  - Conception détaillée du module backend par le lead technique  
  - Implémentation du code backend selon la conception validée  
  - Création d’une interface frontend simple pour démonstration (Gradio)  
  - Écriture et exécution de tests unitaires automatisés  
  - Processus structuré et séquentiel avec gestion des tâches  
  - Paramétrage indépendant des modèles pour chaque agent  

- **EN :**  
  - Full software development lifecycle managed by a team of AI agents  
  - Detailed backend module design by the engineering lead  
  - Backend code implementation following the approved design  
  - Simple frontend demo interface built with Gradio  
  - Automated unit testing and validation  
  - Structured sequential workflow with task management  
  - Independent model configuration for each agent  

## Demo
You can watch a quick demo of the multi-agent engineering team in action here:
https://drive.google.com/file/d/17ePDdkq0TVcTeYgG-axHndiNdVlBoeM5/view

This video showcases how the agents collaborate seamlessly to design, code, test, and build a frontend for the trading simulation platform. It highlights the power of modular AI agents working together under CrewAI orchestration.


## Prerequisites

- Configure your `.env` file with the required API keys for the language models. Use the `.env.example` in the project as a reference.  
- Install the Python dependency manager `uv` and run `uv sync` to install all project dependencies.  
- Install and start **Docker Desktop**, as agents execute the code they generate inside Docker containers for safe, isolated execution environments.  
- This project uses **CrewAI** to orchestrate the multi-agent workflow.

## Run the Project

- Ensure Docker Desktop is running.  
- Start the agents team with the command:   crewai run

All generated files (backend module, frontend UI, tests) will be saved in the output directory.

To launch the Gradio frontend demo:

cd .\output\
uv run app.py
