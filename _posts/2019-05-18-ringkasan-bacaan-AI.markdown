---
layout: post
title:  "Ringkasan Mingguan Bacaan AI (18 Mei 2019)"
date: 2019-05-18 00:00 +0000
categories: artificial-intelligence
---

### __1. The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks__
---

__Paper Asli__: https://openreview.net/pdf?id=rJl-b3RcF7

Paper ini mendapatkan *best paper award* pada konferensi [ICLR 2019](https://iclr.cc/), yang merupakan salah satu konferensi tingkat atas di bidang *deep learning*.

*Deep neural networks* (DNN) yang memiliki performa terbaik biasanya memiliki arsitektur model yang besar dan mendalam, yang dilatih dengan sejumlah data yang masif.
Pada domain *computer vision*, beberapa arsitektur model populer seperti AlexNet memiliki jumlah parameter sebesar 61 juta dan VGG-16 memiliki jumlah parameter 138 juta.

Arsitektur model yang besar memiliki efek samping yaitu penambahan kompleksitas waktu dan memori baik dari fase pelatihan maupun fase inferensi.
Jika kita memiliki model DNN yang jauh lebih kecil dengan performa akurasi yang serupa dengan model yang besar, itu akan sangat banyak manfaatnya dari sisi aplikasi.
DNN ukuran yang kecil akan lebih mudah untuk diimplementasi pada perangkat *mobile* atau IoT yang notabene memiliki batasan komputasi dan memori dibandingkan komputer normal.

Di beberapa tahun terakhir ada berbagai percobaan untuk memangkas arsitektur model DNN. 
Sebagai contoh, ([Han et al. NIPS 2015](https://arxiv.org/pdf/1506.02626.pdf)) membuat algoritma yang berhasil memangkas DNN hingga ~90% lebih kecil dari model aslinya tanpa mengurangi performa akurasi saat inferensi -- menurunkan parameter AlexNet ke 6.7 juta dan VGG-16 ke 10.3 juta. 

Namun demikian, metode tersebut, yang selanjutnya dikenal dengan *deep compression*, sebatas memangkas model DNN besar yang sebelumnya sudah dilatih, belum menangani bagaimana memangkas DNN pada saat pelatihan.
Pemangkasan pada saat pelatihan akan secara natural meningkatkan efisiensi proses pelatihan. 

Paper ini mengusulkan sebuah algoritma untuk memangkas arsitektur DNN dari saat proses pelatihan.
Algoritma tersebut dilatarbelakangi oleh sebuah hipotesis yang penulisnya namakan sebagai __Lottery Ticket Hypothesis__:
*Sebuah DNN yang parameternya diinisialisasi secara random memiliki sebuah sub-network yang parameternya diinisialisasi sedemikian rupa sehingga apabila sub-network tersebut dilatih, performa akurasinya akan serupa dengan DNN yang besar dengan jumlah iterasi pelatihan yang serupa.*

Algoritma yang diusulkan akan menghasilkan sebuah *sub-network* yang disebut dengan *winning ticket*, yang secara umum terdiri dari 4 tahapan:
1. Inisialisi parameter DNN secara acak: $$f(x; \theta_0)$$, dimana $$ \theta_0 \sim \mathcal{D}_\theta$$.
2. Latih DNN sebanyak iterasi sejumlah $$j$$, menghasilkan parameter $$\theta_j$$.
3. Pangkas $$ p\%$$ dari parameter $$ \theta_j $$ sehingga menghasilkan *mask* $$ m $$.
4. Kembalikan nilai parameter yang tersisa ke nilai pada $$\theta_0$$, yang menghasilkan *winning ticket* $$ f(x; m \odot \theta_0) $$.

Berbagai hasil eksperimen yang dilaporkan pada paper tersebut menunjukkan bahwa hasilnya mendukung *lottery ticket hypothesis* dan secara konsisten mampu menghasilkan *sub-network* yang berukuran ~90% lebih kecil dibandingkan model aslinya melalui proses pelatihan pada dataset MNIST dan CIFAR10.
<!-- Manfaat utama dari algoritma ini adalah membuat proses pelatihan secara keseluruhan lebih efisien dibandingkan cara konvensional. -->
Model dengan parameter yang jauh lebih sedikit mengakibatkan proses inferensi menjadi lebih efisien. 


### __2. A Meta-Transfer Objective for Learning to Disentangle Causal Mechanisms__
---
__Paper Asli__: https://arxiv.org/pdf/1901.10912.pdf

Penulis pertama dari paper ini, Yoshua Bengio, merupakan salah satu pionir di bidang *deep learning* yang baru saja dinobatkan sebagai pemenang [Turing Award 2018](https://www.acm.org/media-center/2019/march/turing-award-2018).
Paper ini membahas tentang *meta-learning* dan bagaimana konsep *causal inference* berpengaruh pada keberhasilan dari *meta-learning*.

*Meta-learning* merupakan sebuah ide pada *machine learning* agar sebuah model AI dapat mempelajari kemampuan baru dengan cepat dan dengan hanya membutuhkan sedikit data latih. 
Metode *machine learning* konvensional biasanya membutuhkan data yang banyak dan waktu yang cukup lama untuk melatih sebuah agen AI dengan kemampuan yang mumpuni.
*Meta-learning*, jika dijalankan dengan sukses, akan membawa *machine learning* menjadi jauh lebih efisien, baik dari segi proses pelatihan maupun kebutuhan data latih.


Problem yang lebih fundamental yang mungkin dapat diselesaikan dengan *meta-learning* adalah problem adaptasi.
Biasanya sebuah model AI akan melakukannya tugasnya dengan baik apabila kondisi atau distribusi antara data latih dengan lingkungan aktual tidak jauh berbeda.
Jika distribusi tersebut berbeda, model AI akan kehilangan kemampuan generalisasi terhadap lingkungan aktual.
Akan lebih baik jika model AI dapat beradaptasi pada lingkungan aktual dengan mengambil sedikit (1 atau 2) langsung dari lingkungan tersebut, kemudian melatih dirinya kembali. 
Dengan demikian, kemampuan *meta-learning* akan berimplikasi pada kemampuan adaptasi yang baik.


*Causal inference* merupakan ide lain yang mencoba menangkap hubungan kausalitas (sebab-akibat) dari dua buah variabel.
Ide ini memungkinkan untuk melakukan intervensi terhadap proses prediksi dari suatu model AI. 


Sebagai contoh, misal $$X$$ merupakan metode pengobatan dan $$Y$$ merupakan kondisi kesehatan. 
Model yang memiliki kemampuan *causal inference* akan mampu menjawab pertanyaan yang bersifat intervensi seperti ini: 
jika obat yang lama $$X=a$$ diganti dengan obat yang baru $$ X=b $$, apa yang akan terjadi pada kondisi kesehatan pasien $$Y$$?
Kemampuan ini tidak dimiliki oleh metode *machine learning* standar yang pada umumnya berbasis korelasi.

Singkatnya, paper ini mencoba menangkap hubungan kausalitas antara *distribusi data latih* dengan distribusi lingkungan tempat model AI dijalankan, yang diistilahkan dengan *distribusi target*.
Dengan memodelkan kausalitas antara kedua distribusi tersebut, proses *meta-learning* akan berlangsung dengan lebih efektif dan efisien.

Secara keseluruhan, penyampaian argumen-argumen dari paper ini sangat teoretis dan matematis sehingga agak sulit untuk dipahami bagi yang belum familiar dengan berbagai konsep matematika yang melandasi *machine learning*.

