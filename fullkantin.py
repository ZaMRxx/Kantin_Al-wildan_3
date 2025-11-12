# Dictionary untuk menyimpan menu dan harga
menu = {
    'beng-beng': 2000,
    'Tao Kae Noi Big Sheet Rumput Laut': 5100,
    'Qtela keripik tempe original': 8600,
    'pocky biskuit stik stroberi': 9000,
    'Cha-cha Minis cokelat susu police': 6500
}

print("Selamat datang di Kantin Kejujuran")

# Meminta nama pengguna
nama_pengguna = input("Masukkan nama Anda: ")

# Variabel untuk total biaya dan uang yang dibayarkan
total_biaya = 0
uang_dibayarkan = 0

# Loop untuk memproses pembelian makanan
while True:
    # Menampilkan daftar menu dengan nomor urut
    print("\nMenu:")
    for i, (item, harga) in enumerate(menu.items(), start=1):
        print(f"{i}. {item.capitalize()} Rp. {harga}")

    # Meminta pilihan makanan dengan angka 1-5
    pilihan = input("\nPilih menu dengan menuliskan angka 1-5 (atau ketik 'selesai' untuk mengakhiri): ")

    # Keluar dari loop jika pengguna memilih 'selesai'
    if pilihan.lower() == 'selesai':
        break

    # Memeriksa apakah pilihan valid (angka 1-5)
    if pilihan.isdigit():
        index = int(pilihan) - 1  # mengubah input menjadi index dalam list

        if 0 <= index < len(menu):
            makanan = list(menu.keys())[index]
            harga = menu[makanan]

            # Meminta jumlah makanan yang ingin dibeli
            jumlah = int(input(f"Masukkan jumlah {makanan.capitalize()} yang ingin Anda beli: "))
            total_harga = harga * jumlah
            total_biaya += total_harga
            print(f"Berhasil membeli {jumlah} {makanan.capitalize()} dengan total biaya Rp{total_harga}")
        else:
            print("Pilihan tidak valid, silakan pilih kembali.")
    else:
        print("Input tidak valid, silakan masukkan angka 1-5 atau 'selesai'.")

# Meminta uang yang dibayarkan
while True:
    try:
        uang_dibayarkan = float(input(f"\nTotal biaya keseluruhan adalah Rp{total_biaya}. Masukkan uang yang dibayarkan: "))
        if uang_dibayarkan >= total_biaya:
            break
        else:
            print("Uang yang dibayarkan kurang dari total biaya. Silakan masukkan jumlah uang yang cukup.")
    except ValueError:
        print("Masukkan angka yang valid untuk uang yang dibayarkan.")

# Menghitung uang kembalian
uang_kembalian = uang_dibayarkan - total_biaya

# Mengucapkan terima kasih dan menampilkan total biaya keseluruhan dan uang kembalian
print(f"\nTerima kasih, {nama_pengguna}!")
print(f"Total biaya yang harus Anda bayar adalah Rp{total_biaya:.2f}.")
print(f"Uang yang dibayarkan: Rp{uang_dibayarkan:.2f}.")
print(f"Uang kembalian yang harus Anda terima adalah Rp{uang_kembalian:.2f}.")
