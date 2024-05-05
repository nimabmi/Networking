

import subprocess

def get_connected_lan_windows():
    result = subprocess.run(["netsh", "interface", "show", "interface"], capture_output=True, text=True)
    output = result.stdout
    lines = output.split('\n')
    for line in lines:
        if "Ethernet" in line and "Connected" in line:
            parts = line.split()
            if len(parts) == 4:
                return parts[3]
            
def get_connected_ssid_windows():
    result = subprocess.run(["netsh", "wlan", "show", "interfaces"], capture_output=True, text=True)
    output = result.stdout
    lines = output.split('\n')
    for line in lines:
        if "SSID" in line:
            ssid = line.split(":")[1].strip()
            return ssid



ssid_lan = get_connected_lan_windows()
ssid_wifi = get_connected_ssid_windows()


if ssid_lan:
    print("Connected LAN SSID:", ssid_lan , "as Network")
elif ssid_wifi:
    print("Connected WIFI SSID:", ssid_wifi)
else:
    print("No LAN connection detected.")