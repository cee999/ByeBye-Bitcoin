import requests
from requests.structures import CaseInsensitiveDict
from bs4 import BeautifulSoup
import time
import os

checked = 0

# Function to handle title or print status
def update_status(checked):
    if os.name == 'nt':  # If the system is Windows
        os.system(f"title Bye Bye Bitcoin // Checked Wallets: {checked} // by clout")
    else:  # If it's Linux or macOS, just print the status
        print(f"Bye Bye Bitcoin // Checked Wallets: {checked} // by clout")

while True:
    update_status(checked)
    url = "https://www.bitcoinlist.io/random"
    headers = CaseInsensitiveDict()
    headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36"
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    wallets = soup.find_all("tr")
    for wallet in wallets:
        getwallet = str(wallet.getText()).strip()
        privkey = getwallet.split()[0].strip()
        uncompaddy = getwallet.split()[1].strip()
        compaddy = getwallet.split()[2].strip()
        balance = getwallet.split()[3].strip()
        if "Private Key" in getwallet:
            pass
        else:
            checked += 1
            if float(balance) > 0:
                # Post to Discord webhook if needed (commented out in this version)
                # requests.post("webhook URL", json={"content": f"{balance} BTC found\n\nAddress: {compaddy}\nPrivate Key: {privkey}"}) 
                with open('hits.txt', 'a+') as file:
                    file.write(f"{balance} BTC found in Address: {compaddy} // Private Key: {privkey}\n")

            os.system("clear")  # For Linux, use 'clear' instead of 'cls'
            update_status(checked)  # Update the status (title on Windows, print on Linux)
            print(f"""
            .-.____________________.-.
     ___ _.' .-----.    _____________|======+--------------------+
    /_._/   (      |   /_____________|      |   Bye Bye Bitcoin  |
      /      `  _ ____/                     |      by clout      |
     |_      .\( \\                          |____________________|
    .'  `-._/__`_//
  .'       |'           Private Key: {privkey}
 /        /             Uncompressed Address: {uncompaddy}
/        |              Compressed Address: {compaddy}
|        '              Balance: {balance}
|        |
`-._____.-'""")
        time.sleep(0.5)

/        |              Compressed Address: {compaddy}
|        '              Balance: {balance}
|        |
`-._____.-'""")
        time.sleep(0.5)
    

    
