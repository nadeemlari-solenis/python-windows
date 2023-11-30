import requests as r 
import time 
from tqdm import tqdm
count = int(input("Enter the number of times to run the test: "))
print("\nusing blob storage only")
start = time.perf_counter()
for i in tqdm(range(count)):
    response = r.get('https://ssotesttemplate.blob.core.windows.net/pages/AzureBlue/selfAsserted.html') 
    response = r.get('https://ssotesttemplate.blob.core.windows.net/pages/AzureBlue/unified.html')
    response = r.get('https://ssotesttemplate.blob.core.windows.net/pages/src/backgrounds/solenis_background.jfif') 
    response = r.get('https://ssotesttemplate.blob.core.windows.net/pages/src/css/solenis_styles.css')
    response = r.get('https://ssotesttemplate.blob.core.windows.net/pages/src/fonts/din_medium-webfont.woff')
    response = r.get('https://ssotesttemplate.blob.core.windows.net/pages/src/fonts/din_medium-webfont.woff2')
    
end = time.perf_counter()
elapsed_time = end - start
print(f"Average Time: {elapsed_time*1000/count} ms")


print("\nusing Azure CDN ")
start = time.perf_counter()
for i in tqdm(range(count)):
    response = r.get('https://soleniscdn.azureedge.net/pages/AzureBlue/selfAsserted.html') 
    response = r.get('https://soleniscdn.azureedge.net/pages/AzureBlue/unified.html')
    response = r.get('https://soleniscdn.azureedge.net/pages/src/backgrounds/solenis_background.jfif') 
    response = r.get('https://soleniscdn.azureedge.net/pages/src/css/solenis_styles.css')
    response = r.get('https://soleniscdn.azureedge.net/pages/src/fonts/din_medium-webfont.woff')
    response = r.get('https://soleniscdn.azureedge.net/pages/src/fonts/din_medium-webfont.woff2')
    
end = time.perf_counter()
elapsed_time = end - start
print(f"Average Time: {elapsed_time*1000/count} ms")
