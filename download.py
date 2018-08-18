import requests
import os
def download_file(url):
	local_filename = url.split('/')[-1]
	r = requests.get(url, stream=True)
	if(r.status_code != 404):
		with open("data/"+local_filename, 'wb') as f:
			for chunk in r.iter_content(chunk_size=1024): 
				if chunk: 
					f.write(chunk)
		return local_filename

def download_data():
	os.mkdir("data")
	names = ["als", "control", "park", "hunt"]
	numbers = [13, 16, 15, 20]

	for j in range(4):
		for i in range(1 , numbers[j]+1):
			num =str(i)
			url = "https://www.physionet.org/physiobank/database/gaitndd/"+names[j]+num+".ts"
			res = download_file(url)

def main():
	download_data()

if __name__ == '__main__':
	main()