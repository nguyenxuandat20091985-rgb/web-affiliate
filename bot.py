import os
import requests
from dotenv import load_dotenv

load_dotenv('.env')
ACCESS_KEY = os.getenv('ACCESSTRADE_API_KEY')

def tao_link_affiliate(shopee_url):
    api_url = "https://api.accesstrade.vn/v1/custom_links"
    headers = {
        "Authorization": f"Token {ACCESS_KEY}",
        "Content-Type": "application/json"
    }
    payload = {"url": shopee_url}
    try:
        response = requests.post(api_url, json=payload, headers=headers)
        if response.status_code == 200:
            return response.json().get('data', {}).get('short_link', shopee_url)
        return shopee_url
    except Exception:
        return shopee_url

if __name__ == "__main__":
    print("--- CHUYỂN ĐỔI LINK ACCESSTRADE ---")
    link_goc = input("Dán link sản phẩm Shopee vào đây: ")
    link_moi = tao_link_affiliate(link_goc)
    print("Link Affiliate của anh đây:")
    print(link_moi)
