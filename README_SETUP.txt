PANDUAN SETUP WORKFLOW CI - KRITERIA 3 (BASIC)
==============================================

LANGKAH 1: BUAT REPOSITORY GITHUB
----------------------------------
1. Buka GitHub: https://github.com
2. Klik tombol "New repository"
3. Nama repository: Workflow-CI-Rivan-Aprilian (sesuaikan nama Anda)
4. Set visibility: PUBLIC (wajib!)
5. Jangan centang "Add a README file"
6. Klik "Create repository"


LANGKAH 2: UPLOAD FOLDER INI KE GITHUB
---------------------------------------
1. Buka terminal di folder Workflow-CI ini
2. Jalankan commands berikut:

git init
git add .
git commit -m "Initial commit - MLflow CI setup"
git branch -M main
git remote add origin https://github.com/USERNAME/Workflow-CI-Rivan-Aprilian.git
git push -u origin main

(Ganti USERNAME dengan username GitHub Anda)


LANGKAH 3: VERIFIKASI WORKFLOW BERJALAN
----------------------------------------
1. Buka repository di GitHub
2. Klik tab "Actions"
3. Anda akan lihat workflow "MLflow CI - Train Model" sedang running
4. Tunggu sampai selesai (hijau = berhasil)
5. Klik workflow tersebut untuk lihat detail logs


LANGKAH 4: AMBIL SCREENSHOT
----------------------------
Screenshot yang dibutuhkan:
1. Screenshot halaman Actions yang menunjukkan workflow berhasil (centang hijau)
2. Screenshot detail logs workflow


LANGKAH 5: BUAT FILE WORKFLOW-CI.TXT
-------------------------------------
Buat file bernama "Workflow-CI.txt" di root folder submission:
Isi file:
https://github.com/USERNAME/Workflow-CI-Rivan-Aprilian

(URL repository GitHub Anda)


CATATAN PENTING:
- Repository HARUS public
- Workflow harus berhasil minimal 1 kali
- Jangan lupa ganti USERNAME dengan username GitHub Anda
- Pastikan file MLproject, conda.yaml, dan modelling.py sudah ada di folder MLProject


TROUBLESHOOTING:
----------------
Jika workflow gagal:
1. Cek logs di GitHub Actions
2. Pastikan conda.yaml dependency benar
3. Pastikan iris_preprocessing.csv ada di folder MLProject
4. Re-run workflow dari tab Actions -> pilih workflow -> Re-run all jobs
