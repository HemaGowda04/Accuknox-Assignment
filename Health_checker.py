import requests
import logging

logging.basicConfig(filename="app_health.log", level=logging.INFO,
                    format="%(asctime)s:%(levelname)s:%(message)s")

URL = "https://httpbin.org/status/404"

def check_application_health():
    try:
        response = requests.get(URL, timeout=5)

        if response.status_code == 200:
            logging.info("Application is UP")
        else:
            logging.warning(f"Application is DOWN, status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Application check failed: {e}")

if __name__ == "__main__":
    check_application_health()
