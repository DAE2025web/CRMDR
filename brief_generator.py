#!/usr/bin/env python3
"""Generador simple de briefs de marketing para bufetes de abogados."""

def prompt(text):
    return input(f"{text}: ").strip()

print("Bienvenido al generador de Brief de Marketing para Bufetes de Abogados")

nombre = prompt("Nombre del bufete")
mision = prompt("Misión o eslogan")
colores = prompt("Colores corporativos deseados")
tipografia = prompt("Tipografías preferidas")
objetivos = prompt("Objetivos de marketing digital")
audiencia = prompt("Público objetivo")
objetivo_web = prompt("Objetivo principal del sitio web")

brief = f"""\n==== BRIEF DE MARKETING ====\n"""
brief += f"Bufete: {nombre}\n"
brief += f"Eslogan: {mision}\n"
brief += "Identidad Visual:\n"
brief += f"  Colores: {colores}\n"
brief += f"  Tipografía: {tipografia}\n"
brief += "Marketing Digital:\n"
brief += f"  Objetivos: {objetivos}\n"
brief += f"  Audiencia: {audiencia}\n"
brief += "Sitio Web:\n"
brief += f"  Objetivo: {objetivo_web}\n"
brief += "==========================\n"

filename = f"brief_{nombre.replace(' ', '_')}.txt"
with open(filename, "w", encoding="utf-8") as f:
    f.write(brief)

print(f"Brief generado en {filename}")
