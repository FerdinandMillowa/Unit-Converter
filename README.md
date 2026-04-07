# Unit Converter CLI

A versatile Command Line Interface tool designed to convert measurements between different units of length, weight, and temperature. This is Project 4 of my **Backend Development Roadmap**.

## 🧠 Key Logic: The "Base Unit" Strategy
To keep the code clean and avoid hundreds of conversion combinations, this project uses a **Base Unit** approach. 

1. **Length:** All units are normalized to **Meters (m)** before being converted to the target unit.
2. **Weight:** All units are normalized to **Grams (g)** before being converted to the target unit.
3. **Temperature:** Uses specific mathematical formulas for Celsius and Fahrenheit.

### 📐 Formulas Used
The temperature conversions are calculated as follows:

* **Celsius to Fahrenheit:** $$F = (C \times \frac{9}{5}) + 32$$

* **Fahrenheit to Celsius:** $$C = (F - 32) \times \frac{5}{9}$$

Roadmap.sh url: https://roadmap.sh/projects/unit-converter

## 🚀 Usage
Run the script using positional arguments in your terminal:

```bash
python converter.py <value> <from_unit> <to_unit>

