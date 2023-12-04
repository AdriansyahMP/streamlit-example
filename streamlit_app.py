import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/adria/OneDrive/Dokumen/Realestate.csv')
df.head()

# Fungsi untuk membaca data dari file CSV
def baca_data_csv(nama_file):
    with open(nama_file, 'r', newline='') as file_csv:
        pembaca_csv = csv.reader(file_csv)
        # Membaca header
        header = next(pembaca_csv)
        # Membaca baris-baris data
        data = [baris for baris in pembaca_csv]
    return header, data

# Fungsi untuk menulis data ke file CSV
def tulis_data_csv(nama_file, header, data):
    with open(nama_file, 'w', newline='') as file_csv:
        penulis_csv = csv.writer(file_csv)
        # Menulis header
        penulis_csv.writerow(header)
        # Menulis baris-baris data
        penulis_csv.writerows(data)

# Contoh penggunaan
nama_file_input = 'data_input.csv'
nama_file_output = 'data_output.csv'

# Membaca data dari file CSV
header, data = baca_data_csv(nama_file_input)

# Melakukan pemrosesan data (contoh: menambahkan kolom baru)
for baris in data:
    # Misalnya, menambahkan kolom jumlah
    baris.append(int(baris[1]) + int(baris[2]))

# Menulis data yang telah diproses ke file CSV baru
tulis_data_csv(nama_file_output, header, data)
