from fastapi import FastAPI
import requests

app = FastAPI()

def get_exchange_rates():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    data = response.json()

    usd_to_kzt = data["rates"]["KZT"]
    usd_to_rub = data["rates"]["RUB"]
    kzt_to_rub = usd_to_rub / usd_to_kzt

    return {
        "USD_TO_KZT": usd_to_kzt,
        "USD_TO_RUB": usd_to_rub,
        "KZT_TO_RUB": kzt_to_rub
    }
@app.get("/exchange-rates")
def read_exchange_rates():
    rates = get_exchange_rates()
    return rates

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
