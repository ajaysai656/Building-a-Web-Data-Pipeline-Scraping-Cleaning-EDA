import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
}


def scrape_brand(url_template, output_file):
    
    Product, Price, Availability = [], [], []
    Ratings, Reviews = [], []
    Camera, Processor, Storage = [], [], []
    Warranty, Battery = [], []

    for page in range(1, 42):
        url = url_template.format(page=page)
        response = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(response.text, "html.parser")

        for j in soup.find_all("div", class_="RG5Slk"):
            Product.append(j.get_text(strip=True))

        for j in soup.find_all("div", class_="MKiFS6"):
            Ratings.append(j.get_text(strip=True))

        for j in soup.find_all("div", class_="hZ3P6w DeU9vF"):
            Price.append(j.get_text(strip=True))

        for j in soup.find_all("div", class_="PvbNMB"):
            Reviews.append(j.get_text(strip=True))

        for j in soup.find_all("div", class_="bgFu62"):
            Availability.append(j.get_text(strip=True))

        for j in soup.find_all("li", class_="DTBslk"):
            text = j.get_text(strip=True)

            if "Processor" in text:
                Processor.append(text)
            elif "ROM" in text:
                Storage.append(text)
            elif "Warranty" in text:
                Warranty.append(text)
            elif "Battery" in text:
                Battery.append(text)
            elif "Front Camera" in text:
                Camera.append(text)

    # Equalize lengths
    max_len = len(Product)

    lists = [Price, Availability, Ratings, Reviews, Camera, Processor, Storage, Warranty, Battery]

    for lst in lists:
        while len(lst) < max_len:
            lst.append(np.nan)

    df = pd.DataFrame({
        "Product": Product,
        "Price": Price,
        "Availability": Availability,
        "Camera": Camera,
        "Processor": Processor,
        "Storage": Storage,
        "Ratings": Ratings,
        "Reviews": Reviews,
        "Warranty": Warranty,
        "Battery": Battery
    })

    df.to_csv(output_file, index=False, encoding="utf-8")
    print(f"{output_file} saved successfully!")


# ---- BRAND CALLS ----

scrape_brand(
    "https://www.flipkart.com/search?q=phone&sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3DApple&page={page}",
    "data/apple.csv"
)

scrape_brand(
    "https://www.flipkart.com/mobiles/smartphones~type/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3DGoogle&p%5B%5D=facets.brand%255B%255D%3DSamsung&page={page}",
    "data/samsung_google.csv"
)

scrape_brand(
    "https://www.flipkart.com/mobiles/smartphones~type/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3Dvivo&p%5B%5D=facets.brand%255B%255D%3DOPPO&page={page}",
    "data/oppo_vivo.csv"
)

scrape_brand(
    "https://www.flipkart.com/mobiles/smartphones~type/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3DHuawei&p%5B%5D=facets.brand%255B%255D%3DOnePlus&p%5B%5D=facets.brand%255B%255D%3DNothing&p%5B%5D=facets.brand%255B%255D%3DHonor&p%5B%5D=facets.brand%255B%255D%3DCMF%2Bby%2BNothing&p%5B%5D=facets.brand%255B%255D%3DIQOO&p%5B%5D=facets.brand%255B%255D%3DPOCO&p%5B%5D=facets.brand%255B%255D%3DLenovo&page={page}",
    "data/others.csv"
)

df = pd.concat([
    pd.read_csv("data/apple.csv"),
    pd.read_csv("data/samsung_google.csv"),
    pd.read_csv("data/oppo_vivo.csv"),
    pd.read_csv("data/others.csv")
], ignore_index=True)

df.to_csv("data/merged_smartphone_data.csv", index=False)
