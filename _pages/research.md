---
layout: single
permalink: /research/
title: "Research"
excerpt: "Physics-based modeling, scientific machine learning, and high-performance computing for fluid-flow simulation, reconstruction, estimation, and control."
---

<p class="eyebrow">Fluid mechanics &amp; scientific machine learning</p>
<p class="lead">Integrating physics and machine learning to model, predict, and control fluid flows.</p>

I develop computational methods for accurate and efficient fluid-flow simulation, prediction, and control. My research combines physics-based modeling, scientific machine learning, and high-performance computing, with a focus on scalable, differentiable hybrid physics–machine-learning simulations.

My work spans three complementary directions: scalable and multi-fidelity flow simulation; physics-informed flow reconstruction; and flow estimation and control. Together, these directions address how to simulate flows efficiently, reconstruct flow fields from data, and use flow dynamics and measurements for estimation and control. Applications include separated flows, airfoil wakes, and turbulent jets.

<section class="research-topic" markdown="1">

<span id="differentiable-simulation" aria-hidden="true"></span>
<span id="scalable-multi-fidelity-flow-simulation" aria-hidden="true"></span>
<h2 id="differentiable-hybrid-physics-ML-simulation"><span class="research-index">01 / </span>Scalable and multi-fidelity flow simulation</h2>

<p class="research-question">How can physical models, learned corrections, and different levels of simulation fidelity be combined to predict fluid flows accurately at affordable computational cost?</p>

This research direction brings together hybrid turbulence simulation, differentiable physics–machine-learning models, and adaptive multi-fidelity workflows. The common goal is to improve the balance between computational cost and predictive accuracy while retaining governing-equation-based solvers.

### Differentiable hybrid physics–ML simulation

I develop hybrid physics–machine-learning methods that incorporate trainable corrections into spectral-element and finite-element flow simulations. The goal is to improve the accuracy of computationally affordable simulations while keeping the numerical solver at the center of the model.

**Differentiable spectral-element simulation.** My work on **Diff-NekRS** develops a scalable differentiable framework for multi-timestep solver-in-the-loop training. This direction connects learned corrections with the evolution of the numerical solution over multiple timesteps, with an emphasis on high-performance computing and large-scale flow simulation.

**Weak-form learning.** For finite-element simulations, I study differentiable weak-form corrections and structure-preserving neural variational correction operators. This work investigates how learned corrections can be incorporated into the variational formulation to accelerate simulations while retaining their numerical structure.

**Agent-orchestrated simulation workflows.** I investigate adaptive, multi-fidelity workflows for stable hybrid physics–machine-learning simulations. This workflow-level direction complements differentiable solver development and weak-form learning by coordinating numerical simulations and learned models, connecting hybrid-model development with practical use.

<div class="method-flow" role="img" aria-label="Conceptual workflow: PDE solver, then Solver-in-the-loop learning, then Corrected simulation">
  <span>PDE solver</span><b aria-hidden="true">→</b><span>Solver-in-the-loop learning</span><b aria-hidden="true">→</b><span>Corrected simulation</span>
</div>

<p class="diagram-note">Conceptual workflow: learned corrections remain coupled to the numerical solver.</p>

<div class="method-flow" role="img" aria-label="Conceptual simulation workflow: Multi-fidelity simulations, then Agent-orchestrated workflow, then Adaptive hybrid simulation">
  <span>Multi-fidelity simulations</span><b aria-hidden="true">→</b><span>Agent-orchestrated workflow</span><b aria-hidden="true">→</b><span>Adaptive hybrid simulation</span>
</div>

<p class="diagram-note">Workflow-level orchestration for stable, adaptive hybrid simulations.</p>

#### Representative work

[Diff-NekRS: A Scalable Differentiable Framework for Multi-Timestep Solver-in-the-Loop Training](/publications/#diff-nekrs-preprint-2026). arXiv preprint (2026).

[A hybrid physics–machine-learning framework for enhancing a coarse-grid spectral element solver for large-scale computing](/publications/#conference-2). AIAA Aviation Forum (2026; nominated for the best paper award).

[Learning Differentiable Weak-Form Corrections to Accelerate Finite Element Simulations](/publications/#conference-3). ASME FEDSM (2026).

[Agent-Orchestrated Multi-Fidelity Workflow for Stable Hybrid Physics–Machine Learning Simulations](/publications/#conference-1). AIAA SciTech Forum (2027; accepted, forthcoming).

Related manuscripts on differentiable spectral-element hybrid modeling, structure-preserving neural variational correction operators, and agent-orchestrated multi-fidelity workflows are in preparation. [Manuscripts in preparation](/publications/#manuscripts-in-preparation)

#### Research support

**ALCF Director’s Discretionary Allocation Program.** Sole principal investigator—45,000 node-hours over six months (2026), for *Differentiable Hybrid Physics Machine Learning Simulations*.

**Argonne Laboratory Directed Research and Development (LDRD).** Sole principal investigator—\$25,000, April–September 2026, for *Agent-Orchestrated Multi-Fidelity Workflow for Stable Hybrid Physics–Machine Learning Simulations*.


<section class="completed-project" aria-labelledby="zonal-rans-les" markdown="1">

<h3 id="zonal-rans-les">Fully coupled zonal RANS–LES for separated turbulent flows</h3>

<p class="project-meta"><span class="status">Foundational work · Completed · 2018</span> Master’s thesis · RWTH Aachen University · Research: 2017–2018</p>

This completed project provides an earlier example of combining different physical models and numerical resolutions for efficient flow simulation. It uses RANS–LES coupling rather than machine learning or differentiable training; its connection to my current work is the broader challenge of balancing simulation fidelity and computational cost.

<p class="research-question">How can we combine the efficiency of RANS with turbulence-resolving LES across different computational regions?</p>

#### Contribution

For my master’s thesis, I extended the Zonal Flow Solver’s fully coupled Reynolds-averaged Navier–Stokes (RANS) and large-eddy simulation (LES) approach to overlapping meshes with different resolutions. I developed interpolation and parallel data exchange across multiple zonal interfaces, enabling the two modeling approaches to work together within one simulation.

#### Results and significance

In a turbulent flat-plate boundary layer, the method agreed with reference data after an adjustment distance of approximately two incoming boundary-layer thicknesses. I then applied the implementation to a launcher configuration with backward-facing-step separation. The contribution addresses a practical challenge in turbulent-flow simulation: coupling regions with different mesh resolutions and turbulence treatments.

<figure class="research-figure project-video">
  <iframe src="https://www.youtube-nocookie.com/embed/Ex097CDDPNU?autoplay=1&amp;mute=1&amp;playsinline=1&amp;rel=0" width="1596" height="1000" title="Zonal RANS/LES method for the simulation of a turbulent backward-facing step flow — Junoh Jung" aria-describedby="zonal-video-caption" allow="autoplay; encrypted-media; picture-in-picture; fullscreen" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
  <figcaption id="zonal-video-caption">Streamwise velocity <em>u</em> in the launcher-type backward-facing-step configuration. The animation shows an unsteady low-speed region downstream of the step. Simulation visualization from my master’s research. Junoh Jung, RWTH Aachen University (2018); no audio.</figcaption>
</figure>

<p class="project-links">
  <a href="https://publications.rwth-aachen.de/record/794112/files/794112.pdf">Read the master’s thesis (PDF)</a>
  <a href="https://www.youtube.com/watch?v=Ex097CDDPNU">Watch on YouTube</a>
</p>

<p class="thesis-citation">Junoh Jung (2018). <em>Development of a fully coupled zonal RANS/LES method for the simulation of a turbulent backward-facing step flow.</em> Master’s thesis, RWTH Aachen University. Advisor: Wolfgang Schroeder. <a href="https://doi.org/10.18154/RWTH-2020-07411">Thesis record / DOI</a>.</p>

</section>
</section>

<section class="research-topic" markdown="1">

<span id="physics-informed-flow-reconstruction" aria-hidden="true"></span>
<h2 id="physics-integrated-learning"><span class="research-index">02 / </span>Physics-informed flow reconstruction</h2>

<p class="research-question">How can flow data and physical models be combined to reconstruct fluid fields?</p>

### Approach

**Physics-informed reconstruction.** I develop physics-informed B-spline methods that combine flow data with physical information to reconstruct fluid fields. This direction uses physical models to inform data reconstruction, complementing the solver-level corrections described above.

<div class="method-flow" role="img" aria-label="Conceptual reconstruction workflow: Flow data and physics, then Physics-informed B-splines, then Reconstructed flow fields">
  <span>Flow data &amp; physics</span><b aria-hidden="true">→</b><span>Physics-informed B-splines</span><b aria-hidden="true">→</b><span>Reconstructed flow fields</span>
</div>

<p class="diagram-note">Physics-informed flow-data reconstruction.</p>

### Representative work

[Physics-Informed B-spline Reconstruction of Flow Data](/publications/#pibsr-2026). *Computer Methods in Applied Mechanics and Engineering* (accepted, 2026).

</section>

<section class="research-topic" markdown="1">

<h2 id="flow-estimation-and-control"><span class="research-index">03 / </span>Flow estimation and control</h2>

<p class="research-question">How can we estimate and control aerodynamic flows using models of their input–output dynamics?</p>

### Approach

I develop resolvent-based methods that use the input–output dynamics of fluid flows to connect measurements, disturbances, and actuation. My research spans Wiener–Hopf formulations for optimal estimation and control, efficient harmonic resolvent analysis via time stepping, and applications to laminar airfoil wakes and turbulent wakes.

Collaborative work extends these methods to the estimation and control of wavepackets in turbulent and supersonic jets. Across these applications, the aim is to connect flow measurements with physics-based models for estimation and control.

<div class="method-flow" role="img" aria-label="Conceptual workflow: Flow measurements, then Resolvent-based estimator, then Estimation and control">
  <span>Flow measurements</span><b aria-hidden="true">→</b><span>Resolvent-based estimator</span><b aria-hidden="true">→</b><span>Estimation &amp; control</span>
</div>

<p class="diagram-note">Conceptual workflow.</p>

### Representative work

[Resolvent-based estimation of a turbulent wake](https://doi.org/10.1017/jfm.2026.11444). *Journal of Fluid Mechanics*, 1033, A22 (2026).

[Resolvent-based estimation and control of a laminar airfoil wake](https://doi.org/10.1017/jfm.2025.10423). *Journal of Fluid Mechanics*, 1016, A41 (2025; nominated for the JFM Emerging Scholar Best Paper Prize).

Related methodological contributions include [Efficient harmonic resolvent analysis via time stepping](https://doi.org/10.1007/s00162-024-00694-1), *Theoretical and Computational Fluid Dynamics* (2024), and [Resolvent-based tools for optimal estimation and control via the Wiener–Hopf formalism](https://doi.org/10.1017/jfm.2022.102), *Journal of Fluid Mechanics* (2022).

Collaborative contributions include [Towards resolvent-based estimation and control of wavepackets in supersonic turbulent jets](/publications/#conference-4), AIAA SciTech Forum (2026), and [Resolvent-based estimation of wavepackets in turbulent jets](/publications/#conference-5), AIAA/CEAS (2024).

<h3 id="laminar-airfoil-control">Laminar airfoil control · JFM 2025</h3>

Four surface sensors and four actuators suppress unsteady wake fluctuations using nested resolvent-based controllers. Controller A is designed around the original mean flow; Controller B accounts for the mean flow modified by Controller A.

<figure class="research-figure control-comparison">
  <video controls controlslist="nodownload" autoplay muted playsinline preload="metadata" width="1920" height="1080" poster="/images/jfm2025-airfoil-control-poster.jpg?v=short-credit" aria-label="Synchronized airfoil flow visualization and lift and drag response" aria-describedby="airfoil-control-caption">
    <source src="/videos/jfm2025-airfoil-control-comparison.mp4?v=short-credit" type="video/mp4">
    Your browser does not support embedded video.
  </video>
  <figcaption id="airfoil-control-caption">Synchronized flow visualization (left: streamwise velocity above, vorticity below) and lift and drag coefficients (right). Arrows mark when Controllers A and B are turned on. The two source animations play together in one video; no audio. <a href="https://doi.org/10.1017/jfm.2025.10423">Jung, Bhagwat &amp; Towne (2025), Journal of Fluid Mechanics, 1016, A41</a>.</figcaption>
</figure>

With both controllers active, the study reports approximately **143% higher mean lift** and **98% less velocity-fluctuation energy at the control target** relative to the uncontrolled flow. Mean drag remains largely unchanged.

### Turbulent wake estimation · JFM 2026

<figure class="research-figure">
  <a href="/images/jfm-2026-figure16.png"><img src="/images/jfm-2026-figure16.png" width="3821" height="3040" loading="lazy" alt="LES reference fields and resolvent-based estimates of streamwise velocity fluctuations in an airfoil wake at three times, shown as spanwise averages and on the mid-span plane."></a>
  <figcaption>Streamwise velocity fluctuations in a turbulent airfoil wake: large-eddy simulation (LES) compared with estimates from four sensors at three times. <a href="https://doi.org/10.1017/jfm.2026.11444">Jung &amp; Towne (2026), Figure 16</a>, <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>. Reproduced without alteration. Select the figure to view at full resolution.</figcaption>
</figure>

</section>

[Full publication list](/publications/) · [Talks and presentations](/teaching-talks/)
