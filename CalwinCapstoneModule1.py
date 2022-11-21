listBuku = [
    {
        'id': 1,
        'nama buku': 'Of Mice and Men',
        'pengarang' : 'John Steinbeck',
        'stok': 5,
        'harga sewa': 10000
    },
    {
        'id': 2,
        'nama buku': 'A Walk to Remember',
        'pengarang' : 'Nicholas Spark',
        'stok': 7,
        'harga sewa': 7000
    },
    {
        'id': 3,
        'nama buku': 'God of War Ragnarok',
        'pengarang' : 'Richard Gaubert',
        'stok': 9,
        'harga sewa': 9000
    }
]

cart = []


while True :
    pilihanMenu = input('''
       Hallo and Selamat Datang ke Midgard Library. Apa yang bisa kita bantu?

        List Menu :
        1. Menampilkan Daftar Buku
        2. Menambah Buku
        3. Mengubah Data
        4. Menghapus Buku
        5. Exit Program

        Masukkan angka Menu yang ingin dijalankan : ''')

    p = int(pilihanMenu)
    if(p == 1) :
        
        print('Daftar Buku\n')
        print('Index\t| id\t|  Nama Buku  \t\t| Pengarang\t\t| Stok\t| Harga Sewa')
        for i in range(len(listBuku)) :
            print('{}\t| {}\t| {} \t| {} \t| {}\t| {}'.format(i,listBuku[i]['id'],listBuku[i]['nama buku'],listBuku[i]['pengarang'],listBuku[i]['stok'],listBuku[i]['harga sewa']))  
        
        while(True) :
            id = int(input("Masukan id buku : "))

            if(id <= 3) :
                print('Stok buku tersedia')
            else :
                print('Buku tidak tersedia')
        
            checker = input('Apakah anda yakin mau exit dari program ini? (ya/tidak) = ')
            if(checker == 'ya') :
                break
        
    elif(p == 2) :

        while(True) :
            checker = input('Apakah anda ingin menambah daftar buku? (ya/tidak) = ')
            if(checker == 'tidak') :
                break
            else:
                (checker == 'ya\n')

            id = int(input('Masukkan no id baru buku : '))
            if(id <= 3) :
                print('Data sudah ada')
                continue
            else :
                namaBuku = str(input('Masukkan Nama Buku : '))
                namaPengarang = str(input('Masukkan Nama Pengarang : '))
                stokBuku = int(input('Masukkan Stok Buku : '))
                hargaSewa = int(input('Masukkan Harga Sewa : '))
                listBuku.append({
                'id' : id,
                'nama buku': namaBuku,
                'pengarang': namaPengarang,
                'stok': stokBuku,
                'harga sewa': hargaSewa
                })
            print('Daftar Buku\n')
            print('Index\t| id\t|  Nama Buku  \t\t| Pengarang\t\t| Stok\t| Harga Sewa')
            for i in range(len(listBuku)) :
                print('{}\t| {}\t| {} \t| {} \t| {}\t| {}'.format(i,listBuku[i]['id'],listBuku[i]['nama buku'],listBuku[i]['pengarang'],listBuku[i]['stok'],listBuku[i]['harga sewa']))  
        
            
            print('\n\n\nData telah tersimpan') 
            continue    
        
    elif(p == 3) :

        while(True) :
            id = int(input("Nomor index buku : "))
            if(id >= 5):
                print('Data yang anda cari tidak ada')
                continue

            listBuku[1]["stok"] = 20 # contoh di update data stok di index 1
            print("daftar baru stok buku =\n", listBuku)

            checker = input('Apakah anda ingin mengubah lagi? (ya/tidak) = ')
            if(checker == 'tidak') :
                break
            else:
                (checker == 'ya\n')

                        
    elif(p == 4) :
            
        while(True) :
            indexBuku = int(input('Masukkan index buku yang ingin dihapus : '))
            del listBuku[indexBuku]
            print("Index buku berhasil terhapus =\n", listBuku)

            checker = input('Apakah anda ingin melanjutkan lagi? (ya/tidak) = ')
            if(checker == 'tidak') :
                break
            else:
                (checker == 'ya\n')
                continue

    elif(p == 5) :
        checker = input('Apakah anda yakin mau exit dari program ini? (ya/tidak) = ')
        if(checker == 'ya') :
            break # exit program 
        else:
            (checker == 'tidak\n')
            print("\nPilihan yang anda masukan Salah")
            # jika jawab 'tidak' dan muncul text print, selanjut nya akan balik ke menu utama
