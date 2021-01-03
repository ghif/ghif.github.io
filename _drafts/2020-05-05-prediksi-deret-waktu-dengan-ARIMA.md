---
layout: post
title:  "Prediksi Deret Waktu dengan ARIMA"
date: 2020-05-05 00:00 +0000
categories: math
---

---

# Intro

Salah satu bentuk data yang sering dianalisis pada beragam aplikasi yaitu data dalam bentuk deret waktu (*time series*).
Hasil analisis dari data deret waktu dapat digunakan untuk melakukan prediksi atau perkiraan nilai pada waktu yang akan datang, sering dikenal dengan istilah *time series forecasting*.

Analisis deret waktu (*time series analysis*) merupakan metode untuk menganalisa data dalam bentuk deret waktu untuk menemukan informasi statistik yang bermanfaat dari data tersebut

# Deret Waktu
Sebuah deret waktu merupakan rangkaian sampel berupa nilai pengamatan yang diukur selama kurun waktu tertentu, yang memiliki interval waktu yang uniform.
Beberapa contoh interval waktu yang uniform antara lain dalam hitungan jam, harian, mingguan, bulanan, tahunan, dan sebagainya.
Dalam notasi matematis, deret waktu dapat ditulis dengan $$x(t), t=0,1,2,\ldots$$, dimana $$t$$ merupakan indeks waktu dan $$x(t)$$ merupakan sebuah variabel random.

Jika nilai $$x(t)$$ dalam bentuk skalar, maka deret waktu tersebut dikategorikan sebagai univariat. 
Jika $$x(t)$$ dalam bentuk vektor atau berdimensi banyak, maka dikategorikan sebagai multivariat.

Secara umum deret waktu memiliki 4 buah komponen: *Trend*, *Cyclical*, *Seasonal*, dan *Irregular*.

....

# Analisis dan Prediksi Deret Waktu
Analisis deret waktu merupakan prosedur untuk menemukan model yang tepat yang menggambarkan suatu deret waktu.
Analisis ini bermanfaat untuk memahami karakteristik dari suatu deret waktu dan juga untuk memprediksi nilai di waktu yang akan datang.

Pada prediksi deret waktu, nilai pengamatan pada masa lampau dikoleksi dan dianalisis untuk membangun sebuah model matematis yang menangkap proses pembangkitan data pada deret waktu tertentu.
Nilai masa depan kemudian diprediksi dengan menggunakan model tersebut.

# Konsep Stasioneritas
Ada sebuah kondisi atau asumsi yang diperlukan agar analisis terhadap deret waktu menjadi lebih mudah, yaitu stasioneritas.
Sebuah deret waktu dikatakan stasioner apabila komponen-komponen statistis seperti *rata-rata* dan *varian* tidak bergantung terhadap waktu.

Stasioneritas pada deret waktu dapat dikategorikan menjadi 2 tipe: i) *stasioner kuat* dan ii) *stasioner lemah*.
Sebuah deret waktu $$x(t), t=0,1,2,\ldots$$ dikatakan stasioner kuat apabila distribusi probabilitas gabungan $$\{ x_{t-s}, x_{t-s+1}, \ldots, x_{t}, \ldots, x_{t+s-1}, x_{t+s}\} $$ independen terhadap $$t$$ untuk tiap $$s$$.

Namun demikian pada aplikasi praktis, asumsi stasioner kuat tidak selalu dibutuhkan. 
Terkadang cukup dibutuhkan asumsi yang tidak terlalu ketat sehingga munculah tipe *stasioner lemah*.
Sebuah deret waktu dikatakan stasioner lemah apabila [momen](https://en.wikipedia.org/wiki/Moment_(mathematics)) statistis order ke-$m$ pada deret tersebut independen terhadap waktu.

Sebagai contoh, deret waktu $$x(t), t=0,1,2,\ldots$$ bersifat stasioner order ke-2 apabila rata-rata dan varian independen terhadap waktu, dan nilai kovarian $$\mathrm{Cov}(x_t, x_{t-s}) $$ hanya bergantung pada $$s$$.

# Prediksi Deret Waktu dengan Model Linear

Prediksi pada deret waktu merupakan problem untuk melakukan perkiraan nilai di masa yang akan datang. 
Misalkan diketahui $$N$$ buah nilai suatu deret waktu $$ x(1), \ldots, x(N)$$, kita ingin mengestimasi berapa nilai untuk $$ x^\prime(k) $$ untuk $$ k > N$$.

Salah satu cara 


#### ARMA

**Autoregressive (AR)**

$$ \mathrm{AR}(p) $$:

$$
\begin{equation}
x(t) = c + \sum_{i=1}^{p} x(t-i) + \epsilon(t)
\end{equation}
$$

**Moving Average (MA)**

$$ \mathrm{MA}(q) $$:

$$
\begin{equation}
x(t) = \mu + \sum_{j=1}^{q} \epsilon(t-j) + \epsilon(t)
\end{equation}
$$

$$ \mathrm{ARMA}(p, q) $$:

$$
\begin{equation}
x(t) = c + \epsilon(t) + \sum_{i=1}^{p} \alpha_i x(t-i) + \sum_{j=1}^{q} \beta_j \epsilon(t-j)
\end{equation}
$$

#### ARIMA
Model $$ \mathrm{ARMA}(p, q) $$ berjalan dengan baik apabila data deret waktu bersifat stasioner. 
Namun demikian, di beragam aplikasi dunia nyata data deret waktu bersifat non-stasioner.
ARIMA (Autoregressive Integrated Moving Average) dirancang sebagai bentuk yang lebih umum dari ARMA untuk menangani kondisi non-stasioner.

Model ARIMA membuat data deret waktu yang non-stasioner menjadi stasioner dengan cara 



#### SARIMA






