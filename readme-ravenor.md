# Travenor

Aplikasi travel berbasis Flutter & Supabase. Explore destinasi, atur jadwal perjalanan, dan chat dengan sesama traveler secara real-time.

## Fitur

### 1. Autentikasi
- Daftar akun baru (nama, email, password)
- Login dengan email & password
- Lupa password — reset via email (Supabase Auth)
- Verifikasi OTP
- Sesi otomatis (tetap login setelah tutup aplikasi)
- Role admin untuk manage destinasi

### 2. Jelajahi Destinasi (Home & Explore)
- **Home** — Menampilkan banner slider, kategori (Gunung, Pulau, Danau, DLL), destinasi populer, dan rekomendasi dalam bentuk card vertikal
- **Explore** — Grid semua destinasi dengan gambar, rating, dan lokasi
- Setiap card bisa diklik untuk lihat detail destinasi
- Filter berdasarkan kategori di home screen

### 3. Detail Destinasi
- Gambar besar dengan overlay tombol back
- Nama, rating, lokasi, dan deskripsi lengkap
- Galeri gambar (swipe horizontal)
- Tombol "Add to Schedule" — langsung navigasi ke tab jadwal dengan destinasi terisi
- **Admin:** Tombol edit dan delete destinasi
- **Komentar:** Lihat, tambah, edit, dan hapus komentar dari pengguna lain

### 4. Pencarian
- Cari destinasi berdasarkan nama
- Tampilan daftar hasil pencarian dengan gambar dan rating
- Setiap hasil bisa diklik ke detail

### 5. Jadwal Perjalanan
- Tambah jadwal baru dengan destinasi (pilih dari daftar), tanggal mulai & selesai, catatan, dan status (Planning / Upcoming / Completed)
- Edit atau hapus jadwal yang sudah ada
- Tab filter: All | Planning | Upcoming | Completed
- **Admin:** Bisa edit/hapus jadwal mana pun
- **Previous Trips** di profil — menampilkan semua jadwal dengan status Completed

### 6. Chat Real-time
- Percakapan 1-on-1 antar pengguna
- Kirim dan terima pesan real-time via Supabase Realtime
- Daftar percakapan di tab Messages
- Unread count badge di bottom navigation
- Buat percakapan baru dari daftar pengguna
- Tandai pesan sudah dibaca

### 7. Profil
- Tampilkan foto profil, nama, email
- Edit profil (nama, bio, upload avatar)
- Ganti password
- **Previous Trips** — lihat riwayat perjalanan selesai
- Notifikasi (dalam aplikasi, statis)
- Pengaturan (tema, bahasa)
- Bantuan & dukungan
- Logout

### 8. Pengaturan
- **Mode Gelap** — Toggle tema terang/gelap
- **Bahasa** — Pilih Inggris atau Indonesia
- Seluruh UI menyesuaikan dengan pilihan bahasa

### 9. Admin
- Tambah destinasi baru (nama, lokasi, deskripsi, kategori, gambar, koordinat)
- Edit destinasi yang sudah ada
- Hapus destinasi
- Edit/hapus jadwal pengguna lain
- Tombol FAB "+" di home untuk admin

## Teknologi

| Lapisan | Teknologi |
|---------|-----------|
| Framework | Flutter (Dart) |
| State Management | Provider |
| Backend | Supabase (Auth, Database, Storage, Realtime) |
| Gambar | CachedNetworkImage, FilePicker |
| Notifikasi | Lokal (dalam aplikasi) |

## Cara Mulai

### Prasyarat

- Flutter SDK >=3.0.0
- Proyek Supabase (atau pakai yang sudah ada)

### Setup

```bash
# Clone & masuk folder
cd travenor

# Install dependencies
flutter pub get

# Buat file .env
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_ANON_KEY=your-anon-key

# Jalankan di web
flutter run -d chrome

# Jalankan di Android (USB debugging)
flutter run
```

### Migrasi Database

SQL migration ada di `supabase/migrations/`. Jalankan berurutan lewat SQL Editor Supabase:

1. `00001_create_destinations.sql`
2. `00002_create_storage.sql`
3. `00003_create_comments.sql`
4. `00004_add_user_profile_image.sql`
5. `00005_create_schedules.sql`
6. `00006_add_notes_to_schedules.sql`
7. `00007_create_chat.sql`
8. `00008_add_unread.sql`
9. `00009_add_admin_role.sql`

### Fungsi RPC

Fitur chat membutuhkan fungsi PostgreSQL ini (didefinisikan di migrasi 00007–00008):

- `get_conversations()` — Daftar semua percakapan pengguna yang login
- `get_or_create_conversation(other_user_id UUID)` — Cari atau buat percakapan 1-on-1
- `get_unread_count()` — Total pesan belum dibaca
- `get_unread_count_for_conversation(conv_id UUID)` — Pesan belum dibaca per percakapan
- `mark_conversation_read(conv_id UUID)` — Tandai percakapan sudah dibaca

### Trigger Database

- `on_auth_user_created` / `on_auth_user_updated` — Sinkronisasi `auth.users` → `profiles`

## Struktur Folder

```
lib/
├── components/         # Widget UI yang bisa dipakai ulang (banner slider)
├── config/             # Konstanta, tema, warna, gaya teks, bahasa
├── data/
│   ├── models/         # Model data (banner saja)
│   └── services/       # Layanan API (Supabase + eksternal)
├── models/             # Model data utama (destinasi, komentar, jadwal, chat, notifikasi)
├── providers/          # State management (ChangeNotifier + Provider)
├── screens/            # Layar aplikasi
│   ├── add_travel/     # Tambah/edit destinasi (admin)
│   ├── auth/           # Login, daftar, lupa password, OTP
│   ├── details/        # Detail destinasi + komentar + peta
│   ├── explore/        # Grid semua destinasi
│   ├── home/           # Beranda (slider, kategori, rekomendasi)
│   ├── messages/       # Chat real-time (daftar percakapan + room)
│   ├── onboarding/     # Halaman selamat datang
│   ├── profile/        # Profil, edit profil, pengaturan, previous trips
│   ├── schedule/       # Jadwal perjalanan
│   ├── search/         # Pencarian destinasi
│   ├── splash/         # Layar splash
│   └── main_wrapper/   # Bottom navigation wrapper
├── utils/              # Data dummy (tidak dipakai)
└── main.dart           # Titik masuk aplikasi
```

## Dependencies Utama

- `supabase_flutter` — Auth, database, storage, realtime
- `provider` — State management
- `cached_network_image` — Cache & loading gambar dari URL
- `file_picker` — Pilih gambar dari gallery/file manager (web support)
- `carousel_slider` — Carousel banner di home
- `flutter_dotenv` — Variabel lingkungan (.env)
- `google_fonts` — Tipografi custom
- `url_launcher` — Buka peta eksternal
