print("===Konversi Uang: Rupiah menjadi mata uang lain===")

rupiah = float(input("Masukkan jumlah uang (Rp):"))

print("\nPilih mata uang tujuan:")
print("1. USD (Dollar Amerika)")
print("2. EUR (Euro)")
print("3. JPY (Yen Jepang)")
print("4. SGD (Dollar singapore)")

pilihan = input("Masukkan pilihan (1/2/3/4):")

kurs_usd = 16722
kurs_eur = 19320
kurs_jpy = 107
kurs_sgd = 12825

if pilihan == "1":
    hasil = rupiah / kurs_usd
    mata_uang = "USD"
elif pilihan == "2":
    hasil = rupiah / kurs_eur
    mata_uang = "EUR"
elif pilihan == "3":
    hasil = rupiah / kurs_jpy
    mata_uang = "JPY"
elif pilihan == "4":
    hasil = rupiah / kurs_sgd
    mata_uang = "SGD"
else:
    print("Pilihan tidak valid")
    exit()

print(f"\n {rupiah:,.0f} Rupiah = {hasil:,.f} {mata_uang}" )






