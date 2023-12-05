from pywifi import PyWiFi, const, Profile
import time
from prettytable import PrettyTable

def wifi_scan():
    wifi = PyWiFi()
    iface = wifi.interfaces()[0]
    iface.scan()
    time.sleep(5)
    result = iface.scan_results()
    return result

def wifi_connect(wifi_name, wifi_password):
    wifi = PyWiFi()
    iface = wifi.interfaces()[0]
    profile = Profile()
    profile.ssid = wifi_name
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP
    profile.key = wifi_password
    iface.remove_all_network_profiles()
    tmp_profile = iface.add_network_profile(profile)
    iface.connect(tmp_profile)
    time.sleep(5)
    if iface.status() == const.IFACE_CONNECTED:
        print("Connected to " + wifi_name)
        return True
    else:
        print("Failed to connect to " + wifi_name)
        return False

def display_networks(networks):
    table = PrettyTable()
    table.field_names = ["SSID", "BSSID", "Signal", "Frequency"]

    for network in networks:
        table.add_row([network.ssid, network.bssid, network.signal, network.freq])

    print(table)
    
available_networks = wifi_scan()
display_networks(available_networks)
wifi_connect("Airtel_Zerotouch_5G", "air@70089")