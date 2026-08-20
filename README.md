# Hotel Booking Cancellation Prediction

Project ini memprediksi apakah reservasi hotel akan dibatalkan menggunakan machine learning. Hasil model digunakan pada aplikasi Streamlit untuk memberikan prediksi secara langsung.

## Tujuan

Model mengidentifikasi risiko pembatalan berdasarkan lead time, harga kamar, jumlah tamu, lama menginap, permintaan khusus, dan status tamu berulang.

## Dataset dan Target

Dataset berada di `HotelData.xlsx`. Target `booking_status` dipetakan menjadi:

- `Canceled` menjadi `0`
- `Not_Canceled` menjadi `1`

Fitur tambahan yang dibuat:

- `total_guests`: jumlah orang dewasa dan anak-anak.
- `total_nights`: jumlah malam akhir pekan dan malam hari biasa.
- `is_weekend_heavy`: bernilai `1` jika malam akhir pekan lebih banyak.

## Alur Analisis

Seluruh analisis dilakukan di [notebook.ipynb](notebook.ipynb):

1. Membaca dataset dan memeriksa tipe data, ukuran data, statistik deskriptif, serta distribusi target.
2. Melakukan exploratory data analysis dengan Seaborn dan Matplotlib.
3. Membandingkan pembatalan berdasarkan lead time, harga kamar, jumlah tamu, paket makanan, dan bulan kedatangan.
4. Membuat fitur turunan dan membagi data menjadi training dan testing dengan stratifikasi target.
5. Melatih Random Forest, Gradient Boosting, dan XGBoost menggunakan `RandomizedSearchCV`.
6. Membandingkan akurasi pada data testing.
7. Menyimpan model Gradient Boosting terbaik ke `gb_booking_model.pkl`.

Fitur yang dipakai model:

```text
lead_time
avg_price_per_room
no_of_special_requests
total_guests
total_nights
repeated_guest
```

## Hasil Model

Hasil evaluasi yang tersimpan di notebook:

| Model | Accuracy |
| --- | ---: |
| Random Forest | 0.8081 |
| Gradient Boosting | **0.8309** |
| XGBoost | 0.8119 |

Gradient Boosting dipilih karena menghasilkan akurasi testing tertinggi, sekitar **83,09%**.

## Aplikasi Streamlit

Aplikasi berada di [app.py](app.py). Aplikasi menerima lead time, harga rata-rata kamar, jumlah permintaan khusus, jumlah tamu, total malam menginap, dan status tamu berulang. Hasilnya berupa prediksi `Canceled` atau `Not Canceled` beserta probabilitasnya.

## Struktur Project

```text
.
├── app.py                  # Aplikasi prediksi Streamlit
├── notebook.ipynb          # EDA, feature engineering, training, dan evaluasi
├── HotelData.xlsx          # Dataset
├── gb_booking_model.pkl    # Model Gradient Boosting yang sudah dilatih
├── data.txt                # File data tambahan, saat ini kosong
└── README.md               # Dokumentasi project
```

## Catatan Teknis

`gb_booking_model.pkl` dibuat menggunakan scikit-learn versi `1.7.2`, sedangkan environment saat ini menggunakan versi `1.9.0`. Karena ada perubahan modul internal scikit-learn, [app.py](app.py) menyediakan compatibility alias sebelum membaca file model.

Untuk deployment jangka panjang, model sebaiknya dilatih ulang dan disimpan menggunakan versi scikit-learn yang sama dengan environment aplikasi. Keenam fitur harus diberikan dalam urutan yang sama seperti saat training.
