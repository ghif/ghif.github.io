---
layout: post
title:  "Matematika Optimisasi II: Fungsi Konveks Terdiferensiasi"
date: 2019-01-20 00:00 +1300
categories: Math
---


Salah satu jenis fungsi $$ f: \mathcal{X} \rightarrow \mathbb{R}$$ yang menjadi perhatian utama pada optimisasi konveks adalah fungsi terdiferensiasi.
Fungsi terdiferensiasi memungkinkan kita untuk mengeksekusi teknik optimisasi yang cukup efisien dan praktis, yang dikenal sebagai *optimisasi berbasis gradient*. 

Fungsi $$ f(x) $$ dikatakan terdiferensiasi pada titik $$ x $$ apabila memiliki __derivatif orde ke-1 (turunan pertama)__ $$ f^\prime(x)$$.
Notasi lain untuk menyatakan turunan pertama yaitu $$ \frac{d f(x)}{dx}$$.
Untuk ruang input berdimensi banyak $$ \mathcal{X} = \mathbb{R}^d $$, turunan pertama pada titik $$ \mathbf{x} \in \mathbb{R}^d$$ biasa dinyatakan dengan $$ \nabla f(\mathbf{x})$$, yang memiliki dimensi yang sama dengan $$ \mathbf{x} $$.

Bagi yang sudah mempelajari kalkulus tentunya derivatif bukan konsep yang asing.
Namun kita akan secara singkat mengulas konsep limit dan derivatif sebelum membahas kaitannya dengan fungsi konveks.

#### __Limit dan Kontinuitas__
__Limit__ (pada fungsi) merupakan sebuah konsep untuk menyatakan "kedekatan dalam skala yang sangat kecil (*infinitesimal*)" antara nilai fungsi terhadap suatu angka/nilai tertentu.
Notasi umum limit fungsi biasa dinyatakan sebagai berikut:

$$
\begin{equation}
\lim_{x \rightarrow c} f(x) = L \nonumber
\end{equation}
$$

Ekspresi di atas dibaca sebagai berikut: <i>$$ f(x) $$ semakin mendekati $$ L $$ untuk $$ x $$ semakin mendekati $$ c $$</i>.
Definisi berikut ini merupakan pengertian limit fungsi (pada domain 1D) yang lebih saksama.


<div markdown="1" style="border-style: solid; margin: 5px; padding: 5px; text-align: justify; background-color:lightgrey">
**Definisi 1: Limit fungsi ($$\varepsilon$$-$$\delta$$)** \\
Fungsi $$ f: \mathbb{R} \rightarrow \mathbb{R} $$ memiliki limit $$ L $$ untuk $$ x $$ mendekati $$ c $$:

$$
\begin{equation}
\lim_{x \rightarrow c} f(x) = L
\end{equation}
$$

apabila untuk setiap $$ \varepsilon > 0 $$ terdapat $$ \delta > 0 $$ 
sedemikian sehingga $$ 0 < | x - c | < \delta $$ dan $$ 0 < | f(x) - L | < \varepsilon $$.
</div>

Definisi ini berlaku umum termasuk ketika $$ f(c) \neq L$$ atau bahkan ketika $$ f(c) $$ tidak terdefinisi.

Walaupun konsep limit tampak simpel dan cenderung sepele, limit sangat esensial sebagai fondasi dari konsep kontinuitas dan derivatif.

Selanjutnya kita akan menelaah konsep kontinuitas pada fungsi. 
Fungsi kontinu tidak lain merupakan fungsi yang *bersambung*, tidak tiba-tiba terputus atau melompat pada titik tertentu.
Penjelasan lain dari fungsi kontinu adalah fungsi yang apabila menerima perubahan input yang cukup kecil, maka akan menghasilkan perubahan keluaran yang cukup kecil pula.

Secara saksama kita dapat mendefinisikan kontinuitas pada fungsi dengan menggunakan konsep limit.

<div markdown="1" style="border-style: solid; margin: 5px; padding: 5px; text-align: justify; background-color:lightgrey">
**Definisi 2: Fungsi Kontinu** \\
Fungsi $$ f: \mathbb{R} \rightarrow \mathbb{R} $$ dikatakan kontinu pada titik $$ x = c $$ jika $$ f(c) $$ terdefinisi dan limit berikut ini terpenuhi

$$
\begin{equation}
\lim_{x \rightarrow c} f(x) = f(c)
\end{equation}
$$

</div>

Perhatikan bahwa Definisi 2 mensyaratkan $$ f(c) $$ harus ada, sedangkan Definisi 1 tidak.
Dengan kata lain, fungsi kontinu merupakan kondisi yang lebih ketat untuk menyatakan fungsi tersebut memiliki limit -- fungsi kontinu pasti memiliki limit, namun tidak sebaliknya. 

Gambar 1 di bawah ini memberikan ilustrasi perbedaan antara fungsi yang sekadar memiliki limit pada $$x=c$$ dan fungsi kontinu.

<img src="/assets/limit.png" width="750"/>
{: style="font-size: 80%; text-align: center;"}

**Gambar 1**. Ilustrasi limit dan kontinuitas pada fungsi $$ f(x) $$. (a): $$ \lim_{x=c} f(x) $$ terdefinisi namun tidak kontinu, (b): $$ \lim_{x=c} f(x) $$ terdefinisi dan kontinu, (c): Limit tidak terdefinisi pada $$ x = c $$ dan juga tidak kontinu.
{: style="font-size: 80%; text-align: center;"}

Fungsi pada gambar 1c tidak memiliki limit pada $$ x = c $$ karena $$ x $$ dari arah kiri $$c$$ mendekati nilai yang berbeda dari arah kanan.
Fungsi tersebut sebenarnya memenuhi definisi __limit satu-arah__ yang tidak kita bahas lebih lanjut pada kesempatan ini.

#### __Derivatif: Turunan Pertama__
Kita dapat menghitung seberapa cepat fungsi $$ f $$ berubah terhadap input.
Caranya mudah: ambil 2 titik  $$ (x_1, f(x_1)) $$ dan $$ (x, f(x))$$ lalu hitung fraksi 

$$ 
\label{eq:der1}
\begin{equation}
\frac{\Delta f(x)}{\Delta x} = \frac{f(x_1) - f(x)}{x_1 - x} = \frac{f(x + \Delta x) - f(x)}{\Delta x}
\end{equation}
$$

Fraksi tersebut merepresentasikan *kemiringan (slope / gradient)* dari suatu fungsi atau dapat juga dilihat sebagai *kecepatan (velocity)*.

<img src="/assets/derivatif.png" width="500"/>
{: style="font-size: 80%; text-align: center;"}

**Gambar 2**. Fraksi $$ \frac{\Delta f(x)}{\Delta x}$$ menyatakan kemiringan (*gradient*) fungsi $$f$$ pada titik $$x$$. Jika $$f$$ fungsi kontinu dan $$ \Delta x $$ sangat kecil, $$ \Delta x \rightarrow 0 $$, maka fraksi tersebut menjadi derivatif $$ f'(x) = \frac{dy}{dx} $$.
{: style="font-size: 80%; text-align: center;"}

Jika fungsi $$ f:\mathbb{R} \rightarrow \mathbb{R} $$ kontinu, kita dapat meminjam konsep limit untuk menyatakan perubahaan sesaat (*infinitesimal change*) dari nilai fungsi $$ f $$ terhadap input, yaitu $$ \lim_{\Delta x \rightarrow 0} \frac{\Delta f(x)}{\Delta x}$$.
Kuantitas tersebut dikenal sebagai __derivatif__ atau __turunan pertama__ dari fungsi $$ f(x) $$.
Notasi yang sering digunakan untuk menyatakan __derivatif__ yaitu $$ f'(x) $$ dan $$ \frac{dy}{dx} $$ ([Leibniz's notation](https://en.wikipedia.org/wiki/Leibniz%27s_notation)).

Apabila fungsi $$ f (x) $$ memiliki derivatif pada titik $$ x $$, kita sebut $$ f(x) $$ sebagai __fungsi terdiferensiasi__.

<div markdown="1" style="border-style: solid; margin: 5px; padding: 5px; text-align: justify; background-color:lightgrey">
**Defini 3: Fungsi Terdiferensiasi** \\
Fungsi $$ f: \mathbb{R} \rightarrow \mathbb{R}$$ merupakan fungsi terdiferensiasi apabila limit di bawah ini terdefinisi:

$$
\begin{equation}
\label{eq:der2}
\frac{dy}{dx} = f'(x) = \lim_{\Delta x \rightarrow 0} \frac{f(x + \Delta x) - f(x)}{\Delta x}
\end{equation}
$$

Kuantitas $$ \frac{dy}{dx}$$ atau $$ f'(x) $$ dikenal dengan istilah *derivatif dari fungsi f(x)*. 
Sedangkan $$ dy = f'(x) dx $$ dikenal sebagai *diferensial*.

</div>

Ada istilah baru pada definisi di atas yaitu diferensial, yang erat kaitannya dengan *integral*. 
Namun ini diluar cakupan dari tulisan ini. 


#### __Derivatif Partial: Fungsi Dimensi Banyak__
Untuk fungsi berdimensi banyak $$ f: \mathbb{R}^d \rightarrow \mathbb{R}$$, ada sedikit perbedaan pada bentuk derivatif.
Misalkan sebuah vektor $$ \mathbf{x} = (x_1, x_2, \ldots, x_d) $$ merupakan input multi-variabel dari fungsi $$ f $$, derivatif dari $$ f $$ yaitu

$$
\begin{equation}
\label{eq:der3}
\nabla f(\mathbf{x}) = \left( \frac{\partial f}{\partial x_1}, \frac{\partial f}{\partial x_2}, \ldots, \frac{\partial f}{\partial x_d} \right),
\end{equation}
$$

dimana notasi $$ \frac{\partial f}{\partial x_i}$$ merupakan __derivatif partial__ dari $$ f $$.
Derivatif partial tidak lain merupakan derivatif 1 dimensi yang didefinisikan pada persamaan ($$ \ref{eq:der2}$$) namun diaplikasikan pada hanya salah satu/masing-masing variabel dari $$ f $$.

Derivatif $$ \nabla f(\mathbf{x})$$ merupakan kumpulan dari turunan partial untuk tiap variabel input, yang membentuk sebuah vektor. 
Perhatikan bahwa $$ \nabla f(\mathbf{x})$$ memiliki dimensi yang sama dengan vektor input $$ \mathbf{x}$$.

#### __Derivatif: Turunan Kedua__
Kita pun dapat menghitung kembali seberapa cepat perubahan derivatif $$ f'(x) $$, yaitu $$ \frac{f'(x+\Delta x) - f'(x)}{\Delta x}$$.
Jika kita aplikasikan limit pada fraksi tersebut dan limit tersebut terdefinisi, maka kita akan mendapatkan fungsi derivatif yang lain, yaitu __turunan kedua__:

$$
\begin{equation}
\frac{d^2 f(x)}{dx^2} = f^{''}(x) = \lim_{\Delta x \rightarrow 0 } f'(x) = \lim_{\Delta x \rightarrow 0} \frac{f'(x+\Delta x) - f'(x)}{\Delta x}
\end{equation}
$$

Apabila domain fungsi $$ f $$ berdimensi banyak, $$\mathrm{dom}(f) \subseteq \mathbb{R}^d $$, maka turunan kedua menjadi bentuk matriks $$ d \times d $$ yang biasa disebut dengan matriks *Hessian*:

$$
\begin{eqnarray}
\nabla^2 f(\mathbf{x}) = 
\begin{bmatrix}
\frac{\partial^2 f}{\partial x_1^2} & \frac{\partial^2 f}{\partial x_1 x_2} & \cdots & \frac{\partial^2 f}{\partial x_1 x_d} \\
\frac{\partial^2 f}{\partial x_2 x_1} &  \frac{\partial^2 f}{\partial x_2^2} & \cdots & \frac{\partial^2 f}{\partial x_2 x_d} \\
\vdots & \vdots & \ddots & \vdots \\
\frac{\partial^2 f}{\partial x_d x_1} & \cdots & \cdots & \frac{\partial^2 f}{\partial x_d^2}
\end{bmatrix}

\in \mathbb{R}^{d \times d}
\end{eqnarray}
$$



#### __Kondisi Konveksitas Orde I__
Sekarang kita akan menghubungkan fungsi terdiferensiasi dengan konveksitas.
Ingat kembali bahwa fungsi konveks merupakan fungsi yang hanya memiliki 1 lembah, atau nilai fungsi antara 2 titik $$f(x)$$ dan $$f(y)$$ selalu di bawah garis lurus yang menghubungkan antara 2 titik tersebut.
Teorema berikut ini secara eksplisit menyatakan hubungan antara derivatif dan konveksitas.

<div markdown="1" style="border-style: solid; margin: 5px; padding: 5px; text-align: justify; background-color:lightgrey">
**Teorema 1: Fungsi Terdiferensiasi Konveks** \\
Fungsi terdiferensiasi $$ f: \mathcal{X} \rightarrow \mathbb{R} $$ merupakan fungsi konveks *jika dan hanya* jika pertidaksamaan di bawah ini terpenuhi:

$$
\begin{equation}
\label{eq:convex-ord1}
f \left( \mathbf{y}) \geq f(\mathbf{x} \right) + \nabla f(\mathbf{x})^\top (\mathbf{y} - \mathbf{x})
\end{equation}
$$

_Bukti:_

Tanpa mengurangi generalisasi, kita asumsikan $$ \mathcal{X} = \mathbb{R} $$. 
Dengan demikian pertidaksamaan ($$ \ref{eq:convex-ord1} $$) dapat kita sederhanakan menjadi

$$
\begin{equation}
\label{eq:convex-ord2}
f(y) \geq f(x) + f'(x)(y-x)
\end{equation}
$$

Pertama-tama kita buktikan jika fungsi $$ f: \mathbb{R} \rightarrow \mathbb{R} $$ konveks, maka pertidaksamaan di atas terpenuhi.
Dari definisi fungsi konveks kita dapat tulis

$$
\begin{equation}
f((1 - t)x + ty) \leq (1-t) f(x) + t f(y). \nonumber
\end{equation}
$$

Dengan aljabar sederhana dan memanfaatkan Definisi 3 (fungsi terdiferensiasi), maka

$$ 
\begin{eqnarray}
t f(y) &\geq& f((1 - t)x + ty) - (1-t) f(x) \nonumber \\
 f(y) &\geq& f(x) + \frac{ f((1-t)x + ty) - f(x)}{ t}  \nonumber \\
 &\geq& f(x) + \lim_{t \rightarrow 0}  \frac{ f( t(y-x) + x) - f(x) } {t (y - x)} (y - x) \nonumber \\
 &=& f(x) + f'(x)(y - x), \nonumber
\end{eqnarray}
$$

yang merupakan pertidaksamaan ($$\ref{eq:convex-ord2}$$).

Sebaliknya, kita asumsikan pertidaksamaan ($$\ref{eq:convex-ord2}$$) terpenuhi. 
Ambil $$ z = tx + (1-t)y $$ untuk $$ 0 \leq < t \leq 0 $$.
Kita dapat membentuk dua buah pertidaksamaan baru dengan substitusi $$ z $$ pada ($$\ref{eq:convex-ord2}$$)

$$
\begin{eqnarray}
f(y) \geq f(z) + f'(z)(y-z) \nonumber \\
f(x) \geq f(z) + f'(z)(y-x) \nonumber
\end{eqnarray}
$$

Kalikan pertidaksamaan pertama dengan $$(1- t)$$ dan juga pertidaksamaan kedua dengan $$t$$, lalu jumlahkan. Maka kita akan dapatkan

$$
\begin{equation}
tf(x) + (1-t)f(y) \geq f(tx + (1-t)y) \nonumber
\end{equation}
$$

yang merupakan definisi dari fungsi konveks.

Hasil yang sama juga berlaku untuk $$ \mathcal{X} = \mathbb{R}^d $$ dengan memanfaatkan operasi aljabar matriks-vektor.

</div>

Fakta yang kita dapatkan dari Teorema 1 bermanfaat untuk membuktikan secara saksama bahwa *tidak ada solusi optimum lokal pada problem optimisasi konveks*.
Secara intuitif, pernyataan tersebut masuk akal dan mudah untuk dibayangkan dikarenakan fungsi konveks hanya memiliki 1 lembah / cekungan.

Secara formal, pernyataan tersebut dapat dibuktikan dengan Teorema 2 di bawah ini.


<div markdown="1" style="border-style: solid; margin: 5px; padding: 5px; text-align: justify; background-color:lightgrey">
**Teorema 2: Optimum lokal sama dengan optimum global** \\
Jika $$ x_l $$ merupakan solusi optimum lokal, $$ f'(x_l) = 0$$, dari problem optimisasi fungsi konveks terdiferensiasi

$$
\begin{equation}
\min_{x} f(x) \nonumber
\end{equation}
$$

maka $$ x_l $$ sekaligus solusi optimum global. 
Dengan kata lain, tidak ada solusi optimum lokal pada optimisasi konveks. 


_Bukti_:

Misalkan $$ x^* $$ merupakan solusi optimum global, $$f(x^*) < f(x), \forall x \in \mathrm{dom}(f)$$, dan $$f'(x^*) = 0 $$.
Kita akan buktikan dengan kontradiksi. 

Andaikan fungsi konveks $$ f $$ memiliki solusi optimum lokal $$x_l$$, sehingga $$ f(x^*) < f(x_l)$$. 
Karena $$f$$ konveks, maka pertidaksamaan di bawah ini mesti terpenuhi:

$$
\begin{eqnarray}
f(x^*) &>& f(x_l) + f'(x_l)(x^* - x_l) \nonumber \\
f(x^*) &>& f(x_l) \nonumber
\end{eqnarray}
$$

yang kontradiktif dengan pernyataan $$ f(x^*) < f(x_l) $$.

Dengan demikian, fungsi konveks $$ f $$ tidak memiliki solusi optimum lokal.

</div>



#### __Kondisi Konveksitas Orde II__
Kita pun dapat menghubungkan konveksitas dengan turunan kedua.
Teorema di bawah ini menjelaskan hubungan tersebut.

<div markdown="1" style="border-style: solid; margin: 5px; padding: 5px; text-align: justify; background-color:lightgrey">
**Teorema 3: Fungsi Terdiferensiasi Konveks (Orde II)** \\
Fungsi terdiferensiasi orde II $$ f: \mathcal{X} \rightarrow \mathbb{R} $$ merupakan fungsi konveks *jika dan hanya* jika pertidaksamaan di bawah ini terpenuhi:

$$
\begin{equation}
\nabla^2 f(\mathbf{x}) \succeq 0
\end{equation}
$$

yaitu matriks Hessian $$ \nabla^2 f(\mathbf{x}) $$ dalam bentuk positif-definit.

_Bukti:_

Sekali lagi kita sederhanakan kasusnya untuk ruang input berdimensi 1 $$ \mathcal{X} \subseteq \mathbb{R}$$ (tanpa mengurangi generalisasi) dimana bentuk turunan kedua merupakan fungsi skalar $$ f''(x) $$.
Kita akan buktikan kondisi salah satu implikasi: jika $$f^{''} \geq 0$$ maka $$f$$ merupakan fungsi konveks. Kondisi arah sebaliknya silakan dibuktikan sendiri sebagai latihan :)

Dari definisi limit derivatif orde II:

$$
\begin{eqnarray}
\lim_{x \rightarrow 0} f'(x) &=& \lim_{x \rightarrow 0} \frac{f'(x + \Delta x) - f'(x)}{\Delta x} \nonumber \\
&=& \lim_{x \rightarrow 0} \frac{f(x + 2\Delta x) - 2 f(x + \Delta x) + f(x)} {\Delta x^2} \nonumber \\
&=& \lim_{x \rightarrow 0} \frac{f(x + \Delta x) - 2 f(x) + f(x- \Delta x)} {\Delta x^2} \nonumber \\
& \geq & 0
\end{eqnarray}
$$

Karena penyebut $$\Delta x^2 $$ pasti positif, kita jabarkan hanya bagian pembilang dari derivatif di atas:

$$
\begin{eqnarray}
\begin{aligned}
&f(x + \Delta x) - 2 f(x) + f(x- \Delta x) \geq 0 \nonumber \\
&f(x) \leq \frac{1}{2}f(x + \Delta x) + \frac{1}{2}f(x - \Delta x) \nonumber \\
&f( \frac{1}{2} (x + \Delta x) + \frac{1}{2}(x - \Delta x)) \leq \frac{1}{2}f(x + \Delta x) + \frac{1}{2}f(x - \Delta x) \nonumber
\end{aligned}
\end{eqnarray} 
$$

Perhatikan bahwa baris terakhir pada pertidaksamaan di atas merupakan definisi dari konveksitasi fungsi $$f$$.
Dengan demikian terbukti bahwa $$f^{''} \geq > 0 $$ berimplikasi bahwa fungsi $$f$$ merupakan fungsi konveks.
</div>

#### __Caveat__
Sebagai catatan terakhir, baik derivatif orde I atau orde II keduanya dapat digunakan sebagai alat untuk mengidentifikasi konveksitas sebuah fungsi $$ f $$. 
Penggunaan derivatif orde II bahkan tampak lebih simpel, yaitu hanya cukup mengecek $$ f^{''} > 0 $$ atau matriks Hessian $$ \nabla^2 f(\mathbf{x}) \succeq 0 $$, apabila turunan kedua terdefinisi pada fungsi $$ f $$.
Namun demikian, untuk kasus berdimensi banyak, penghitungan matriks Hessian akan memakan waktu dan memori yang cukup besar pada komputer. 


#### __Referensi__

[1] [S. P. Boyd dan L. Vandenberghe. "Convex Optimization", Cambridge University Press, 2009](http://web.stanford.edu/~boyd/cvxbook/)

[2] [G. Strang. "Calculus", Wellesley-Cambridge Press](https://ocw.mit.edu/ans7870/resources/Strang/Edited/Calculus/Calculus.pdf)
