---
layout: single
permalink: /
title: "Junoh Jung"
excerpt: "Computational fluid dynamics, scientific machine learning, and high-performance computing."
---
<p class="eyebrow">Computational science &amp; fluid mechanics</p>
<p class="lead">Connecting physics, machine learning, and computation to understand, predict and control fluid flows.</p>

I am a Postdoctoral Appointee in the **Mathematics and Computer Science Division at Argonne National Laboratory**, working with Emil Constantinescu (supervisor) and Bethany Lusch (mentor). My research combines computational fluid dynamics, scientific machine learning, and high-performance computing.

I develop hybrid physics–machine-learning methods for PDE simulations and resolvent-based tools for estimating and controlling aerodynamic flows. I received my Ph.D. in Mechanical Engineering from the University of Michigan in 2024, advised by Aaron Towne.

<p class="action-links"><a class="primary-link" href="/research/">Explore my research</a><a href="/files/CV_Jung_Sep2026_public.pdf">Download CV <span aria-hidden="true">↓</span></a></p>

## Research directions

<div class="research-overview"><a href="/research/#differentiable-simulation"><span class="research-index">01</span><h3>Differentiable hybrid physics-ML simulation</h3><p>Learned corrections that work with the structure of numerical PDE solvers.</p></a><a href="/research/#physics-integrated-learning"><span class="research-index">02</span><h3>Physics-integrated flow reconstruction</h3><p>Physical models and B-spline approximation for reconstruction of flow data.</p></a><a href="/research/#flow-estimation-and-control"><span class="research-index">03</span><h3>Flow estimation &amp; control</h3><p>Resolvent-based tools for aerodynamic flows, from airfoils to wakes and jets.</p></a></div>

## Current work

As sole principal investigator, I lead an Argonne LDRD project on **agent-orchestrated multi-fidelity workflows for stable hybrid physics–machine-learning simulations** (April–September 2026). I also lead an ALCF allocation for differentiable hybrid physics–machine-learning simulations.

## Selected publications

{% assign selected = site.publications | where: "selected", true | sort: "year" | reverse %}
{% for paper in selected %}{% include publication-entry.html paper=paper %}{% endfor %}

[View all publications](/publications/)
