print("Info Dokter RumahSakit")
print("------------------")

def doctor_intro(dictionary): 
    print("\n Data Doctor \n")
    for key,val in dictionary.items(): 
        print(f" {key} : {val}")
        
doctors = []

while True: 
    input_nama = input("Siapa nama doctornya? : ")
    input_umur = int(input("Berapa umur doctornya? : "))
    input_spes = input("Apa spesialisasinya? : ")

    doctor = {
        "Nama" : input_nama,
        "Umur" : input_umur,
        "Spesialisasi" : input_spes
    }
    doctors.append(doctor)

    if input("Apakah Anda ingin mengisi info tentang dokter? (y/n) : ") == "n":
        break

for x in doctors: #apply function dokter_intro() ke tiap2 elemen di list doctors[]
    doctor_intro(x)
