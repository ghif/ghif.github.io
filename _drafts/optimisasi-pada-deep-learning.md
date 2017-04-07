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
Salah satu bentuk fungsi *loss*, untuk $$\mathcal{Y} \subseteq \mathbb{R}$$, adalah *least-square error* $$\ell(f_\theta(x), y) = (f_\theta(x) - y)^2$$. 
{: style="text-align: justify;"}

Tulis $$\ell(\theta) := \ell(f_\theta(x), y)$$. Kita definisikan *gradient* dari fungsi *loss* terhadap $\theta$ dengan notasi $$\nabla_\theta \ell$$.






 
# Gradient Descent (GD)
Misalkan $$f_\theta : \mathcal{X} \rightarrow \mathcal{Y}$$

# GD dengan Classical Momentum (CM)

# Nesterov Accelerated Gradient (NAG)

# 
