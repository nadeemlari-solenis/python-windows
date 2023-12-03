import win32serviceutil
import time
import subprocess

def start_service(service_name):
    try:
        # Start the service
        win32serviceutil.StartService(service_name)
        print(f"Service {service_name} started successfully.")

        # Optional: Wait for a moment to let the service start
        time.sleep(5)
        vpn_client_path = r"C:\Program Files (x86)\Cato Networks\Cato Client\CatoClient.exe"
        subprocess.Popen(vpn_client_path)
        time.sleep(2)
    except Exception as e:
        print(f"Error: {e}")
        
def stop_service(service_name):
    try:
        # Start the service
        win32serviceutil.StopService(service_name)
        print(f"Service {service_name} stopped successfully.")
        # Optional: Wait for a moment to let the service start
        time.sleep(5)
        subprocess.Popen("taskkill /F /IM CatoClient.exe", shell=True)
        time.sleep(2)
    except Exception as e:
        print(f"Error: {e}")

# Replace 'YourServiceName' with the name of the service you want to start
service_name = "CatoNetworksVPNService"
input = input("Press 1=Start or 2=Stop: ")
if input=="1":    
    start_service(service_name)
if input=="2":
    stop_service(service_name)

print("closing in 1 seconds")
time.sleep(1)