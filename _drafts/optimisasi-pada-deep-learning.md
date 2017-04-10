---
layout: post
title:  "Optimisasi pada Deep Learning"
date: 2017-03-25 08:13:15 +1300
categories: aiml
---

*Deep learning* bekerja melalui proses optimisasi. 
Dengan kata lain, *artificial neural networks* belajar dari data dengan cara mengoptimalkan fungsi objektif.
Dari pertengahan tahun 80-an hingga sekarang, teknik optimisasi yang digunakan berbasis *first-order gradient* dari fungsi objektif yang disebut sebagai *gradient descent* ([Cauchy, 1847](http://gallica.bnf.fr/ark:/12148/bpt6k2982c.image.f540.pagination.langEN)).
Dipadukan dengan *chain rule*, *gradient descent* pada neural networks dikenal dengan algoritma *back-propagation* ([Rumelhart et al. 1986](http://www.cs.toronto.edu/~fritz/absps/pdp8.pdf)). 
{: style="text-align: justify;"}

Di ranah *mathematical optimization*, gradient descent merupakan metode yang paling sederhana dan telah banyak tersedia metode-metode optimisasi lain yang lebih canggih. 
Mengapa *deep learning* masih mengandalkan gradient descent? 
Alasan utamanya adalah skalabilitas komputasi: gradient descent memiliki kompleksitas linear terhadap pertambahan data dan juga mudah untuk dikomputasi secara paralel (dengan memanfaatkan GPU).
Karakteristik ini memungkinkan sebuah model *neural network* yang cukup besar untuk dilatih dengan jutaan data latih.
Beberapa kisah sukses terkait hal ini antara lain AlexNet ([Krizhevsky et al. 2012](https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf)), Word2Vec ([Mikolov et al. 2013](https://papers.nips.cc/paper/5021-distributed-representations-of-words-and-phrases-and-their-compositionality.pdf)), dan ResNet ([He et al. 2015](https://arxiv.org/pdf/1512.03385.pdf)).
{: style="text-align: justify;"}


Misalnya kita punya sebuah *neural network* $$\displaystyle f_{\theta} : \mathcal{X} \rightarrow \mathcal{Y}$$, dimana $$\theta$$ merupakan parameter yang nantinya akan disetel berdasarkan data yang dipelajari -- pada *neural networks* parameter ini terdiri dari *weights* dan *bias*.
Asumsikan kondisi *supervised learning*, yaitu $$f_\theta$$ belajar dari pasangan data $$(x, y)$$ dan definisikan fungsi *loss* $$\displaystyle \ell: \mathcal{Y} \times \mathcal{Y} \rightarrow \mathbb{R}$$. 
Salah satu bentuk fungsi *loss*, untuk $$\mathcal{Y} \subseteq \mathbb{R}$$, adalah *least-square error* $$L\left(f_\theta(x), y \right) = \left( f_\theta(x) - y\right)^2$$.

Untuk menyederhanakan notasi, tulis $$L(\theta) := L(f_\theta(x), y)$$. 
Tujuan dari optimisasi pada *deep learning* yaitu meminimalkan fungsi *loss*
{: style="text-align: justify;"}

$$
\begin{equation}
\label{eq:dlobj}
	\min_{\theta} L(\theta)
\end{equation}
$$

Kita definisikan *gradient* dari fungsi *loss* terhadap $\theta$ dengan notasi $$\nabla_\theta L(\theta)$$.

 
# Gradient Descent (GD)
Kita definisikan *gradient* dari fungsi *loss* terhadap $\theta$ dengan notasi $$\nabla_\theta L(\theta)$$.
*Gradient descent* melakukan *update* terhadap parameter $$\theta$$ agar objektif (\ref{eq:dlobj}) tercapai 
dengan memanfaatkan $$\nabla_{\theta}L(\theta)$$. 
Tahapan GD diringkas pada __Algoritma 1__. 
{: style="text-align: justify;"}


<div markdown="1" style="border-style: solid; margin: 5px; padding: 5px; text-align: justify;">
**Algoritma 1** (Gradient Descent). \\
$$
\text{1: } \theta_0 = \mathrm{rand()} \\
\text{2: } \textbf{repeat} \\
\text{3: } \quad g_t := \nabla_{\theta_{t-1}} L(\theta_{t-1})  \\
\text{4: } \quad \theta_t := \theta_{t-1} - \alpha g_t \\
\text{5: } \textbf{until}\quad\text{convergence}
$$
</div>


Gambar 1 mengilustrasikan parameter dengan ruang solusi berdimensi dua -- parameter pada *neural networks* umumnya berdimensi banyak.
Parameter $$\theta$$ dapat diilustrasikan sebagai sebuah titik pada ruang solusi.
Secara intuitif, GD memindah-mindahkan titik tersebut berdasarkan arahan dari *gradient*, 
yang menginformasikan **jalur tercuram/tercepat** dari suatu posisi tertentu ke posisi tujuan.
Harapannyai, akumulasi informasi dari *gradient* pada tiap-tiap posisi mampu mengantarkan ke solusi optimal.
{: style="text-align: justify;"}

![GD](http://komarix.org/ac/papers/thesis/thesis_html/img30.png "Gradient Descent")
{: style="font-size: 80%; text-align: center;"}
**Gambar 1**. Gradient Descent (sumber: [http://komarix.org/ac/papers/thesis/thesis_html/img30.png](http://komarix.org/ac/papers/thesis/thesis_html/img30.png]))
{: style="font-size: 80%; text-align: center;"}

Namun demikian, strategi memilih jalur tercuram ini memiliki beberapa kekurangan.
Pertama, terdapat resiko untuk terjebak di solusi yang kurang optimal. 
Kedua, tidak ada garansi untuk terjadi konvergensi ke suatu solusi.
Kedua masalah ini terkait juga dengan pemilihan konstanta $$\alpha > 0$$ (baris ke-4 pada **Algoritma 1**).
Jika $$\alpha$$ terlalu kecil, maka $$\theta$$ berpotensi terperangkap ke *local optima*, 
sedangkan jika terlalu besar maka berpotensi terjadi osilasi/divergensi.

Masalah yang lebih fundamental adalah bahwa mengikuti jalur tercuram belum tentu merupakan cara yang benar atau efisien untuk menuju tujuan solusi, 
terutama untuk lanskap ruang solusi yang kompleks.
Bayangkan seseorang yang turun dari perbukitan dengan berjalan kaki, tetapi tidak tahu jalan menuju daratan dan tidak mempunyai peta. 
Salah satu metode heuristis yang bisa dipakai adalah selalu mengikuti jalur yang turun ke bawah.
Padahal bisa jadi itu akan membawa kita berputar-putar dahulu sebelum mencapai daratan tujuan, atau bahkan bisa terperangkap ke jurang.
Mungkin saja jalur yang benar adalah dengan cara menaiki bukit-bukit kecil terlebih dahulu, lalu kemudian turun.
{: style="text-align: justify;"}


Dapatkah GD diperbaiki sehingga mampu membentuk jalur optimisasi yang lebih efisien? Secara umum terdapat 2 strategi: 
i) menggunakan *momentum* dan ii) mengatur kecepatan *gradient* menjadi adaptif.
{: style="text-align: justify;"}


# GD dengan Classical Momentum (CM)
Momentum ([Polyak, 1964](https://www.researchgate.net/profile/Boris_Polyak2/publication/243648538_Some_methods_of_speeding_up_the_convergence_of_iteration_methods/links/5666fa3808ae34c89a01fda1.pdf)) merupakan sebuah metode untuk mengakselerasi GD dengan memanfaatkan informasi *gradient* dari langkah-langkah sebelumnya.
Akumulasi informasi dari *gradient* berguna untuk mengurangi efek osilisasi sehingga jalur optimisasi menjadi lebih stabil.
Algoritma 2 di bawah ini merupakan modifikasi dari GD dengan penambahan strategi momentum.
{: style="text-align: justify;"}


<div markdown="1" style="border-style: solid; margin: 5px; padding: 5px; text-align: justify;">
**Algoritma 2** (Gradient Descent dengan Classical Momentum (CM)). \\
$$
\text{1: } \theta_0 = \mathrm{rand()} \\
\text{2: } m_0 = 0 \\
\text{3: } \textbf{repeat} \\
\text{4: } \quad g_t := \nabla_{\theta_{t-1}} L(\theta_{t-1})  \\
\text{5: } \quad m_t := g_t + \beta m_{t-1} \\
\text{6: } \quad \theta_t := \theta_{t-1} - \alpha m_t \\
\text{7: } \textbf{until}\quad\text{convergence}
$$
</div>

Kita sebut saja algoritma ini dengan *Classical Momentum* (CM) -- pada bagian berikutnya akan dibahas metode momentum yang lebih terkini.
Jika dibandingkan dengan GD, CM hanya melakukan satu penambahan, yaitu $$ \beta m_{t-1}$$, 
dimana $$ \beta $$ merupakan konstanta yang mengatur seberapa besar kontribusi dari *gradient* sebelumnya. 
$$ \beta = 0.9 $$ merupakan best practice dari CM -- perhatikan bahwa $$ \beta = 0$$ akan membuat CM sama persis dengan GD.
{: style="text-align: justify;"}


Andaikan gradient $$ g_t $$ merupakan sebuah vektor berdimensi banyak.
Secara intuitif, CM akan memberikan bobot yang lebih pada dimensi tertentu yang memiliki nilai yang konsisten untuk tiap langkah.
Sebaliknya, untuk dimensi yang tidak stabil CM akan memberikan bobot yang lebih kecil.
Hal inilah yang menstabilkan jalur optimisasi dari parameter $$ \theta $$ sehingga menimbulkan efek akselerasi.
{: style="text-align: justify;"}


Perbedaan antara GD dan CM dapat dijelaskan dengan analogi sebagai berikut: GD seperti seseorang yang berjalan kaki di perbukitan dan mencoba turun ke daratan, 
sedangkan CM seperti bola yang menggelinding ke bawah.
Bagi yang tertarik mendalami lebih lanjut tentang CM bisa membaca sebuah tulisan brilian di sini: [http://distill.pub/2017/momentum](http://distill.pub/2017/momentum/).
{: style="text-align: justify;"}



# Nesterov Accelerated Gradient (NAG)
<div markdown="1" style="border-style: solid; margin: 5px; padding: 5px; text-align: justify;">
**Algoritma 3.1** (Nesterov's Accelerated Gradient (NAG)). \\
$$
\text{1: } \theta_0 = \mathrm{rand()} \\
\text{2: } m_0 = 0 \\
\text{3: } \textbf{repeat} \\
\text{4: } \quad g_t := \nabla_{\theta_{t-1}} L(\theta_{t-1} - \beta m_{t-1})  \\
\text{5: } \quad m_t := g_t + \beta m_{t-1} \\
\text{6: } \quad \theta_t := \theta_{t-1} - \alpha m_t \\
\text{7: } \textbf{until}\quad\text{convergence}
$$
</div>


<div markdown="1" style="border-style: solid; margin: 5px; padding: 5px; text-align: justify;">
**Algoritma 3.2** (Nesterov's Accelerated Gradient (NAG)). \\
$$
\text{1: } \theta_0 = \mathrm{rand()} \\
\text{2: } m_0 = 0 \\
\text{3: } \textbf{repeat} \\
\text{4: } \quad g_t := \nabla_{\theta_{t-1}} L(\theta_{t-1})  \\
\text{5: } \quad m_t := g_t + \beta m_{t-1} \\
\text{6: } \quad \hat{m}_t := g_t + \beta m_t \\
\text{7: } \quad \theta_t := \theta_{t-1} - \alpha \hat{m}_t \\
\text{8: } \textbf{until}\quad\text{convergence}
$$
</div>


# 
