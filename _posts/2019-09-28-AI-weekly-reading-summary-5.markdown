---
layout: post
title:  "AI Weekly Reading Summary (28 September 2019)"
date: 2019-09-24 00:00 +0000
categories: artificial-intelligence
---

---
#### __1. Adversarial Examples Are Not Bugs, They Are Features__


__Source__: https://arxiv.org/abs/1905.02175

__Authors__: Andrew Ilyas, Shibani Santurkar, Dimitris Tsipras, Logan Engstrom, Brandon Tran, Aleksander Madry

__Topics__: deep learning, adversarial examples

Adversarial examples -- inputs that are slightly perturbed by an imperceptible noise but causing weird behaviour in machine learning models -- have received a great attention, especially since its appearance in the context of deep learning ([Szegedy et al. 2013](https://arxiv.org/pdf/1312.6199.pdf), [Goodfellow et al. 2014](https://arxiv.org/pdf/1412.6572.pdf)).
The impact of such examples has also been studied in some previous work ([Dalvi et al. 2003](https://dl.acm.org/citation.cfm?id=1014066),[Globerson and Roweis 2006](1143889)).
The figure below shows one example of adversarial examples including its unintended behaviour.

<img src="/assets/piggie.png" alt="Adversarial Example" width="80%" height="80%"/>
{: style="text-align: center;"}
**The effect of adversarial noise**
{: style="font-size: 80%; text-align: center;"}

To alleviate such a behaviour, some solutions have been proposed, which mainly focus on building more robust models against the adversarial examples ([Madry et al. 2018](https://arxiv.org/pdf/1706.06083.pdf), [Stutz et al. 2019](http://openaccess.thecvf.com/content_CVPR_2019/papers/Stutz_Disentangling_Adversarial_Robustness_and_Generalization_CVPR_2019_paper.pdf))-- the solutions theirselves now have a name called *adversarial training*.
The assumption held by those work is that adversarial examples will disappear if better algorithms and larger scale data are available.

This paper provides a new perspective on why adversarial examples arise in the first place.
The main observation in this work is the existence of the so-called "non-robust features", which directly attribute to adversarial examples.
__Non-robust features__ are defined as those that are highly predictive, yet brittle and incomprehensible to humans, as opposed to __robust features__, i.e., highly predictive and also human comprehensible. 

This work captures the non-robust features within a theoretical framework and also finds their empirical evidence on a range of image datasets.
The way to find was conducted by disentangling robust and non-robust features via an optimization that results in two separate datasets: robust dataset $$\mathcal{\hat{D}}_R $$ and non-robust dataset  $$ \mathcal{\hat{D}}_{NR}$$.

One interesting outcome from this work is that a classifer trained on the robust dataset $$\mathcal{\hat{D}}_R $$ through *standard training* can already reach a certain level of robustness, i.e., having a good adversarial performance.
Additionally, non-robust datasets are found to be sufficient to produce good standard generalisation tests, but suffer from adversarial tests.
The following figure succinctly summarizes the fore-mentioned outcomes.


<img src="/assets/nonrobust_datasets.png" alt="Robust vs non-robust features with respect to the standard and adversarial training" width="100%" height="100%"/>
{: style="text-align: center;"}
**Robust vs non-robust features with respect to the standard and adversarial training**
{: style="font-size: 80%; text-align: center;"}




#### __2. Billion-scale Commodity Embedding for E-commerce Recommendation in Alibaba__


__Source__: https://arxiv.org/pdf/1803.02349.pdf

__Authors__: Jizhe Wang, Pipei Huang, Zhibo Zhang, Binqiang Zhao, Huan Zhao, Dik Lun Lee

__Topics__: recommender system, graph embedding


Recommender System (RS) is perhaps one of the most widely used AI applications on the Internet these days. 
It plays a central role in many business products, especially e-commerces.

This paper proposes an RS solution for Taobao, the largest customer-to-customer (C2C) platform in China to date. 
There are three main challenges addressed by the proposed solution: scalability, sparsity, and cold start







