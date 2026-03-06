print("=== BASIC CALCULATOR ===")
2
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))
operasi = input("Pilih operasi (+, -, *, /): ")

if operasi == "+":
    print("Hasil:", angka1 + angka2)
elif operasi == "-":
    print("Hasil:", angka1 - angka2)
elif operasi == "*":
    print("Hasil:", angka1 * angka2)
elif operasi == "/":
    print("Hasil:", angka1 / angka2)
else:
    print("Operasi tidak dikenal!")