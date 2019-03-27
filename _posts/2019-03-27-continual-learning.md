---
layout: post
title:  "Continual Learning: Pembeda Utama Cara Belajar Manusia vs Komputer?"
date: 2019-03-27 00:00 +0000
categories: artificial-intelligence
---

<img src="/assets/lifelong-learning.jpg" width="750"/>
{: style="font-size: 80%; text-align: center;"}
**Gambar 1**. Sumber: http://netprofitgrowth.com/business-learning/
{: style="font-size: 80%; text-align: center;"}

Ada sebuah fenomena yang menarik dari kemampuan otak manusia dalam mempelajari hal baru. Otak kita dapat belajar berkesinambungan akan kemampuan yang baru tanpa (benar-benar) melupakan hal-hal yang telah dipelajari sebelumnya. Lebih hebatnya lagi, kita dapat mentransfer kemampuan yang sudah ada sehingga lebih mudah untuk mempelajari hal-hal baru yang berkaitan.

Salah satu contoh fenomena ini adalah proses belajar berbahasa. Bayangkan Anda baru mulai belajar, misalnya, bahasa Spanyol. Di fase awal Anda mempelajari huruf-huruf / unsur-unsur terkecil dari bahasa Spanyol. Kemudian Anda menghafal berbagai kosa kata. Selanjutnya Anda belajar menyusun frasa dan kalimat dari kosa kota tersebut. 

Kesemuanya itu berkesinambungan: ketika belajar merangkai kalimat, Anda tidak melupakan bagaimana caranya menyusun frasa dan arti dari kosa kata yang sudah dihafal. Sebaliknya, justru yang sudah Anda pelajari sebelumnya, yaitu menyusun frasa, akan sangat membantu kefasihan merangkai kalimat. Bandingkan jika Anda langsung melompat untuk mempelajari kalimat tanpa tahu frasa dan kosa kata.

Sekarang bayangkan Anda sudah mahir berbahasa Spanyol. Selanjutnya Anda ingin mempelajari bahasa Italia. Dikarenakan bahasa Spanyol dan Italia [cukup dekat](https://bigthink.com/strange-maps/a-map-of-lexical-distances-between-europes-languages), Anda akan merasa bahasa Italia relatif lebih mudah dipahami, dibandingkan orang lain yang langsung belajar bahasa Italia tanpa tahu bahasa Spanyol. Disaat yang bersamaan Anda tidak lupa dengan berbahasa Spanyol selagi belajar bahasa Italia.

Kemampuan otak manusia yang luar biasa ini dikenal dengan istilah __*continual learning*__ (CL) atau __*lifelong learning*__ atau __*incremental learning*__. Studi neurosains mengindikasikan bahwa continual learning benar-benar terjadi secara biologis pada otak mamalia [[Cichon & Gan, 2015](https://www.ncbi.nlm.nih.gov/pubmed/25822789)].

Inilah salah satu aspek yang masih belum dimiliki oleh teknik kecerdasan buatan atau pemelajaran mesin saat ini. Deep neural networks yang sangat sukses dalam 1 dekade terakhir di berbagai aplikasi pun belum memiliki kemampuan ini. Algoritma pemelajaran konvensional pada deep neural networks mengalami apa yang disebut sebagai *catastrophic forgetting* [[McCloskey and Cohen 1989](https://www.sciencedirect.com/science/article/pii/S0079742108605368), [Goodfellow et al. 2014](https://arxiv.org/abs/1312.6211)]: ketika algoritma pembelajaran menerima data yang baru, deep neural networks akan dengan cepat melupakan hal yang lama.

#### __Continual Learning pada Kecerdasan Buatan__

Saat ini Continual Learning (CL) sudah mulai mendapat perhatian serius oleh komunitas kecerdasan buatan dan pemelajaran mesin. DARPA (Defense Advanced Research Projects Agency) meluncurkan proyek riset khusus bernama [Lifelong Learning Machines (L2M)]( https://www.darpa.mil/program/lifelong-learning-machines) untuk mengembangkan agen kecerdasan buatan yang lebih mumpuni.
Dalam beberapa tahun terakhir, Neural Information Processing Systems (NeurIPS), yang merupakan salah satu konferensi yang paling bereputasi dan berpengaruh di bidang pembelajaran mesin, mengadakan [*workshop* khusus dengan tema Continual Learning](https://sites.google.com/view/continual2018).


Perkembangan CL akan mendorong cara belajar kecerdasan buatan semakin mendekati cara belajar otak biologis.
Lalu apa keuntungan dari sisi praktis? Paling tidak, akan ada dua keuntungan:

1. __Skalabilitas__

	Jika ada data yang baru untuk dipelajari, misalnya berjumlah 10 sampel, algoritma pemelajaran mesin konvensional mesti melalui proses belajar dari awal yang mengikutsertakan data sebelumnya ditambah dengan 10 sampel yang baru sebagai data latih. Proses ini disebut juga sebagai __*offline learning*__. 

	Seiring dengan penambahan data, proses *offline learning* akan menjadi tidak efisien. Bayangkan jika data sebelumnya sudah berjumlah 1 juta sampel dan data yang baru hanya 10 sampel -- untuk memasukkan pengetahuan baru dari 10 sampel tersebut akan membutuhkan kompleksitas *training* yang sama atau bahkan lebih dari 1 juta sampel.

	CL membuka peluang untuk melakukan __*online learning*__: agen kecerdasan buatan hanya cukup untuk dilatih dengan 10 sampel yang baru tanpa melupakan pengetahuan sebelumnya, tanpa harus mengikutsertakan 1 juta sampel sebelumnya.


2. __Kemampuan Adaptasi__
	
	Algoritma pemelajaran mesin konvensional dirancang hanya untuk melakukan tugas atau domain tertentu saja.
	Dengan kata lain, agen kecerdasan buatan dengan algoritma standar secara umum bersifat sebagai spesialias yang tidak mampu beradaptasi dengan tugas yang baru.

	CL memungkinkan agen kecerdasan buatan untuk beradaptasi dengan tugas yang baru tanpa melupakan tugas yang lama, disaat yang bersamaan kemampuan dalam melaksanakan tugas yang lama akan menyokong untuk mempelajari kemampuan yang baru. 
	Kemampuan ini membuat agen kecerdasan buatan mampu untuk terus belajar pada dunia yang dinamis, yang terus berubah-ubah seiring dengan berjalannya waktu. 
	Karakteristik tersebut lebih dekat dengan dunia nyata dibandingkan *offline learning* pada algoritma konvensional.

Sebuah perangkat lunak bernama *[neurala](https://www.neurala.com/press-releases/edge-deep-learning-without-cloud)* merupakan contoh konkrit yang mencoba memiliki kedua hal tersebut.
Neurala mengklaim dapat melakukan *continual learning* secara efisien pada perangkat-perangkat keras *low-end* atau *client-side* seperti *drone*, kamera digital, atau ponsel pintar, tanpa harus terhubung pada server.

	
#### __Perkembangan Riset Terkini__

Ketertarikan komunitas peniliti pemelajaran mesin terhadap Continual Learning semakin meningkat setiap tahunnya, seperti yang ditunjukkan pada grafik di bawah ini:

<img src="/assets/CL_interest.png" width="750"/>
{: style="font-size: 80%; text-align: center;"}
**Gambar 2**. Grafik jumlah publikasi artikel ilmiah yang bertema *continual learning* berdasarkan kata kunci "continual learning", "lifelong learning", dan lain-lain. Sumber: https://www.continualai.org/#home, 
{: style="font-size: 80%; text-align: center;"}

Salah satu metode yang akhir-akhir ini cukup populer adalah __Elastic Weight Consolidation (EWC)__ [[Kirkpatrick et al. 2017](https://arxiv.org/pdf/1612.00796.pdf)].
Metode ini dikembangkan terinspirasi dari temuan neuro-biologis pada *neocortical circuits* otak mamalia. 
Suatu observasi pada otak tikus mengindikasikan bahwa mempelajari suatu hal berasosiasi dengan pembentukan atau penguatan koneksi *synapses*. Yang lebih menarik lagi, ketika belajar hal yang baru setelahnya, koneksi *synapses* yang sebelumnya terbentuk tidak serta merta hilang, namun membentuk koneksi yang baru [[Yang et al. 2009](https://www.nature.com/articles/nature08577)].
Fenomena ini diilustrasikan pada Gambar 3 di bawah ini.


<img src="/assets/dendrites.png" width="750"/>
{: style="font-size: 80%; text-align; center:"}
**Gambar 3**. Ilustrasi koneksi *synapses* yang terbentuk berkaitan dengan proses belajar dan pembentukan memori.
Sumber: https://www.cell.com/current-biology/pdf/S0960-9822(09)02203-9.pdf
{: style="font-size: 80%; text-align: center;"}


EWC menerjemahkan observasi di atas dengan memodifikasi algoritma deep learning standar dengan memberikan penalti / batasan pada proses pemutakhiran bobot koneksi *neural networks*. 
Penalti tersebut berupa *soft freezing* pada koneksi yang dianggap penting sehingga koneksi yang sudah terbentuk sebelumnya tidak langsung hilang ketika memproses data yang baru.
Seberapa penting suatu koneksi untuk diperhatikan ditentukan berdasarkan data dengan menghitung *Fisher-information matrix* dari bobot koneksi *neural networks*.


Contoh metode yang lain yaitu *generative replay* [[Shin et al. 2017](https://papers.nips.cc/paper/6892-continual-learning-with-deep-generative-replay.pdf)].
Metode ini mencoba mengatasi *catastrophic forgetting* pada *neural networks* dengan memanfaatkan *generator* (yang juga merupakan *neural networks*) yang men-*generate* balik input yang dipelajari pada problem sebelumnya.
Input hasil produksi dari *generator* tersebut digunakan oleh model utamanya sebagai *pivot* ketika modelnya dilatih dengan data yang baru agar modelnya tetap memiliki pengetahuan sebelumnya.

#### __Penutup__
Saat ini pengembangan riset di bidang Continual Learning dapat dikatakan masih dalam tahap prematur. 
Masih banyak hipotesis yang perlu diuji dan problem yang perlu dipecahkan.
Jika berhasil, Continual Learning akan semakin mendekatkan kecerdasan buatan dengan kecerdasan manusia.

#### __Referensi__
1. [[Cichon & Gan 2015](https://www.ncbi.nlm.nih.gov/pubmed/25822789)] J. Cichon and W. Gan. “Branch-specific dendritic ca2+ spikes cause persistent synaptic plasticiy.”. Nature, 520(7546):180-185, 2015.

2. [[Goodfellow et al. 2014](https://arxiv.org/abs/1312.6211)] I. J. Goodfellow, M. Mirza, D. Xiao, A. Courville, Y. Bengio. “An empirical investigation of catastrophic forgetting in gradient-based neural networks”. International Conference on Machine Learning (ICML), 2014.

3. [[McCloskey & Cohen 1989](https://www.sciencedirect.com/science/article/pii/S0079742108605368)] M. McCloskey and N. J. Cohen. “Catastrophic interference in connectionist networks: The sequential learning problem”. Psychology of Learning and Motivation, 1989.

4. https://sites.google.com/view/continual2018

5. https://www.neurala.com/press-releases/edge-deep-learning-without-cloud

6. [[Kirkpatrick et al. 2017](https://arxiv.org/pdf/1612.00796.pdf)] Kirkpatrick et al. "Overcoming catastrophic forgetting in neural networks". PNAS, 2017.

7. https://www.continualai.org/

8. [[Yang et al. 2009](https://www.nature.com/articles/nature08577)] G. Yang, F. Pan, W-B. Gan. "Stably maintained dendritic spines are associated with lifelong learning". Nature, 2009.

9. [[Shin et al. 2017](https://papers.nips.cc/paper/6892-continual-learning-with-deep-generative-replay.pdf)] H. Shin, J. K. Lee, J. Kim, J. Kim. "Continual learning with deep generative replay". NIPS, 2017.


