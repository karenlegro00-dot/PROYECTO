#!/usr/bin/env python3
"""Organiza documentos originales del ZIP en las cuatro etapas del proyecto."""
from pathlib import Path
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
ARCHIVO = ROOT / "01_PROYECTO_20260916_UC001-20261103T214921Z-1-001.zip"

DESTINOS = {
    "01_UC001_Pla_260916_Antecedentes_v01.docx": "01_Formulacion",
    "PRO_EDU_SUP_FICHA_20261002_v03_LIMPIA.docx": "01_Formulacion",
    "PRO_EDU_SUP_FICHA_20260922_v01.docx": "01_Formulacion/versiones_anteriores",
    "PRO_EDU_SUP_FICHA_20260928_v02.docx": "01_Formulacion/versiones_anteriores",
    "PRO_EDU_SUP_FICHA_20261002_v03.docx": "01_Formulacion/versiones_anteriores",
    "PRO_EDU_SUP_FUENTES_NUEVAS_20261002_v01.docx": "02_Evidencias",
    "LAB_PRO_EDU_SUP_MATRIZ_20261002_v02.xlsx": "03_Seguimiento",
    "LAB_PRO_EDU_SUP_MATRIZ_20260928_v01.xlsx": "03_Seguimiento/versiones_anteriores",
    "Conso_Pro_Per_GitHub_v01.docx": "03_Seguimiento",
}

def main() -> None:
    with ZipFile(ARCHIVO) as zipf:
        archivos = {
            Path(name).name: name
            for name in zipf.namelist()
            if not name.endswith("/")
        }
        faltantes = sorted(set(DESTINOS) - set(archivos))
        if faltantes:
            raise FileNotFoundError("No se encontraron documentos: " + ", ".join(faltantes))
        for nombre, carpeta in DESTINOS.items():
            salida = ROOT / carpeta / nombre
            salida.parent.mkdir(parents=True, exist_ok=True)
            contenido = zipf.read(archivos[nombre])
            if not salida.exists() or salida.read_bytes() != contenido:
                salida.write_bytes(contenido)
            print(f"{carpeta}/{nombre}")
    print(f"Se verificaron {len(DESTINOS)} documentos.")

if __name__ == "__main__":
    main()
