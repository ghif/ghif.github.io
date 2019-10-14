---
layout: post
title:  "Ringkasan Mingguan Bacaan AI (12 Oktober 2019)"
date: 2019-10-12 00:00 +0000
categories: artificial-intelligence	
---

---
#### __1. Deep Learning: A Critical Appraisal__


__Source__: https://arxiv.org/pdf/1801.00631.pdf

__Authors__: Gary Marcus

__Topics__: deep learning

Artikel ini ditulis oleh [Gary Marcus](https://en.wikipedia.org/wiki/Gary_Marcus), seorang ilmuwan kognitif, pengusaha, dan penulis buku yang cukup terkenal dengan kajian-kajian kritisnya mengenai *artificial intelligence* (AI) dan *deep learning* (DL).
Pada tulisan ini Gary menekankan 10 hal yang menjadi kekhawatiran akan DL dan bahwa DL harus didukung dengan metode-metode lainnya untuk menghasilkan [*artificial general intelligence*](https://en.wikipedia.org/wiki/Artificial_general_intelligence).


Walaupun kritik-kritik yang disampaikan terkadang cukup tajam dan sikapnya yang hampir selalu skeptis terhadap *deep learning*, menurut saya pemikirannya tetap layak untuk dicermati atau dijadikan bahan perenungan.
Seringkali *deep learning* diberitakan secara hiperbolis dan cenderung menyesatkan, terutama oleh media-media, baik disengaja ataupun tidak disengaja. 
Informasi-informasi hiperbolis tersebut membuat *deep learning* seolah-olah menjadi jawaban terhadap semua masalah.
Hal tersebut bisa membuat kesan yang salah atau ekspektasi yang terlalu tertinggi terhadap AI atau *deep learning*, terutama dari sudut pandang awam.


Jika impresi tersebut mempengaruhi para pelaku bisnis atau investor sehingga terlalu percaya diri untuk berinvestasi besar-besaran dalam pengembangan AI, maka bersiaplah untuk mengalami kekecewaan karena bisa jadi apa yang diinvestasikan jauh tidak sebanding dengan yang dihasilkan.
Ini salah satu penyebab terjadinya *AI winter* pada tahun 1970-an, dimana para pemegang dana (pemerintah maupun swasta) berbalik menjadi pesimis untuk berinvestasi, yang menyebabkan riset dan pengembangan AI menjadi stagnan.


Dalam konteks tersebut, pemikiran dari Gary Marcus bermanfaat sebagai penyeimbang (walaupun bisa tidak sepenuhnya sependapat pula dengan Gary) agar publik tidak salah dalam menilai kemampuan AI atau DL yang sesungguhnya saat ini.
Dengan pemahaman yang lebih tepat mengenai apa yang bisa atau tidak bisa dilakukan oleh DL, maka para pemegang dana akan lebih paham dengan apa yang mereka investasikan sehingga bisa mengambil keputusan dengan lebih tepat pula.


Berikut ini merupakan 10 tantangan yang dimiliki oleh DL yang disampaikan oleh Gary Marcus pada artikel berjudul "Deep Learning: A Critical Appraisal":
1. DL sangat *lapar* terhadap data.
2. DL sebenarnya masih dangkal dan memiliki kapasitas terbatas untuk transfer kemampuannya.
3. DL tidak mudah untuk menangani representasi dengan struktur hirarkis.
4. DL kesulitan untuk melakukan inferensi yang *open-ended*.
5. DL tidak cukup transparan.
6. DL cukup sulit terintegrasi dengan *prior knowledge*.
7. DL tidak bisa menangkap kausalitas (hubungan sebab akibat) dari korelasi.
8. DL menganggap dunia/lingkungan tempat ia dioperasikan berkeadaan stabil atau past.
9. DL bekerja dengan baik sebagai alat prediksi / perkiraan, namun terkadang hasilnya tidak dapat sepenuhnya dipercaya.
10. DL relatif sulit untuk direkayasa.


Sumber-sumber lain mengenai kajian kritis mengenai AI / DL semacam ini dapat dilihat di [halaman yang disusun dengan baik oleh Thomas Nield](https://github.com/thomasnield/ai-appraisal-and-hype-articles).

#### __2. The Neuro-Symbolic Concept Learner: Interpreting Scenes, Words, and Sentences from Natural Supervision__


__Source__: https://arxiv.org/pdf/1801.00631.pdf

__Authors__: Jiayuan Mao, Chuang Gan, Pushmeet Kohli, Joshua B. Tenenbaum, Jiajun Wu

__Topics__: deep learning, computer vision, symbolic reasoning, concept learning


Paper ini mengemukakan sebuah model bernama Neuro-Symbolic Concept Learner (NS-CL), yang mencoba mempelajari konsep visual, kata-kata, dan penguraian semantik dari kalimat-kalimat secara simultan tanpa supervisi yang eksplisit.
Model tersebut hanya mengandalkan data gambar beserta pasangan kalimat tanya-jawab (QA) terkait gambar tersebut.
Cara bagaimana NS-CL belajar dan melakukan inferensi diilustrasikan pada gambar di bawah ini.

<img src="/assets/nscl_learning.png" alt="NS-CL Learning" width="80%" height="80%"/>
{: style="text-align: center;"}
**Ilustrasi bagaimana NS-CL belajar (disebut dengan istilah *curriculum learning*) dan inferensi untuk VQA (Visual Question Answering)**
{: style="font-size: 80%; text-align: center;"}

NS-CL dilatih dengan cara *curriculum learning*: mulai belajar dengan konsep-konsep visual sederhana terlebih dahulu seperti bentuk, warna, dll, lalu mempelajari hal-hal yang lebih kompleks (contoh: relasi antar objek, ekspresi referensial, konsep berstruktur hirarkis), tahap demi tahap.
NS-CL memiliki 3 buah modul: 1) modul persepsi berbasis *neural network* yang mengekstraksi representasi level objek dari suatu gambar, 2) pengurai semantik untuk menerjemahkan pertanyaan-pertanyaan dalam bahasa alami menjadi program-program yang dapat dieksekusi, 3) eksekutor program simbolik yang membaca representasi perseptual dari objek-objek, mengklasifikasi atribut dan relasi objek-objek tersebut, dan mengeksekusi program untuk mendapatkan jawaban yang tepat.

Sederhananya, NS-CL memadukan antara *deep learning* dan *symbolic reasoning* untuk menjembatani proses belajar konsep-konsep visual, kata-kata, dan juga pengurai semantik dari kalimat-kalimat secara simultan. 
Gambar di bawah ini menunjukkan integrasi tersebut.

<img src="/assets/nscl_symbolic_reasoning.png" alt="NS-CL Symbolic Reasoning" width="80%" height="80%"/>
{: style="text-align: center;"}
**Ilustrasi *neural symbolic reasoning* pada model NSCL**
{: style="font-size: 80%; text-align: center;"}

Model NS-CL mammpu menghasilkan performa teratas pada problem Visual Question-Answering (VQA) diuji dengan dataset CLEVR. 
Yang lebih menariknya, NS-CL juga mendemonstrasikan kemampuan generalisasi yang efektif, yang dievaluasi dalam 4 bentuk.
Salah satunya adalah kemampuan untuk beradaptasi melakukan pekerjaan yang lain, seperti mempelajari warna yang baru dan melakukan pekerjaan *image-caption retrieval* tanpa tambahan proses belajar.

Perpaduan antara *deep learning* dan paradigma AI yang lain, contohnya *symbolic reasoning* seperti yang dijalankan oleh NS-CL, secara umum sangat menarik untuk diteliti dan dikaji. 
Paradigma-paradigma tersebut diharapkan akan saling mengatasi kekurangan masing-masing sehingga mampu menghasilkan metode AI yang lebih kuat.	 

