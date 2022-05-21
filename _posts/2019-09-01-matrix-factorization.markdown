---
layout: post
title:  "Matrix Factorization dengan Alternating Least Squares (ALS)"
date: 2019-09-01 00:00 +0000
categories: math
published: false
---

---
Misalnya terdapat sebuah matriks $$ \mathbf{R} \in \mathbb{R}^{n \times m}$$, dimana $$ n $$ dan $$ m $$ biasanya cukup besar, kita dapat membaginya menjadi perkalian matriks-matriks dengan ukuran yang lebih kecil:


$$
\label{eq:mf}
\mathbf{R} \approx \mathbf{U} \mathbf{V}^\top
$$ 

dimana $$\mathbf{U} \in \mathbb{R}^{n \times d} $$ dan $$ \mathbf{V} \in \mathbb{R}^{m \times d}$$.
Dimensi $$ d $$ biasanya jauh lebih kecil dibandingkan $$ n $$ dan $$ m $$. 

Konsep ini dikenal dengan istilah __matrix factorization__ atau __matrix decomposition__ -- matrix $$\mathbf{U}$$ dan $$\mathbf{V}$$ disebut dengan *latent factors*. 
Pada bilangan 1D, faktorisasi merupakan hal yang sudah sangat familiar, seperti $$ 6 = 2 \times 3 $$.


Mengapa kita membutuhkan faktorisasi pada matriks? Alasan utamanya adalah untuk membuat komputasi objek-objek matriks yang berjalan setelahnya menjadi lebih sederhana atau efisien.
Saat ini telah banyak metode untuk melakukan faktorisasi matriks yang didesain untuk kebutuhan-kebutuhan tertentu seperti LU decomposition, QR decomposition, Cholesky decomposition, Singular value decomposition, Alternating Least-Squares (ALS), dan sebagainya.


#### Contoh Efisiensi: Penyelesaian Sistem Persamaan Linear 

