### Tugas 1

1. Ya, saya memakai <section> untuk membagi porto menjadi beberapa bagian seperti profile, education, dan skills. Elemen tersebut (section) sangat membantu saya untuk memisahkan bagian-bagian di porto saya.
2. Elemen foto di web porto harus diprioritaskan. Dan untuk bagian lain bisa diubah posisi nya dengan mudah karena bisa diletakkan memanjang ke bawah.
3. Untuk website portofolio, static web sudah cukup karena tujuannya untuk menampilkan informasi fix saja. Di proyek selanjutnya, saya mungkin ingin menambahkan contact form agar visitor bisa langsung menghubungi saya dan lebih mudah untuk networking juga.

Dokumentasi:
Saya menggunakan AI Gemini 3.1 Pro untuk membantu saya mengerjakan Tutorial 1 dan Tugas 1. Saya masih cukup bingung dengan kerumitan kode dari Tutorial 1 dan tidak tahu ingin merubah kode tersebut mulai darimana. Saya juga meminta AI untuk desain web saya dengan tema yang sudah diberikan sebelumnya.

Berikut log percakapan saya dengan Gemini: https://share.gemini.google/yUmzUMmltDYl

### Tugas 2

1. Browser kirim request - ditangkap urls.py proyek(tugas nya sebagai router utama yg nge-delegate ke app yang sesuai berdasarkan URL) - urls.py aplikasi(mencocokkan sisa path <int:id> ke view tertentu) - view (memanggil model buat ambil data dari database lalu menyiapkan data nya ke dalam context) - model (menerjemahkan model.objects.get() jadi query SQL, mengambil datanya, lalu mengembalikannya ke object python) - template (menampilkan data dinamis ke HTML) - respon balik ke browser (HTML yg sudah jadi dikirim sebagai HTTP response, browser lalu render menjadi halaman yang terlihat)

2. - template seharusnya cuma ngurusin tampilan, bukan data. klo data ditulis langsung di HTML, template jadi ke campur logic dan presentasi nya.
   - lebih mudah di-update
   - model bisa dipakai ulang di tempat lain (Reusability)

3. - makemigrations: membuat rencana perubahan
   - migrate: yang benar-benar menjalankan perubahan\

   contoh

   class Portofolio(models.Model):
   judul = models.CharField(max_length=100)
   deskripsi = models.TextField()
   tahun = models.IntegerField(default=2026)
   - python manage.py makemigrations > django bikin file sperti "0002_portofolio_tahun.py" yg isinya instruksi untuk tambah kolom tahun ke tabel portofolio_portofolio

   - python manage.py migrate > instruksi tadi baru benar-benar dieksekusi, kolom tahun beneran muncul di tabel database

   Dokumentasi:
   Saya menggunakan AI Gemini 3.1 Pro untuk menuntun saya mengerjakan Tugas 2. Seharusnya saya bisa untuk tidak menggunakan AI, tetapi saya sedikit lupa cara untuk menambah model dan semacamnya. Jika ada kendala dalam mengerjakan Tugas 2 ini, saya juga meminta AI untuk menemukan letak masalahnya.

   Berikut log percakapan saya dengan Gemini: https://share.gemini.google/p0oI41HHQVtN
