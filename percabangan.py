# nilai = int(input("Masukkan Nilai :"))
# if nilai >= 80 and nilai <= 100:
#     print("III PINTER")
# elif nilai >= 70 and nilai <= 80:
#     print("TOLONGLAH PINTER SIKIT")
# elif nilai >= 50 and nilai <= 70:
#     print("AGAK LAEN SIKAWAN INI")
# elif nilai >= 30 and nilai <= 50:
#   print("AMPON LA")
# elif nilai >= 0 and nilai <= 20:
#     print("SIAPA KAU SEBENARNYA")
# else:
#    print("NGULANG BOSSS")
# print("=======Latihan=====")


barang = input("masukkan nama barang kulkas/tv/radio: ")

if barang == "kulkas":
    harga = 2000
    diskon = 0.10 * harga
    total = harga - diskon
    print("barang: kulkas")
    print("harga asli:", harga)
    print("diskon : 10%")
    print("potongan diskon:", int(total))
elif barang == "tv":
    harga = 8000
    diskon = 0.05 * harga
    total = harga - diskon
    print("barang: TV")
    print("harga asli:", harga)
    print("diskon : 5%")
    print("potongan diskon:", int(total))
elif barang == "radio":
    harga = 3000
    total = harga
    print("barang: radio")
    print("harga asli:", harga)
    print("diskon : ga ada ")
    print("harga total:", harga)
else:
    print("=====BARANG TIDAK TERSEDIA BOSSS======")
