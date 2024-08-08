import requests

def fetch_data():
	url = "https://api.publicapis.org/entries"  # Example public API
	response = requests.get(url)
	if response.status_code == 200:
		data = response.json()
		print(data)
	else:
		print(f"Failed to fetch data: {response.status_code}")

if __name__ == "__main__":
	fetch_data()