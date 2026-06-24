# KALTIM SMART PLATFORM

Sistem Layanan Publik dan Pelaporan Warga Berbasis Cloud Computing

---

# Informasi Peserta

**Nama Peserta:** Puji Novianti Andini

**Kode Peserta:** PNA-283DDF3E

**Kategori:** Cloud Computing

**LKS Cloud Computing 2026**

---

# Deskripsi Project

KALTIM SMART PLATFORM adalah aplikasi layanan publik digital yang dirancang untuk membantu masyarakat dan pemerintah daerah dalam mengelola layanan publik secara online.

Aplikasi ini memungkinkan warga untuk:

- Registrasi dan login ke sistem
- Mengirim laporan permasalahan di lingkungan sekitar
- Melihat status laporan
- Menerima notifikasi ketika status laporan berubah
- Mengakses layanan publik secara digital

Sedangkan administrator dapat:

- Melihat seluruh laporan warga
- Mengubah status laporan
- Mengelola layanan publik
- Melihat statistik dan dashboard monitoring

Project ini dikembangkan menggunakan FastAPI dan dipersiapkan untuk deployment pada infrastruktur AWS Cloud.

---

# Fitur Utama

## Modul Autentikasi

- Login pengguna
- JWT Authentication
- Profile pengguna
- Role-Based Access Control (Admin dan Citizen)

Endpoint:

```http
POST /login
GET /profile
```

---

## Modul Laporan Warga

Warga dapat membuat laporan terkait kondisi lingkungan atau pelayanan publik.

Endpoint:

```http
POST /reports
GET /reports
PUT /reports/{id}/status
```

Fitur:

- Membuat laporan baru
- Melihat laporan
- Update status laporan
- Pembatasan akses berdasarkan role

---

## Modul Notifikasi

Sistem akan membuat notifikasi otomatis ketika status laporan berubah.

Endpoint:

```http
GET /notifications
```

---

## Modul Dashboard

Dashboard digunakan oleh administrator untuk melihat statistik sistem.

Endpoint:

```http
GET /dashboard/stats
```

Informasi yang ditampilkan:

- Total laporan
- Total laporan selesai
- Total laporan terbuka

---

# Struktur Project

```text
lks-project/
│
├── app/
│   ├── main.py
│   ├── auth.py
│   ├── deps.py
│   ├── db.py
│   └── models.py
│
├── docker/
│   └── Dockerfile
│
├── lks.db
│
├── requirements.txt
├── .env.example
└── README.md
```

---

# Diagram Arsitektur

```text
                    INTERNET
                        │
                        ▼
                ┌──────────────┐
                │   Browser    │
                └──────┬───────┘
                       │ HTTP
                       ▼
                ┌──────────────┐
                │   FastAPI    │
                │ REST API     │
                └──────┬───────┘
                       │
         ┌─────────────┴─────────────┐
         ▼                           ▼

 ┌───────────────┐          ┌────────────────┐
 │ Authentication│          │ Reports System │
 │ JWT Security  │          │ Notifications  │
 └───────┬───────┘          └───────┬────────┘
         │                          │
         └──────────┬───────────────┘
                    ▼

             ┌────────────┐
             │ SQLite DB  │
             │   lks.db   │
             └────────────┘
```

---

# Arsitektur AWS (Target Deployment)

Pada implementasi cloud, aplikasi akan dijalankan menggunakan layanan AWS berikut:

```text
Internet
    │
    ▼
Application Load Balancer
    │
    ▼
Amazon ECS Fargate
    │
 ┌──┴─────────────┐
 ▼                ▼

Amazon RDS     Amazon ElastiCache
(PostgreSQL)      (Redis)

    │
    ▼

Amazon S3
(File Storage)

    │
    ▼

CloudFront CDN
```

Komponen AWS:

- Amazon ECS Fargate
- Amazon ECR
- Amazon RDS PostgreSQL
- Amazon ElastiCache Redis
- Amazon S3
- Amazon CloudFront
- AWS Secrets Manager
- Amazon CloudWatch
- AWS CloudTrail
- Amazon SNS
- Amazon SQS
- Amazon Cognito
- AWS Budget
- Terraform

---

# Teknologi yang Digunakan

## Backend

- Python
- FastAPI
- SQLAlchemy
- JWT Authentication

## Database

- SQLite (Development)
- PostgreSQL (Production AWS)

## Containerization

- Docker
- Docker Compose

## Cloud Platform

- Amazon Web Services (AWS)

## Infrastructure as Code

- Terraform

---

# Environment Variable

File `.env.example`

```env
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///./lks.db
```

---

# Cara Menjalankan Project

## 1. Clone Repository

```bash
git clone <repository-url>
```

Masuk ke folder project:

```bash
cd lks-project
```

---

## 2. Install Dependency

```bash
pip install -r requirements.txt
```

---

## 3. Jalankan FastAPI

```bash
python -m uvicorn app.main:app --reload
```

---

## 4. Buka Swagger Documentation

```text
http://127.0.0.1:8000/docs
```

Swagger digunakan untuk:

- Login
- Menguji API
- Mengirim laporan
- Melihat dashboard
- Menguji notifikasi

---

# Cara Pengujian API

## Login

```json
{
  "email": "admin@mail.com",
  "password": "123"
}
```

---

## Authorize Token

1. Login terlebih dahulu
2. Copy token JWT
3. Klik tombol Authorize pada Swagger
4. Paste token
5. Klik Authorize

---

## Membuat Laporan

Endpoint:

```http
POST /reports
```

Contoh Request:

```json
{
  "title": "Jalan Rusak",
  "description": "Banyak lubang di depan sekolah"
}
```

---

## Melihat Laporan

Endpoint:

```http
GET /reports
```

---

## Mengubah Status Laporan (Admin)

Endpoint:

```http
PUT /reports/{id}/status
```

Contoh:

```json
{
  "status": "resolved"
}
```

---

## Melihat Notifikasi

Endpoint:

```http
GET /notifications
```

---

# Menjalankan Menggunakan Docker

## Build Image

```bash
docker build -f docker/Dockerfile -t lks-api .
```

---

## Menjalankan Container

```bash
docker run -p 8000:8000 lks-api
```

---

## Akses Aplikasi

```text
http://localhost:8000/docs
```

---

# Author

Puji Novianti Andini

PNA-283DDDF3E

LKS Cloud Computing 2026
