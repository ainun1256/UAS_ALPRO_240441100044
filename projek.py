menu = {
    "\nmangane dek": "",
    "mie gacoan lv.(1-4)": 10000,
    "mie gacoan lv.(5-8)": 12000,
    "mie hompimpa lv.(1-4)": 10000,
    "mie hompimpa lv.(5-8)": 12000,
    "mie suit": 10000,
    "\nmonggo dimsum e": "",
    "dimsum somay": 9000,
    "udang rambutan": 9000,
    "udang keju": 9000,
    "lumpia udang": 9000,
    "pangsit goreng": 10000,
    "\nngombene dek": "",
    "es gobak sodor": 9000,
    "es petak umpet": 9000,
    "es sluku batok": 6000,
    "es tengklek": 6000
}

pesanan = []

def tampilkan_menu():
    print("\n=========== Menu Gacoan ===========")
    for item, harga in menu.items():
        print(f"{item.capitalize()}: Rp{harga}" if harga else item.capitalize())
    print("="*40)

def tambah_pesanan(item, jumlah):
    item_input = item.lower() 
    if item_input in menu:
        pesanan.append((item_input, jumlah, menu[item_input]))
        print(f"{jumlah} porsi {item_input.capitalize()} ditambahkan ke pesanan")
    else:
        print("maaf menu yang di pesan tidak tersedia. Silakan pilih dari menu berikut:")
        tampilkan_menu()

def hapus_pesanan(nomer):
    if 0 <= nomer < len(pesanan):
        item = pesanan[nomer]
        pesanan.pop(nomer)
        print(f"{item[0].capitalize()} dihapus dari pesanan")
    else:
        print("nomer pesanan tidak valid")

def ubah_pesanan(nomer, jumlah_baru, level_baru=None):
    if 0 <= nomer < len(pesanan):
        item = pesanan[nomer][0]
        item_name = item.lower()

        if "mie gacoan" in item_name:
            if 1 <= level_baru <= 4:
                item = "mie gacoan lv.(1-4)"
            elif 5 <= level_baru <= 8:
                item = "mie gacoan lv.(5-8)"
            else:
                print("Level tidak tersedia!!!")
                return
        elif "mie hompimpa" in item_name:
            if 1 <= level_baru <= 4:
                item = "mie hompimpa lv.(1-4)"
            elif 5 <= level_baru <= 8:
                item = "mie hompimpa lv.(5-8)"
            else:
                print("Level tidak tersedia!!!")
                return

        pesanan[nomer] = (item, jumlah_baru, menu[item])
        print(f"Pesanan {item.capitalize()} diperbarui menjadi {jumlah_baru} porsi")
    else:
        print("nomer pesanan tidak valid")

def tampilkan_pesanan():
    print("\n=========== Daftar Pesanan =============")
    for i in range(len(pesanan)):
        item, jumlah, harga = pesanan[i]
        print(f"{i + 1}. {item.capitalize()} (x{jumlah}): Rp{harga * jumlah}")
    print("="*40)

def hitung_total():
    total = 0
    for item, jumlah, harga in pesanan:
        total += jumlah * harga
    
    diskon = 0
    anggota = input("masukkan ke anggotaan? (lama/baru): ")
    if anggota == 'lama':
        diskon += 15 
    elif anggota == 'baru':
        diskon += 10
    else:
        diskon += 0

    if total > 100000:
        diskon += 5 
    total_diskon = total * (diskon / 100)
    total_setelah_diskon = total - total_diskon

    return total, diskon, total_diskon, total_setelah_diskon

def cetak_struk():
    if len(pesanan) == 0:  
        print("Tidak ada pesanan untuk dicetak")
        return
    total, diskon, total_diskon, total_setelah_diskon = hitung_total()
    print("\n=========== Struk Pembelian ============")
    tampilkan_pesanan()
    print("=" * 40)
    print(f"Total harga: Rp{total}")
    print(f"Diskon yang didapat: {diskon}%")
    print(f"Total Diskon: Rp{total_diskon}")
    print(f"Total Setelah Diskon: Rp{total_setelah_diskon}")
    
    while True:
        pembayaran = int(input("Masukkan jumlah uang pembayaran: Rp"))
        if pembayaran < total_setelah_diskon:
            print("Uang yang diberikan tidak cukup!!!")
            print("Lunasi dulu kalo mau makan :0")
        else:
            kembalian = pembayaran - total_setelah_diskon
            print(f"Kembalian: Rp{kembalian}")
            break    
        
def main():
    while True:
        print("\n======= Menu Utama =======")
        print("1. Tampilkan Menu")
        print("2. Tampilkan Daftar Pesanan")
        print("3. Cetak Struk dan Keluar")
        print("4. Keluar")
        print("="*28)
        pilihan = int(input("Pilih opsi (1-4): "))
        
        if pilihan == 1:
            tampilkan_menu()
            while True:
                tanya = input("Apakah kamu ingin memesan? (y/g): ")
                if tanya == 'y':
                    item = input("Pilih menu yang dipesan: ").lower()

                    if item == "mie gacoan":
                        level = int(input("pilih level (1-8): "))
                        if 1 <= level <= 4:
                            item = "Mie Gacoan lv.(1-4)"
                        elif 5 <= level <= 8:
                            item = "Mie Gacoan lv.(5-8)"
                        else:
                            print("Level tidak tersedia!!!")
                            continue
                    elif item == "mie hompimpa":
                        level = int(input("pilih level (1-8): "))
                        if 1 <= level <= 4:
                            item = "Mie Hompimpa lv.(1-4)"
                        elif 5 <= level <= 8:
                            item = "Mie Hompimpa lv.(5-8)"
                        else:
                            print("Level tidak tersedia!!!")
                            continue
                    else:
                        level = 0
                    
                    jumlah = int(input("Jumlah: "))
                    tambah_pesanan(item, jumlah)
                elif tanya == 'g':
                    print("It's okei bro!!")
                    break
                else:
                    print("kode tidak valid")
                    break
            
        elif pilihan == 2:
            if len(pesanan) == 0:
                print("anda belum memilih pesanan")
                continue
            tampilkan_pesanan()
            print("1. Hapus pesanan")
            print("2. Ubah pesanan")
            print("3. Kembali ke menu utama")
            print("="*36)
            pilih = int(input("pili menu yang diinginkan (1-3): "))
            if pilih == 1:
                nomer = int(input("Pilih nomer pesanan yang ingin dihapus: ")) - 1
                hapus_pesanan(nomer)
            elif pilih == 2:
                nomer = int(input("Pilih nomer pesanan yang ingin diubah: ")) - 1
                jumlah_baru = int(input("Jumlah baru: "))
                if "lv." in pesanan[nomer][0]:
                    level_baru = int(input("Masukkan level baru (1-8): "))
                    ubah_pesanan(nomer, jumlah_baru, level_baru)
                else:
                    ubah_pesanan(nomer, jumlah_baru)
            elif pilih == 3:
                print("Kembali ke menu utama")
        
        elif pilihan == 3:
            cetak_struk()
            print("="*40)
            break
        
        elif pilihan == 4:
            print("oh tidak jadi, oke fine")
            break
        
        else:
            print("Kode tidak valid, Silakan coba lagi")

main()