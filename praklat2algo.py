def pangkat(bilangan, p):
    if p == 0:
        return 1
    if p < 0:
        return 1 / (bilangan * pangkat(bilangan, abs(p) - 1))
    return bilangan * pangkat(bilangan, p - 1)

def pangkat_ulang():
    bilangan_input = input("Masukkan bilangan: ")
    if bilangan_input == "":  
        print("selesai yaa")
        return
    
    pangkat_input = input("Masukkan pangkat: ")
    if pangkat_input == "":
        print("Pangkat tidak boleh kosong.")
        return pangkat_ulang() 

    try:
        bilangan = float(bilangan_input)
        pangkatnya = int(pangkat_input)
    except ValueError:
        print("Input tidak valid. Silakan masukkan angka!")
        return pangkat_ulang()  

    hasil = pangkat(bilangan, pangkatnya)
    print(f"{bilangan} dipangkatkan {pangkatnya} adalah: {hasil}")

    return pangkat_ulang()

pangkat_ulang()
