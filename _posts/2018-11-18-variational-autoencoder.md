---
layout: post
title:  "Variational Autoencoder: Membangun Model Generatif dengan Neural Networks"
date: 2018-11-18 00:00 +1300
categories: Machine Learning
published: false
---

Salah satu aspek penting dari pemelajaran mesin adalah membangun model generatif. 
Model generatif 

Bayangkan kita memiliki sebuah model atau alat yang bisa menghasilkan 
Model generatif 



#### __Model Generatif: perspektif Bayesian networks__
Model generatif biasanya diilustrasikan dengan *probabilistic graphical model (PGM)* dalam bentuk Bayesian networks. 

Teori Bayes:

$$
\begin{eqnarray}
P(x | y) = \frac{P(y|x) P(y)} {P(x)}
\end{eqnarray}
$$

#### __Variational Bayesian Inference__

Problem optimisasi pada Variational inference:

$$
\begin{eqnarray}
\label{eq:varopt}
Q_\phi^* := \arg \min_{Q_\phi} \mathrm{KL}(Q_\phi \| P)
\end{eqnarray}
$$

$$ Q^* $$ disebut sebagai distribusi aproksimasi.


$$
\displaystyle
\begin{eqnarray}
\mathrm{KL}\left( Q_{\phi}(z) \| P(z | x) \right) &=& 
\sum_{z \sim Q_{\phi}(z)} Q_\phi(z) \log{ \frac{Q_\phi(z)} {P(z|x)} } =
- \sum_{z \sim Q_{\phi}(z)} Q_\phi(z) \log{ \frac{P(z|x)} {Q_\phi(z)} } =
- \sum_{z \sim Q_{\phi}(z)} Q_\phi(z) \log{ \frac{P(x, z)} {P(x) Q_\phi(z)} } 
\nonumber \\

&=& - \sum_{z \sim Q_{\phi}(z)} Q_\phi(z) \log{ P(x, z) } -  Q_\phi(z) \log{P(x)} - Q_\phi(z) \log{Q_\phi(z)} \nonumber \\
&=& \log{P(x)} - \sum_{z \sim Q_\phi(z)} Q_\phi(z) \log{ \frac{P(x, z)} {Q_\phi(z)} } \nonumber \\
\end{eqnarray}
$$

Persamaan terakhir di atas dapat kita susun menjadi persamaan berikut:

$$
\displaystyle
\begin{eqnarray}
\label{eq:elbo1}
\log{ P(x) } = \mathrm{KL}\left( Q_{\phi}(z) \| P(z | x) \right) + \mathcal{L}(Q_\phi(z))
\end{eqnarray}
$$

dimana $$ \mathcal{L}(Q_\phi(z)) = \sum_{z \sim Q_\phi(z)} \log{ \frac{P(x, z)} {Q_\phi(z)} }$$ merupakan kuantitas yang dikenal dengan istilah *evidence lower bound (ELBO)*.

Persamaan ($$ \ref{eq:elbo1} $$) penting untuk dipahami lebih mendalam karena di sini kunci utama trik komputasi *variational inference*.
Perhatikan bahwa kuantitas pada ruas kiri $$ \log{ P(x)} $$ tidak berubah atau konstan.  
Ingat kembali bahwa tujuan optimisasi di sini yaitu untuk meminimalkan divergensi $$ \mathrm{KL} $$ antara $$ Q $$ dan $$ P $$, seperti pada persamaan ($$ \ref{eq:varopt}$$).

#### __Referensi__
[[Kingma & Welling ICLR2014] "Auto-Encoding Varitional Bayes"](https://arxiv.org/abs/1312.6114)
