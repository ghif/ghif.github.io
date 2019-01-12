---
layout: post
title:  "Matematika Optimisasi I: Himpunan dan Fungsi Konveks"
date: 2019-01-13 00:00 +1300
categories: Machine Learning, Artificial Intelligence, Mathematical Optimization
---

Jika ada yang bertanya disiplin matematika apakah yang sangat sentral perannya pada bidang pemelajaran mesin dan kecerdasan buatan, saya akan menjawab dua, yaitu __teori probabilitas__ dan __matematika optimisasi__. 

Hampir semua algoritma pemelajaran mesin berbasis matematika optimisasi.
Matematika optimisasi, yang bertujuan untuk mencari solusi optimal dari permasalahan, merupakan basis dari hampir semua algoritma pemelajaran mesin.

Saya akan coba menuliskan seri tulisan mengenai optimisasi konveks secara singkat, dimulai dari teori hingga beberapa algoritma populer untuk menyelesaikan problem optimisasi konveks.


#### __Problem Optimisasi__
Problem optimisasi merupakan problem meminimalkan atau memaksimalkan suatu __fungsi objektif__, biasanya dalam bentuk fungsi riil $$ f:\mathcal{D} \rightarrow \mathbb{R} $$ dengan mencari __variabel optimisasi__ $$ x \in \mathcal{D}$$ yang tepat, dimana $$ \mathcal{D}$$ merupakan ruang input / domain dari $$ f $$ -- seringkali ditulis dengan $$ \mathrm{dom}(f)$$.
Untuk kasus multi-variabel, $$ \mathcal{D} $$ dapat berupa subset dari ruang Euclidean $$ \mathbb{R}^n $$ sehingga
$$ \mathbf{x} = [x_1, x_2, \ldots, x_n]^\top \in \mathbb{R}^n $$ merupakan vektor berdimensi $$n$$.

Notasi formal problem optimisasi multi-variabel (dalam bentuk minimisasi) dapat ditulis sebagai berikut.

$$
\begin{equation}
\label{eq:opt}
P: \min_{\mathbf{x} \in \mathbb{R}^n} f(\mathbf{x})
\end{equation}
$$

Untuk problem maksimisasi kita tinggal mengganti operator $$ \min $$ menjadi $$ \max $$.

Notasi formal di atas merupakan bentuk problem optimisasi yang tanpa batasan (*unconstrained*) dari sudut pandang variabel optimisasi $\mathbf{x}$. 
Dengan kata lain, $$ \mathbf{x} $$ dapat bernilai apa saja selama berada pada domain fungsi objektif, $$ \mathbf{x} \in \mathrm{dom}(f)$$.

Vektor $$ \mathbf{x}^* \in \mathcal{F}$$ disebut sebagai __solusi__ dari problem ($$ \ref{eq:opt} $$) jika memberikan nilai yang paling minimum: $$ f(\mathbf{x}^*) \leq f(\mathbf{x}), \forall \mathbf{x} \in \mathcal{F} $$. 
Himpunan $$ \mathcal{F} $$ biasa disebut sebagai __feasible set__, yaitu, himpunan solusi yang mungkin. 
Pada problem ($$ \ref{eq:opt}$$), __feasible set__ merupakan domain dari fungsi $$ f $$, yaitu $$ \mathcal{F} = \mathrm{dom}(f)$$.


#### __Problem Optimisasi dengan Batasan__
Seringkali problem optimisasi memiliki batasan (*constraints*) bagi $$ x $$ untuk *bergerak* ke arah tertentu. 
Ada dua tipe fungsi batasan:
1. Tipe pertidaksamaan (inequality constraints): $$ g(\mathbf{x}) \leq h $$
2. Tipe persamaan (equality constraints): $$ h(\mathbf{x}) = b \$$

Batasan ini dinyatakan pula dengan fungsi, bisa jadi lebih dari 1 fungsi. 
Misalkan terdapat $$ m $$ buah fungsi batasan pertidaksamaan dan $$ k $$ buah fungsi batasan persamaan, problem optimisasi dapat ditulis menjadi

$$
\begin{eqnarray}
\label{eq:copt}
\min_{\mathbf{x}  \in \mathbb{R}^n} & f(\mathbf{x}) \\
\text{subject to } & g_i(x) \leq h_i, i = 1, \ldots, m,  \nonumber \\
				   & h_j(x) = b_j, j = 1, \ldots, k. \nonumber
\end{eqnarray}
$$

Dengan adanya fungsi-fungsi batasan, __feasible set__ merupakan irisan dari domain fungsi objektif dan fungsi-fungsi batasan:

$$
\begin{eqnarray}
\mathcal{F} = \{ \mathrm{dom}(f) \cap \mathrm{dom}(g_i) \cap \mathrm{dom}(h_j) \}, i=1,\ldots,m, j=1,\ldots,k \nonumber
\end{eqnarray}
$$

*Feasible set* dapat berupa himpunan kosong, $$ \mathcal{F} = \emptyset $$ yang berarti problem optimisasi tersebut tidak memiliki solusi.

#### __Problem Optimisasi Konveks__
Secara geometris, fungsi-fungsi $$f, g_i, h_j $$ memiliki bentuk: untuk domain hingga 3 dimensi kita dapat melakukan visualisasi dengan mudah dengan menggambar $$ (x, f(x)) $$.
Bentuk-bentuk fungsi tersebut dapat berupa bentuk yang sederhana/teratur seperti fungsi konstanta, linear, kuadrat, kubik, dan sebagainya, ataupun yang kompleks/tidak teratur seperti fungsi [indeks saham](https://en.wikipedia.org/wiki/Stock_market_index).

Pada umumnya, semakin kompleks suatu fungsi maka akan semakin sulit pula untuk menyelesaikan problem optimisasi.
Fungsi yang kompleks dicirikan dengan banyaknya [optimum lokal](https://en.wikipedia.org/wiki/Local_optimum) yang dapat membuat pencarian solusi optimal $$ \mathbf{x}^*$$ menjadi sulit.

Pada optimisasi, terdapat sebuah kelas bentuk fungsi yang sudah cukup praktis untuk diselesaikan. 
Bentuk fungsi tersebut yaitu fungsi konveks (atau konkaf apabila dibalik).
Problem optimisasi dengan fungsi objektif dan batasan berbentuk konveks disebut sebagai __problem optimisasi konveks__.

<div markdown="1" style="border-style: solid; margin: 5px; padding: 5px; text-align: justify; background-color:lightgrey">
**Definisi 1: Optimisasi Konveks** \\
Problem optimisasi dengan batasan ($$ \ref{eq:copt} $$) dikatakan sebagai optimisasi konveks apabila:
* Fungsi objektif $$ f $$ merupakan fungsi konveks;
* Fungsi batasan $$ g_i $$ dan $$ h_j $$ juga merupakan fungsi konveks
</div>

Apakah yang dimaksud dengan fungsi konveks? Secara intuitif, bentuk fungsi konveks diilustrasikan pada Gambar 1 di bawah ini.
Dapat dilihat bahwa semua fungsi tersebut hanya memiliki 1 buah *lembah/cekungan*. 

<img src="/assets/konveks1d.jpg" width="500"/>
{: style="font-size: 80%; text-align: center;"}

**Gambar 1**. Ilustrasi ungsi konveks dalam 1D
{: style="font-size: 80%; text-align: center;"}


Problem optimisasi konveks sudah cukup lama dipelajari dan sudah banyak metode / algoritma yang dapat menyelesaikannya secara efisien, dengan teori yang cukup mapan.
Banyak problem pada dunia nyata yang dapat diaproksimasi dengan problem konveks. 

Tantangan utama dan juga seni dari optimisasi konveks lebih kepada sisi mengidentifikasi dan memformulasikannya. 
Ketika Anda berhasil memformulasikan suatu problem sebagai optimisasi konveks, bisa dikatakan Anda hampir 100% menyelesaikan problemnya: algoritma penyelesaian optimisasi konveks hampir mencapai level teknologi *black-box* yang dapat diandalkan. Solusi dari optimisasi konveks $$ \mathbf{x}^* $$ sudah pasti solusi optimal, walaupun belum tentu unik.


Agar dapat menjalankan komputasi optimisasi konveks, kita perlu mendefinisikan fungsi konveks secara formal.
Bagaimana menyatakan sebuah fungsi $$ f: \mathcal{X} \rightarrow \mathbb{R} $$ secara matematis?


#### __Himpunan Konveks__
Sebelum ke definisi formal fungsi konveks, perlu untuk diketahui terlebih dahulu definisi dari himpunan konveks.
Bayangkan sebuah himpunan $$ \mathcal{X} $$ yang berisi titik koordinat $$ \mathbf{x} = (x_1, x_2) \in \mathcal{X} $$.
Ambil dua titik koordinat pada himpunan $$ \mathcal{X} $$, yaitu $$ \mathbf{x} $$ dan $$ \mathbf{y} $$, lalu gambar garis lurus antara kedua buah titik tersebut.

Apabila garis yang digambar tersebut masih berada pada area himpunan $$ \mathcal{X} $$, maka $$ \mathcal{X} $$ merupakan himpunan konveks (lihat Gambar 2 kiri dan tengah).
Dan sebaliknya, apabila garis tersebut keluar dari wilayah $$ \mathcal{X} $$, maka $$ \mathcal{X} $$ tidak konveks (Gambar 2 paling kanan).

<img src="/assets/konveks2d.jpg" width="500"/>
{: style="font-size: 80%; text-align: center;"}
**Gambar 2**. Ilustrasi himpunan konveks dalam 2D. Yang berwarna merah bukan merupakan fungsi konveks.
{: style="font-size: 80%; text-align: center;"}

Pernyataan di atas dapat dinyatakan lebih formal dengan definisi di bawah ini.
Definisi ini berlaku tidak hanya untuk himpunan $$ \mathcal{X} $$ pada ruang 2 dimensi, namun berlaku umum untuk dimensi berapapun. 

<div markdown="1" style="border-style: solid; margin: 5px; padding: 5px; text-align: justify; background-color:lightgrey">
**Definisi 2: Himpunan Konveks**

Sebuah himpunan $$ \mathcal{X} $$ dikatakan konveks apabila untuk setiap anggota himpunan $$ \mathbf{x}, \mathbf{y} \in \mathcal{X} $$ dan $$ 0 \leq t \leq 1$$ kondisi di bawah ini terpenuhi:

$$ 
\begin{equation}
t \mathbf{x} + (1 - t) \mathbf{y} \in \mathcal{X}
\end{equation}
$$

</div>

Ekspresi $$ t \mathbf{x} + (1- t) \mathbf{y} $$ dengan $$ 0 \leq t \leq 1 $$ menyatakan garis lurus antara $$ \mathbf{x} $$ dan $$ \mathbf{y} $$.
Ekspresi tersebut juga dikenal dengan istilah [kombinasi konveks](https://en.wikipedia.org/wiki/Convex_combination).

Berikut ini beberapa contoh dari himpunan konveks:
1. *Norm ball*: $$ \mathcal{X} = \{ \mathbf{x} : \| \mathbf{x} \| \leq r \} $$
2. *Hyperplane*: $$ \mathcal{X} = \{ \mathbf{x} : \mathbf{a}^\top \mathbf{x} = b \} $$
3. *Halfspace*: $$ \mathcal{X} = \{ \mathbf{x} : \mathbf{a}^\top \mathbf{x} < b \} $$
4. *Affine space*: $$ \mathcal{X} = \{ \mathbf{x} : \mathbf{A}^\top \mathbf{x} = \mathbf{b} \} $$
5. *Polyhedron*: $$ \mathcal{X} = \{ \mathbf{x} : \mathbf{A}^\top \mathbf{x} < \mathbf{b} \} $$

Kita akan coba buktikan bahwa *hyperplane* merupakan himpunan konveks dengan menggunakan Definisi 2.

<div markdown="1" style="border-style: solid; margin: 5px; padding: 5px; text-align: justify; background-color:white">
__Contoh 1: *Hyperplane* merupakan himpunan konveks__

Misalkan $$ \mathcal{Q} = \{ \mathbf{q} : \mathbf{a}^\top \mathbf{q} = b \} $$.
Ambil 2 anggota himpunan *Hyperplane* $$ \mathbf{x}, \mathbf{y}$$. 
Dari Definisi 2 kita akan membuktikan $$ \mathbf{a}^\top \left( t \mathbf{x} + (1 - t) \mathbf{y} \right) = b $$.

$$
\begin{eqnarray} 
\mathbf{a}^\top \left( t \mathbf{x} + (1 - t) \mathbf{y} \right) &=& t \mathbf{a}^\top \mathbf{x} + \mathbf{a}^\top \mathbf{y} - t \mathbf{a}^\top \mathbf{y}  \nonumber \\
&=& tb + b - tb \nonumber \\
&=& b \nonumber
\end{eqnarray}
$$

Dikarenakan kombinasi konveks dari setiap 2 anggota dari *hyperplane* memenuhi Definisi 2, maka *hyperplane* merupakan himpunan konveks.
</div>

Pembaca dianjurkan untuk mengecek apakah contoh-contoh lain di atas merupakan himpunan konveks.

Perlu digarisbawahi bahwa penting untuk mengetahui himpunan konveks karena himpunan konveks merupakan basis dari fungsi konveks. 

#### __Fungsi Konveks__

Sebelumnya telah dijelaskan secara intuitif bahwa sebuah fungsi $$ f: \mathcal{X} \rightarrow \mathbb{R} $$ dikatakan konveks apabila hanya memiliki 1 cekungan.
Definisi di bawah ini menyatakan intuisi tersebut dengan bahasa matematika.


<div markdown="1" style="border-style: solid; margin: 5px; padding: 5px; text-align: justify; background-color:lightgrey">
**Definisi 3: Fungsi Konveks**

Sebuah fungsi $$ f: \mathcal{X} \rightarrow \mathbb{R} $$ dikatakan konveks apabila $$ \mathcal{X} = \mathrm{dom}(f)$$ merupakan himpunan konveks dan untuk $$ \mathbf{x}, \mathbf{y} \in \mathrm{dom}(f)$$ pertidaksamaan di bawah ini terpenuhi

$$
\begin{equation} 
\label{eq:convex_fn}
f \left(t \mathbf{x} + (1-t) \mathbf{y} \right) \leq t f(\mathbf{x}) + (1-t) f(\mathbf{y})
\end{equation}
$$

</div>

Apabila $$ \mathcal{X} $$ dalam ruang 1D, ruas kiri dari persamaan (\ref{eq:convex_fn}) menggambarkan *busur panah*, sedangkan ruas kanan menggambarkan *tali busur* / garis lurus antara $$ (x, f(x)) $$ and $$ (y, f(y)) $$ (lihat Gambar 3).
Fungsi konveks harus memenuhi kondisi ini untuk setiap $$ x $$ dan $$ y $$.

<img src="/assets/fungsi_konveks.png" width="500"/>
{: style="font-size: 80%; text-align: center;"}
**Gambar 3**. Ilustrasi himpunan konveks dalam 2D. Yang berwarna merah bukan merupakan fungsi konveks.
{: style="font-size: 80%; text-align: center;"}

Berikut ini beberapa contoh populer dari fungsi konveks:
1. Fungsi *affine*: $$ f(\mathbf{x}) = \mathbf{a}^\top \mathbf{x} + b $$.
2. Fungsi kuadrat (1-variabel): $$ f(x) = ax^2 + bx + c $$, untuk $$ a > 0$$.
3. Fungsi kuadrat (multi-variabel): $$ f(\mathbf{x}) = \frac{1}{2} \mathbf{x}^\top \mathbf{Q} \mathbf{x} + \mathbf{q} \mathbf{x} + c$$, untuk $$ \mathbf{Q} $$ positif-definit.
4. Fungsi $$ \ell_p$$-norm: $$f(\mathbf{x}) = \| \mathbf{x} \|_p = (\sum_i x^p_i)^{\frac{1}{p}} $$ untuk $$ p \geq 1$$.
5. Fungsi *least-squares*: $$ f(\mathbf{x}) = \| \mathbf{b} - \mathbf{A} \mathbf{x} \|^2_2 $$.
6. Fungsi maksimum: $$ f(\mathbf{x}) = \mathrm{max}(x_1, \ldots, x_d)$$.

<div markdown="1" style="border-style: solid; margin: 5px; padding: 5px; text-align: justify; background-color:white">
__Contoh 2: Fungsi kuadrat 1-variabel merupakan fungsi konveks__

Diketahui fungsi kuadrat 1D $$ f(x) = ax^2 + bx + c $$, $$ a > 0 $$.
Untuk mengecek bahwa $$ f $$ konveks, pertama kita asumsikan $$ \mathrm{dom}(f) $$ merupakan himpunan konveks.
Misalkan $$x, y \in \mathrm{dom}(f) $$, selanjutnya dari Definisi 3 kita buktikan

$$ 
\begin{equation}
a\left(tx + (1-t)y \right)^2 + b \left(tx + (1-t)y \right) + c 
\leq t (a x^2 + bx + c) + (1 - t) (a y^2 + by + c) \nonumber
\end{equation}
$$


Pertidaksamaan di atas apabila diserhanakan akan sama dengan

$$ 
\begin{equation}
a\left(tx + (1-t)y \right)^2 \leq t (a x^2) + (1 - t) (a y^2) \nonumber
\end{equation}
$$

Untuk $$ t = 1 $$ atau $$ t = 0 $$, ruas kiri sama dengan ruas kanan (kondisi terpenuhi).
Untuk $$ 0 < t < 1 $$, dengan menggunakan aljabar standard kita ekspansi ruas kiri:

$$
\begin{eqnarray}
a (tx + (1-t)y)^2 = a t^2 x^2 + a (1-t)^2 y^2 + 2 a t (1-t) x y \nonumber
\end{eqnarray}
$$

Salah satu trik yang dapat digunakan adalah mencari kuantitas yang lebih besar dari  $$ 2 at(1-t) $$.
Dengan memanfaatkan faktwa bahwa $$ a ( tx - (1-t) y)^2 \geq 0 $$ (ini hanya terjadi karena $$ a > 0 $$), kita dapatkan:

$$
\begin{eqnarray}
a (tx - (1-t)y) ^ 2 = a t^2 x^2 + a (1-t)^2 y^2 - 2at(1-t)xy \geq 0 \nonumber \\
\label{eq:left_ineq}
\implies 2at(1-t)xy \leq a t^2 x^2 + a (1-t)^2 y^2 
\end{eqnarray}
$$

Dengan demikian kita dapat simpulkan, untuk $$ 0 < t< 1 $$:

$$
\begin{eqnarray}
a(tx + (1-t)y)^2 &\leq& 2 t^2 (ax^2) + 2 (1-t)^2 (ay^2) \nonumber \\
&\leq& t ax^2 + (1-t) y^2  \nonumber
\end{eqnarray}
$$

</div>


Dengan menggunakan fungsi konveks pada optimisasi ($$ \ref{eq:opt}$$), akan muncul sifat / kondisi dari problem optimisasi yang sangat bermanfaat secara praktis, yaitu kita tidak perlu khawatir akan nilai optimum lokal walaupun solusinya tidak unik.
Maksudnya adalah jika ada 2 algoritma berbeda untuk memecahkan problem optimisasi konveks yang juga menghasilkan 2 solusi yang berbeda, $$ \mathbf{x}^*_1 $$ dan $$ \mathbf{x}^*_2 $$, maka dapat dipastikan $$ f(\mathbf{x}^*_1) = f(\mathbf{x}^*_2)$$.


<div markdown="1" style="border-style: solid; margin: 5px; padding: 5px; text-align: justify; background-color:lightgrey">
**Teorema 1:**
Jika $$ f:\mathcal{X} \rightarrow \mathbb{R}$$ merupakan fungsi konveks, maka setiap optimum lokal pasti merupakan optimum global.

Bukti:

*... tunggu tulisan selanjutnya*
</div>


#### __Referensi__

[1] [S. P. Boyd dan L. Vandenberghe. "Convex Optimization", Cambridge University Press, 2009](http://web.stanford.edu/~boyd/cvxbook/)

