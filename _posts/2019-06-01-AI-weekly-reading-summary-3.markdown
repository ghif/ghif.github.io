---
layout: post
title:  "AI Weekly Reading Summary (1 June 2019)"
date: 2019-06-01 00:00 +0000
categories: artificial-intelligence
---

---
#### __1. How to train your MAML__


__Source__: https://arxiv.org/pdf/1810.09502.pdf

__Authors__: Antreas Antoniou, Amos Storkey, Harrison Edwards

__Topics__: meta learning, few-shot learning

Model Agnostic Meta Learning (MAML) ([Finn et al. 2017](https://arxiv.org/pdf/1703.03400.pdf)) is an elegantly simple meta-learning algorithm yet produces state-of-the-art results in few-shot learning problems. 
MAML is also general enough in the sense that it can be applied on any gradient-based algorithms.
In short, the way that MAML works is to provide good initialization parameters for a model such that after a few steps of standard training on a few-shot task, the model will perform well on that task.

Few-shot learning is concerned with constructing a good ML model trained from a few examples.
A successful few-shot learning will be very useful in the context of supervised learning as it will reduce a huge amount of effort in annotating the training examples.

Despite its success, some technical problems in MAML that may hinder its true potential remain unsolved.
This paper investigates the problems such as training instability, absence of batch normalization statistic accumulation, non-optimal generalization and convergence speed due to fixed learning rate, etc, and proposes solutions to those problems.

The resulting algorithm, referred to as MAML++, was evaluated on the [Omniglot](https://github.com/brendenlake/omniglot) and [Mini-Imagenet](https://github.com/y2l/mini-imagenet-tools) datasets.
The outcomes show some superiorities of MAML++ over MAML both in stability and generalization performance.

<img src="/assets/MAMLpp.png" alt="MAML vs MAML++" width="80%" height="80%"/>
{: style="text-align: center;"}
**Comparison between MAML vs MAML++**
{: style="font-size: 80%; text-align: center;"}

---
#### __2. Data-efficient image recognition with contrastive predictive coding__

__Source__: https://arxiv.org/pdf/1905.09272.pdf

__Authors__ : Olivier J. Henaff, Ali Razavi, Carl Doersch, S. M. Ali Eslami, Aaron van der Oord

__Topics__: computer vision, semi-supervised deep learning

Biological vision is thought to leverage vast amounts of unlabeled data to perform self-supervised learning as a prior to support object classification tasks with limited supervision.
Computer vision has so far not quite succeeded in mimicing such the mechanism.
The most successful image classifier is built upon deep learning that is typically label-hungry.
It is desirable to have a system that can be trained on a small amount of labeled data.

This paper handles the small-label challenge by adapting a recent self-supervised learning algorithm called Contrastive Predictive Coding (CPC) ([van den Oord et al. 2018](https://arxiv.org/pdf/1807.03748.pdf)) with an unusually deep and wide residual network, layer normalization rather than batch normalization, and predicting both lower- and higher-level features.
The pretrained network is then used to extract deep representations as inputs to a standard linear classifier.

From the evaluation on ImageNet dataset, this strategy outperforms AlexNet model that is trained with full supervision, with 61% Top-1 and 83% Top-5 accuracies -- 	AlexNet's accuracies are 59.3% Top-1 and 81.8% Top-5, respectively).
When given a small number of labeled images (as few as 13 labels per class), this model retrains a strong classification performance, surpassing state-of-the-art semi-supervised methods by 10% Top-5 accuracy and supervised methods by 20%.

Learning from a small data is a limitation for deep learning, which is typically label-hungry.
This work opens a new regime in tasks of which only a few labels are available such as detecting rare diseases, spotting defects in a retail pipeline, detecting anomalies/unusual actions in video surveillance, etc.

<!-- ![result example](/assets/cpc_results.png) -->
<img src="/assets/cpc_results.png" alt="CPC Result" width="60%" height="60%"/>
{: style="text-align: center;"}
**Classification accuracy comparison between self-supervision with CPC and fully supervised ResNet as a function of the number of labeled examples.**
{: style="font-size: 80%; text-align: center;"}

---
#### __3. Understanding convolutional neural networks for text classification__

__Source__: https://www.aclweb.org/anthology/W18-5408

__Authors__: Alon Jacovi, Oren Sar Shalom, Yoav Goldberg

__Topics__: deep learning, NLP

This paper investigates the interpretability of convolutional networks that are trained for text classification.
Interpretablity is about presenting a structured explanation which captures what an ML model has learned, which is important to increase trust in model predictions, analyze errors or improve the model ([Riberio et al. 2016](https://arxiv.org/pdf/1602.04938.pdf)).

There have been a number of works that address the interpretability of deep learning models on NLP tasks. 
However, this area is still generally under-explored, particularly in comparison to computer vision tasks.
Furthermore, the proposed methods for interpreting computer vision models may not be directly applicable for NLP models.

A common wisdom in terms of 1D-CNN applied on texts is that convolutional filters followed by global max-pooling serve as ngram detectors.
This work identifies and refines current intuitions as to how 1D-CNNs work on text domain.
Some key takeaways are as follows:
- Max-pooling induces a thresholding behaviour, and values below a given threshold are ignored when making a prediction.
- Filters are not homogeneous, i.e., a single filter can, and often does, detect multiple distinctly different families of ngrams.
- Filters also detect negative items in ngrams.










