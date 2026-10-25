class KarakterSurfer:
    def __init__(self, nama):
        self.nama = nama
        self.skor = 0
        self.koin = 0
        self.is_running = True

    def berlari(self):
        self.is_running = True
        self.skor += 10
        print(f"{self.nama} sedang berlari kencang menghindari inspektur! Skor bertambah menjadi {self.skor}.")

    def ambil_koin(self, jumlah):
        self.koin += jumlah
        print(f"{self.nama} mengambil {jumlah} koin. Total koin sekarang: {self.koin}.")

    def tabrak_rintangan(self):
        self.is_running = False
        print(f"Brakk! {self.nama} menabrak rintangan. Tertangkap oleh inspektur! (Game Over)")

    def info_player(self):
        status_lari = "Sedang Berlari" if self.is_running else "Berhenti (Tertangkap)"
        print("--- STATUS PEMAIN ---")
        print(f"Nama Karakter : {self.nama}")
        print(f"Skor Saat Ini : {self.skor}")
        print(f"Jumlah Koin   : {self.koin}")
        print(f"Status        : {status_lari}")
        print("---------------------")


player1 = KarakterSurfer("Jake")
player1.info_player()
player1.berlari()
player1.ambil_koin(15)
player1.tabrak_rintangan()
player1.info_player()