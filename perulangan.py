brp_mhs = int(input("jumlah mahasiswa : "))
brp_nilai = 0
for i in range(1, brp_mhs + 1):
    nilai = float(input(f"masukan nilai mahasiswa {i} : "))
    brp_nilai += nilai       
rata_rata = brp_nilai / brp_mhs

print(f"\nnilai rata - rata : {rata_rata}")