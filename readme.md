# 📞 VERIFY SPANISH PHONE NUMBERS / VERIFICAR NÚMEROS TELEFÓNICOS ESPAÑOLES

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Pandas](https://img.shields.io/badge/Library-pandas-yellow)
![Excel](https://img.shields.io/badge/Output-.xlsx-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

# [English Version]

A lightweight Python project to identify the **operator** and **province** of Spanish phone numbers — both **mobile** and **landline** — using the official prefix database (`bd-num.zip`) and an Excel file with your phone list.

---

## 🚀 FEATURES

✅ VerifyMobileNumbers.py

- Analyzes mobile phone numbers.
- Detects the correct operator (Movistar, Vodafone, Orange, etc.).
- Automatically cleans and normalizes phone formats.
- Exports results to Excel.

✅ VerifyLandlineNumbers.py

- Analyzes landline (geographic) phone numbers.
- Detects operator and province.
- Uses prefix matching for accurate results.
- Exports results to Excel.

---

## 🧠 HOW IT WORKS

1. Loads prefix data (`moviles.txt` or `geograficos.txt`) from `bd-num.zip`.
2. Reads an Excel file (`numbers.xlsx`) with a column named `numbers`.
3. Cleans phone numbers by removing spaces, dashes, and country codes (+34 / 0034).
4. Matches prefixes and assigns the correct operator or province.
5. Exports a new Excel file with the results.

---

## 📂 PROJECT STRUCTURE

```
VerifyNumbers/
│
├── VerifyMobileNumbers.py # Analyze mobile numbers
├── VerifyLandlineNumbers.py # Analyze landline numbers
├── bd-num.zip # Official prefix database
├── numbers.xlsx # Example input file
└── README.txt # Project documentation
```

---

## 🧩 REQUIREMENTS

Python 3.8+

Install dependencies:

> pip install pandas openpyxl

---

## ⚙️ USAGE

```
🔹 For Mobile Numbers:
Edit the file paths inside the script:
zip_path = r"C:\Users\YourName\Desktop\bd-num.zip"
excel_path = r"C:\Users\YourName\Desktop\numbers.xlsx"
output_path = r"C:\Users\YourName\Desktop\my_mobile_numbers_with_operator.xlsx"
```

Then run:

> python VerifyMobileNumbers.py

🔹 For Landline Numbers:

> python VerifyLandlineNumbers.py

---

## 🧾 EXAMPLE OUTPUT

## numbers | num_norm | operator | province

+34 612345678 | 612345678 | Movistar | —
981123456 | 981123456 | Vodafone | A Coruña

---

## 📘 NOTES

- Files `moviles.txt` and `geograficos.txt` must be inside `bd-num.zip`.
- You can replace `numbers.xlsx` with your own Excel file.
- The Excel column must be named `numbers`.
- The script automatically normalizes phone formats.

---

## 🧑‍💻 AUTHOR

Joao De Abreu
GitHub: https://github.com/deabreu33

---

## 🏷️ LICENSE

This project is licensed under the MIT License — see the LICENSE file for details.

# [Versión en Español]

Un proyecto ligero en Python para identificar el **operador** y la **provincia** de números telefónicos españoles — tanto **móviles** como **fijos** — usando la base de datos oficial de prefijos (`bd-num.zip`) y un archivo Excel con tu lista de números.

---

## 🚀 CARACTERÍSTICAS

✅ VerifyMobileNumbers.py

- Analiza números móviles.
- Detecta el operador correspondiente (Movistar, Vodafone, Orange, etc.).
- Limpia y normaliza los números automáticamente.
- Exporta los resultados a Excel.

✅ VerifyLandlineNumbers.py

- Analiza números fijos (geográficos).
- Detecta operador y provincia.
- Usa coincidencia de prefijos para mayor precisión.
- Exporta los resultados a Excel.

---

## 🧠 CÓMO FUNCIONA

1. Carga los archivos `moviles.txt` o `geograficos.txt` desde `bd-num.zip`.
2. Lee un archivo Excel (`numbers.xlsx`) con una columna llamada `numbers`.
3. Limpia los números (elimina espacios, guiones y el prefijo +34 o 0034).
4. Busca coincidencias de prefijos y asigna operador o provincia.
5. Genera un nuevo archivo Excel con los resultados.

---

## 📂 ESTRUCTURA DEL PROYECTO

```
VerifyNumbers/
│
├── VerifyMobileNumbers.py # Analiza números móviles
├── VerifyLandlineNumbers.py # Analiza números fijos
├── bd-num.zip # Base de datos de prefijos
├── numbers.xlsx # Archivo de ejemplo con números
└── README.txt # Documentación del proyecto
```

---

## 🧩 REQUISITOS

Python 3.8+

Instalar dependencias:

> pip install pandas openpyxl

---

## ⚙️ USO

```
🔹 Para Números Móviles:
Edita las rutas dentro del script:
zip_path = r"C:\Users\TuNombre\Desktop\bd-num.zip"
excel_path = r"C:\Users\TuNombre\Desktop\numbers.xlsx"
output_path = r"C:\Users\TuNombre\Desktop\mis_numeros_moviles_con_operador.xlsx"
```

Luego ejecuta:

> python VerifyMobileNumbers.py

🔹 Para Números Fijos:

> python VerifyLandlineNumbers.py

---

## 🧾 EJEMPLO DE RESULTADO

## numbers | num_norm | operator | province

+34 612345678 | 612345678 | Movistar | —
981123456 | 981123456 | Vodafone | A Coruña

---

## 📘 NOTAS

- Los archivos `moviles.txt` y `geograficos.txt` deben estar dentro de `bd-num.zip`.
- Puedes reemplazar `numbers.xlsx` con tu propio archivo Excel.
- La columna en el Excel debe llamarse `numbers`.
- El script normaliza automáticamente los formatos de teléfono.

---

## 🧑‍💻 AUTOR

Joao De Abreu
GitHub: https://github.com/deabreu33

---

## 🏷️ LICENCIA

Este proyecto está bajo licencia MIT — consulta el archivo LICENSE para más información.
