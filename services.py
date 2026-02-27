import requests
import xml.etree.ElementTree as ET

HTTP_OK = 200
url_tcmb = "https://www.tcmb.gov.tr/kurlar/today.xml"

def convert_money():
    from_currency = str(input("Çevirmek istediğiniz dövizi girin: ")).upper()
    to_currency = str(input("Çevireceğiniz döviz türünü girin: ")).upper()
    amount = float(input("Para miktarını girin: "))
    response = requests.get(f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}")
    print(f"{amount} {from_currency} = {response.json()['rates'][to_currency]} {to_currency}")

def currency_info():
    currency_code = input("Hangi dövizin alış/satış fiyatını görmek istiyorsunuz?: ").upper()
    response = requests.get(url_tcmb)
    if response.status_code == HTTP_OK:
        root = ET.fromstring(response.content)
        currency = root.find(f".//Currency[@Kod='{currency_code}']")
        
        if currency is not None:
            name = currency.find("CurrencyName").text  
            forex_buying = currency.find("ForexBuying").text  
            forex_selling = currency.find("ForexSelling").text  

            print(f"{name} ({currency_code})  Alış: {forex_buying}  Satış: {forex_selling}")
        else:
            print("Hata: Belirtilen para birimi bulunamadı!")

    else:
        print("Hata:", response.status_code)


def buying_selling_info():
    response = requests.get(url_tcmb)

    if response.status_code == HTTP_OK:
        root = ET.fromstring(response.content)        
        print("Döviz Kurları (Alış - Satış):\n")       
        for currency in root.findall(".//Currency"):
            code = currency.get("Kod") 
            name = currency.find("CurrencyName").text 
            forex_buying = currency.find("ForexBuying").text  
            forex_selling = currency.find("ForexSelling").text  
            print(f"{name:<30} ({code})  {'Alış:':>10} {forex_buying:<10}  Satış: {forex_selling}")
    else:
        print("Hata:", response.status_code)