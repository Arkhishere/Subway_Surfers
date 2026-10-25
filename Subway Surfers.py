class KarakterSurfer:
    def __init__(self, nama):
        # TODO 1: Inisialisasi properties
        self.nama = nama
        self.skor = 0
        self.koin = 0
        self.is_running = True

    def berlari(self):
        # TODO 2: Mulai berlari
        self.is_running = True
        self.skor += 10
        print(f"{self.nama} lagi lari kabur dari inspektur! Skor jadi {self.skor}")

    def ambil_koin(self, jumlah):
        # TODO 3: Tambahkan koin
        self.koin += jumlah
        print(f"{self.nama} dapet {jumlah} koin. Total koin sekarang ada {self.koin}")

    def tabrak_rintangan(self):
        # TODO 4: Tabrak rintangan & Game Over
        self.is_running = False
        print(f"Aduh! {self.nama} nabrak rintangan, ketangkep deh... Game Over!")

    def info_player(self):
        # TODO 5: Cetak status terkini
        if self.is_running == True:
            status = "Lagi lari"
        else:
            status = "Ketangkep"
        
        print("Status Pemain:")
        print(f"Nama   : {self.nama}")
        print(f"Skor   : {self.skor}")
        print(f"Koin   : {self.koin}")
        print(f"Status : {status}")
        print()


player1 = KarakterSurfer("Jake")
player1.info_player()
player1.berlari()
player1.ambil_koin(15)
player1.tabrak_rintangan()
player1.info_player()