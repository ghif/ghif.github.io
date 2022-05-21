---
layout: post
title:  "Wasserstein Distances"
date: 2018-12-06 00:00 +1300
categories: Machine Learning, Unsupervised Learning
published: false
---

Suppose we have a real data distribution 
$${\mathbb P_r} $$ and model distribution $$ {\mathbb P_g} $$, we define Earth-Mover (EM) or 1-Wassertein distance as

$$
\displaystyle
\begin{equation} 
\displaystyle
W({\mathbb P_r}, {\mathbb P_g}) = 
\inf_{\gamma \in \Pi({\mathbb P_r}, {\mathbb P_g}) } 
{\mathbb E_{(x, y) \sim \gamma}} \left[ \| x - y \| \right]
\end{equation}
$$


where $$ \Pi({\mathbb P_r}, {\mathbb P_g}) $$ is the set of all joint distributions $$ \gamma(x, y)$$ with marginals $$ {\mathbb P_r} $$ and $$ {\mathbb P_g} $$, respectively.

