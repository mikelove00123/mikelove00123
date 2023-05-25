import requests
import socket
import sys

def check_internet_connective():

    try:
        requests.get('http:www.google.com',timeout=5)
        return True
    except requests.ConnectionError as e:
        print(f"Loss of connectivity: {e}")
        print("Possitive fixes:")
        print("- check if your internet serice provider is ecperiencing any outages.")
        print("- Check if your router is properly configured and connected")
        return False
    
    except socket.timeout as e:
        print(f"Loss of connectivity: {e}")
        print("Possible fixes:")
        print("- Check your internet connection speed.")
        print("- Check if the website's server is experiencing any issues.")
        return False

    except requests.ConnectTimeout as e:
        print(f"Loss of connectivity: {e}")
        print("Possible fixes:")
        print("- Check your internet connection speed.")
        print("- Check if the website's server is experiencing any issues.")
        print("- Check if your computer's or network's firewall or antivirus is blocking the connction.")
        return False    
    
    except requests.ReadTimeout as e:
        print(f"Loss of connectivity: {e}")
        print("Possible fixes:")
        print("- Check your internet connection speed.")
        print("- Ckeck if the website.s server is experiencing any issues.")
        print("- Ckeck if your computer's or network firewall or antivirus is blocking the connection.")
        return False

if check_internet_connectivity():
    print("Internet is connected.")
    sys.exit(0)
else: 
    print("Internet is not connected.")
    sys.exit(1)