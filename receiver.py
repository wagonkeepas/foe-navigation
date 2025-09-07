import requests
import os
from datetime import datetime
import time

def download_image(ip_address, save_folder):
    url = f"http://{ip_address}/capture"
    
    try:
        print(f"Requesting image from {url}...")
        response = requests.get(url, timeout=30)
        
        if response.status_code == 200:
            # Create folder if it doesn't exist
            os.makedirs(save_folder, exist_ok=True)
            
            # Generate filename with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = os.path.join(save_folder, f"esp32_capture_{timestamp}.jpg")
            
            # Save image
            with open(filename, 'wb') as f:
                f.write(response.content)
            
            print(f"✅ Image saved: {filename} ({len(response.content)} bytes)")
            return True
        else:
            print(f"❌ Error: HTTP {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    # Configuration
    ESP_IP = "172.20.10.2"  # Replace with your ESP32's IP (check Serial Monitor)
    SAVE_FOLDER = "C:/Users/mizza/Desktop/Competition Projects/Codenection2025/ESP32cam/ESP32_Captures"  # Change this to your desired folder
    
    print("ESP32-S3-CAM Image Downloader")
    print("=" * 40)
    
    while True:
        choice = input("\nPress Enter to capture image or 'q' to quit: ")
        if choice.lower() == 'q':
            break
        
        download_image(ESP_IP, SAVE_FOLDER)

if __name__ == "__main__":
    main()