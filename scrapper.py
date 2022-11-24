#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests



def main():
	url = "https://inet.detik.com/consumer/d-6061534/beda-nasib-penjualan-iphone-dan-hp-android-di-q1-2022"
	r = requests.get(url).text
	soup = BeautifulSoup(r,'lxml')
	teks = soup.find('div',class_="itp_bodycontent detail__body-text")
	hasil = teks.text.split('\n')
	hasil_scraping_satu = hasil[1]
	hasil_scraping_dua = hasil[34][11:-71]

	with open("hasilscraping.txt","w") as f:
		f.write("Daftar Hasil Scraping")
		f.write("\n"*2)
		f.write("1. ")
		f.write(hasil_scraping_satu)
		f.write("\n"*2)
		f.write("2. ")
		f.write(hasil_scraping_dua + "\n")
		f.close()

if __name__ == "__main__":
	main()