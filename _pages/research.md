---
{"permalink": "/research/", "title": "Research"}
---
<p class="lead">Physics and learning, working together.</p>

My research connects numerical simulation, scientific machine learning, and flow dynamics. I study how physical structure can guide learning, and how models of fluid motion can inform estimation and control.

<section class="research-topic" markdown="1">

<h2 id="differentiable-simulation"><span class="research-index">01 / </span>Differentiable simulation</h2>

<p class="research-question">How can we make PDE simulations more efficient while retaining the structure of numerical solvers?</p>

### Approach

I study differentiable weak-form corrections for finite element simulations and hybrid physics–machine-learning methods for coarse-grid incompressible-flow simulation. This work connects learned corrections with existing numerical discretizations and high-performance computing.

<div class="method-flow" role="img" aria-label="Conceptual workflow: PDE discretization, then Learned weak-form correction, then Corrected simulation"><span>PDE discretization</span><b aria-hidden="true">→</b><span>Learned weak-form correction</span><b aria-hidden="true">→</b><span>Corrected simulation</span></div>
<p class="diagram-note">Conceptual workflow.</p>

### Representative work

[Learning Differentiable Weak-Form Corrections to Accelerate Finite Element Simulations](/publications/#conference-3), ASME FEDSM (2026). The related journal manuscript is to be submitted.

</section>

<section class="research-topic" markdown="1">

<h2 id="physics-integrated-learning"><span class="research-index">02 / </span>Physics-integrated learning</h2>

<p class="research-question">How can physical models and learning work together to reconstruct flow data and support scalable simulations?</p>

### Approach

My work includes physics-informed B-spline reconstruction, hybrid physics–machine-learning acceleration of spectral element solvers, and agent-orchestrated multi-fidelity simulation workflows. I investigate how these approaches can combine physical information, numerical models, and learning in scientific-computing workflows.

<div class="method-flow" role="img" aria-label="Conceptual workflow: Flow data & physics, then B-spline / hybrid model, then Reconstruction & prediction"><span>Flow data & physics</span><b aria-hidden="true">→</b><span>B-spline / hybrid model</span><b aria-hidden="true">→</b><span>Reconstruction & prediction</span></div>
<p class="diagram-note">Conceptual workflow.</p>

### Representative work

Physics-Informed B-spline Reconstruction of Flow Data, *Computer Methods in Applied Mechanics and Engineering* (under review, 2026). Related work includes a hybrid spectral element solver (AIAA Aviation, 2026) and an agent-orchestrated multi-fidelity workflow (AIAA SciTech 2027, accepted). [Publication details](/publications/)

</section>

<section class="research-topic" markdown="1">

<h2 id="flow-estimation-and-control"><span class="research-index">03 / </span>Flow estimation and control</h2>

<p class="research-question">How can we estimate and control aerodynamic flows using models of their input–output dynamics?</p>

### Approach

I develop resolvent-based methods for flow estimation and control, with applications to airfoil flows, turbulent wakes, and jets. My research spans Wiener–Hopf formulations for optimal estimation and control, efficient harmonic resolvent analysis, and flow-specific estimation and control methods.

<div class="method-flow" role="img" aria-label="Conceptual workflow: Flow measurements, then Resolvent-based estimator, then Estimation & control"><span>Flow measurements</span><b aria-hidden="true">→</b><span>Resolvent-based estimator</span><b aria-hidden="true">→</b><span>Estimation & control</span></div>
<p class="diagram-note">Conceptual workflow.</p>

### Representative work

[Resolvent-based estimation of a turbulent wake](https://doi.org/10.1017/jfm.2026.11444), *Journal of Fluid Mechanics* (2026); [Resolvent-based estimation and control of a laminar airfoil wake](https://doi.org/10.1017/jfm.2025.10423), *Journal of Fluid Mechanics* (2025).

### Representative result

<figure class="research-figure">
<a href="/images/jfm-2026-figure16.png"><img src="/images/jfm-2026-figure16.png" width="3821" height="3040" loading="lazy" alt="LES reference fields and resolvent-based estimates of streamwise velocity fluctuations in an airfoil wake at three times, shown as spanwise averages and on the mid-span plane."></a>
<figcaption>Streamwise velocity fluctuations in a turbulent airfoil wake: large-eddy simulation (LES) compared with estimates from four sensors at three times. <a href="https://doi.org/10.1017/jfm.2026.11444">Jung &amp; Towne (2026), Figure 16</a>, <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>. Reproduced without alteration. Select the figure to view at full resolution.</figcaption>
</figure>

</section>

