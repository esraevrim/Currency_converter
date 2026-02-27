# 💱 Currency Converter

A terminal-based currency converter built with Python that fetches live exchange rate data from two real APIs — the **Turkish Central Bank (TCMB)** and **Frankfurter API**.

## 📋 Features

- **View All Exchange Rates** – Fetches and displays live buying & selling rates for all currencies from the TCMB
- **Currency Conversion** – Converts any amount between two currencies using the Frankfurter API
- **Currency Detail** – Looks up the buying and selling rate for a specific currency code from the TCMB
- **Interactive Menu** – Simple numbered menu loop running entirely in the terminal

## 🗂️ Project Structure

```
Currency_converter/
├── main.py        # Entry point — menu loop and user input handling
└── services.py    # API calls and business logic
```

## 🚀 Getting Started

### Requirements

- Python 3.x
- `requests` library

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/esraevrim/Currency_converter.git
   cd Currency_converter
   ```

2. Install dependencies:
   ```bash
   pip install requests
   ```

3. Run the app:
   ```bash
   python main.py
   ```

## 🖥️ Usage

When you run the app, you'll see the following menu:

```
Yapmak istediğiniz işlemi seçin:
1. Döviz Alış Ve Satış Görüntüleme
2. Döviz Çevirme
3. Döviz Bilgisi Görüntüleme
4. Programdan Çıkış
```

| Option | Description |
|--------|-------------|
| 1 | Lists all currencies with their live buying and selling rates |
| 2 | Converts an amount from one currency to another |
| 3 | Shows buying/selling rate for a specific currency code (e.g. `USD`, `EUR`) |
| 4 | Exits the program |

### Example — Currency Conversion

```
Çevirmek istediğiniz dövizi girin: USD
Çevireceğiniz döviz türünü girin: TRY
Para miktarını girin: 100
100.0 USD = 3245.67 TRY
```

## 🔧 Technologies Used

| Technology | Description |
|------------|-------------|
| Python 3 | Core programming language |
| `requests` | HTTP requests to external APIs |
| `xml.etree.ElementTree` | Parsing XML data from TCMB |
| [TCMB XML Feed](https://www.tcmb.gov.tr/kurlar/today.xml) | Live buying/selling rates from the Turkish Central Bank |
| [Frankfurter API](https://www.frankfurter.app) | Free, open-source currency conversion API |

## 🙋‍♀️ Developer

**Esra Evrim** – [@esraevrim](https://github.com/esraevrim)
