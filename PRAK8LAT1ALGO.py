def rekursif(jumlah):
  if jumlah < 1:
    return 0
  elif jumlah == 1:
    angka = int(input("Masukkan angka: "))
    return angka
  else:
    angka = int(input(f"Masukkan angka ke-{jumlah}: "))
    return angka + rekursif(jumlah - 1)

jumlah_angka = int(input("Masukkan Jumlah: "))

hasil = rekursif(jumlah_angka)
print("Hasil penjumlahan:",{hasil})