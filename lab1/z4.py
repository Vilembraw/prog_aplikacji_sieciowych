import ipaddress

def check_ip():
    adress = input("Adress IP: ").strip()

    try:

        ipaddress.ip_address(adress)
        print(f"OK: '{adress}'")
    except ValueError:
        print(f"Error: '{adress}'")

if __name__ == "__main__":
    check_ip()