---
layout: single
permalink: /research-mgm/
title: "Research"
excerpt: "Computational fluid dynamics, scientific machine learning, and high-performance computing for flow simulation, estimation, and control."
---

<p class="eyebrow">Fluid mechanics · Scientific machine learning · High-performance computing</p>
<p class="lead">Physics and machine learning for flow simulation, estimation, and control.</p>

I develop computational methods for modeling, predicting, estimating, and controlling fluid flows. My research combines computational fluid dynamics, scientific machine learning, and high-performance computing, with experience spanning hybrid physics–ML simulation, resolvent-based estimation and control, and multi-fidelity turbulence simulation.

At Argonne National Laboratory, my work focuses on hybrid physics–ML methods for computational fluid dynamics. My doctoral research at the University of Michigan developed physics-based methods for flow estimation and control, following master’s research at RWTH Aachen on coupled turbulence simulation. Together, these experiences connect numerical-method development, fluid dynamics, and parallel scientific computing.

<p class="action-links"><a class="primary-link" href="#hybrid-physics-ml">Hybrid physics–ML simulation</a> · <a href="#flow-estimation-and-control">Flow estimation and control</a> · <a href="#multi-fidelity-simulation">Multi-fidelity turbulence simulation</a></p>

<section class="research-topic" markdown="1">

<h2 id="hybrid-physics-ml"><span class="research-index">01 / </span>Hybrid physics–ML simulation</h2>

My work combines physics-based flow simulation with machine learning to improve coarse-grid spectral-element computations. This research addresses the balance between predictive accuracy and computational cost in large-scale fluid simulation.

The framework integrates a learned component with a numerical flow solver. It brings together computational fluid dynamics and scientific machine learning within a framework designed for large-scale computing.

Within this broader hybrid physics–ML research program, physics-informed B-spline reconstruction (PI-BSR) combines flow data and physical information to reconstruct continuous flow fields. This work is useful for coarse-grid hybrid physics–ML simulation.

### Representative publications and conference contributions

**Jung, J.**, Lenz, D., Constantinescu, E., and Peterka, T. (2026). *Physics-Informed B-spline Reconstruction of Flow Data.* Computer Methods in Applied Mechanics and Engineering. [Published article](https://www.sciencedirect.com/science/article/pii/S0045782526007097).

**Jung, J.**, Constantinescu, E., Balin, R., and Lusch, B. (2026). *A hybrid physics–machine-learning framework for enhancing a coarse-grid spectral element solver for large-scale computing.* AIAA Aviation Forum, AIAA 2026-4474. [Paper](https://doi.org/10.2514/6.2026-4474)

**Jung, J.**, and Constantinescu, E. (2026). *Learning Differentiable Weak-Form Corrections to Accelerate Finite Element Simulations.* ASME FEDSM. [Paper (PDF)](https://arxiv.org/pdf/2601.20019).

**Jung, J.**, Constantinescu, E., and Balin, R. (2027). *Agent-Orchestrated Multi-Fidelity Workflow for Stable Hybrid Physics–Machine Learning Simulations.* AIAA SciTech Forum. **Forthcoming.**

</section>

<section class="research-topic" markdown="1">

<h2 id="flow-estimation-and-control"><span class="research-index">02 / </span>Flow estimation and control</h2>

My doctoral research uses the input–output dynamics of fluid flows to connect disturbances, measurements, and actuation. Resolvent-based models provide a physics-based foundation for estimating flow fields from limited measurements and designing feedback controllers.

### Estimation and control of an airfoil wake

My work on a laminar airfoil wake develops resolvent-based estimation and feedback control using surface sensors and actuators. It examines how a model of the flow dynamics can support the suppression of wake fluctuations and the modification of aerodynamic performance.

**Jung, J.**, Bhagwat, R., and Towne, A. (2025). *Resolvent-based estimation and control of a laminar airfoil wake.* Journal of Fluid Mechanics, 1016, A41. [Paper](https://doi.org/10.1017/jfm.2025.10423)

<figure class="research-figure control-comparison">
  <iframe src="https://www.youtube-nocookie.com/embed/1M5e0QN-EZA?autoplay=1&amp;mute=1&amp;playsinline=1&amp;rel=0" width="1920" height="840" title="Resolvent-based estimation and control of a laminar airfoil wake — Jung et al., JFM (2025)" aria-describedby="airfoil-control-caption" allow="autoplay; encrypted-media; picture-in-picture; fullscreen" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
  <figcaption id="airfoil-control-caption">Flow fields (left: streamwise velocity above, vorticity below) and lift and drag coefficients (right). Arrows mark when Controllers A and B are turned on. <a href="https://doi.org/10.1017/jfm.2025.10423">Jung, Bhagwat &amp; Towne (2025), Journal of Fluid Mechanics, 1016, A41</a>.</figcaption>
</figure>

<p class="project-links"><a href="https://www.youtube.com/watch?v=1M5e0QN-EZA">Watch on YouTube</a></p>

### Estimation of a turbulent wake

My work on turbulent-wake estimation combines flow measurements with resolvent-based models to estimate unmeasured flow fluctuations. This study extends the estimation methodology to a turbulent aerodynamic flow.

**Jung, J.**, and Towne, A. (2026). *Resolvent-based estimation of a turbulent wake.* Journal of Fluid Mechanics, 1033, A22. [Paper](https://doi.org/10.1017/jfm.2026.11444)

<figure class="research-figure turbulent-wake-3d">
  <iframe src="https://www.youtube-nocookie.com/embed/XYpTzq4BICA?autoplay=1&amp;mute=1&amp;playsinline=1&amp;rel=0" width="1920" height="660" title="Turbulent airfoil flow at Re = 23,000 — Jung and Towne, JFM (2026)" aria-describedby="turbulent-wake-3d-caption" allow="autoplay; encrypted-media; picture-in-picture; fullscreen" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
  <figcaption id="turbulent-wake-3d-caption">Three-dimensional large-eddy simulation (LES) of turbulent airfoil flow at Re = 23,000, showing roll-up, laminar–turbulent transition, and the turbulent wake. The simulation was performed using a U.S. Department of Defense (DoD) supercomputer. <a href="https://doi.org/10.1017/jfm.2026.11444">Jung &amp; Towne (2026), Journal of Fluid Mechanics, 1033, A22</a>.</figcaption>
</figure>

<p class="project-links"><a href="https://www.youtube.com/watch?v=XYpTzq4BICA">Watch on YouTube</a></p>

<figure class="research-figure turbulent-wake-video">
  <iframe src="https://www.youtube-nocookie.com/embed/dGAZGiX42DE?autoplay=1&amp;mute=1&amp;playsinline=1&amp;rel=0" width="1920" height="760" title="Resolvent-based estimation of a turbulent wake — Jung and Towne, JFM (2026)" aria-describedby="turbulent-wake-caption" allow="autoplay; encrypted-media; picture-in-picture; fullscreen" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
  <figcaption id="turbulent-wake-caption">Streamwise velocity fluctuations: LES and resolvent-based estimation using four sensors. Left: spanwise-averaged flow. Right: mid-span-plane flow. Red circles indicate sensor locations. <a href="https://doi.org/10.1017/jfm.2026.11444">Jung &amp; Towne (2026), Journal of Fluid Mechanics, 1033, A22</a>.</figcaption>
</figure>

<p class="project-links"><a href="https://www.youtube.com/watch?v=dGAZGiX42DE">Watch on YouTube</a></p>

### Methods for estimation, control, and resolvent analysis

Collaborative methodological work develops optimal estimation and control through the Wiener–Hopf formalism and efficient harmonic resolvent analysis through time stepping.

- Martini, E., **Jung, J.**, Cavalieri, A. V. G., Jordan, P., and Towne, A. (2022). *Resolvent-based tools for optimal estimation and control via the Wiener–Hopf formalism.* Journal of Fluid Mechanics, 937, A19. [Paper](https://doi.org/10.1017/jfm.2022.102)
- Farghadan, A., **Jung, J.**, Bhagwat, R., and Towne, A. (2024). *Efficient harmonic resolvent analysis via time stepping.* Theoretical and Computational Fluid Dynamics, 38, 331–353. [Paper](https://doi.org/10.1007/s00162-024-00694-1)

</section>

<section class="research-topic" markdown="1">

<h2 id="multi-fidelity-simulation"><span class="research-index">03 / </span>Multi-fidelity turbulence simulation</h2>

My master’s research developed a fully coupled zonal RANS–LES method for turbulent separated flows. I extended the coupling to overlapping meshes with different resolutions, implementing interpolation and parallel data exchange across zonal interfaces.

The method was studied using a turbulent flat-plate boundary layer and a launcher configuration with backward-facing-step separation. This work established my foundation in turbulence modeling, numerical coupling, and parallel simulation.

### Publicly available thesis

**Jung, J.** (2018). *Development of a fully coupled zonal RANS/LES method for the simulation of a turbulent backward-facing step flow.* Master’s thesis, RWTH Aachen University. Advisor: Wolfgang Schroeder. [Thesis record](https://doi.org/10.18154/RWTH-2020-07411)

<figure class="research-figure project-video">
  <iframe src="https://www.youtube-nocookie.com/embed/Ex097CDDPNU?autoplay=1&amp;mute=1&amp;playsinline=1&amp;rel=0" width="1596" height="1000" title="Zonal RANS/LES method for the simulation of a turbulent backward-facing step flow — Junoh Jung" aria-describedby="zonal-video-caption" allow="autoplay; encrypted-media; picture-in-picture; fullscreen" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
  <figcaption id="zonal-video-caption">Streamwise velocity <em>u</em> in the launcher-type backward-facing-step configuration. The animation shows an unsteady low-speed region downstream of the step. Simulation visualization from my master’s research. Junoh Jung, RWTH Aachen University (2018).</figcaption>
</figure>

<p class="project-links"><a href="https://www.youtube.com/watch?v=Ex097CDDPNU">Watch on YouTube</a></p>

</section>

<section class="research-topic" markdown="1">

<h2 id="scientific-computing">High-performance computing experience</h2>

My experience in high-performance computing supports the research directions above, connecting numerical-method development with parallel flow simulation and distributed machine learning. I work with C/C++, Python, Fortran, MPI, and GPU computing.

### Argonne National Laboratory

On Aurora at the Argonne Leadership Computing Facility (ALCF), I tested distributed differentiable training on up to 85 nodes with 1,020 MPI ranks, using 12 ranks per node (one per GPU tile). See the [Diff-NekRS paper](https://arxiv.org/abs/2609.23208). My development work includes Diff-NekRS for multi-timestep solver-in-the-loop training, hybrid physics–ML flow simulation, and differentiable weak-form corrections for finite-element solvers. As sole principal investigator, I received an ALCF Director’s Discretionary allocation of 45,000 node-hours over six months for differentiable hybrid physics–ML simulations.

### University of Michigan

My doctoral work used the University of Michigan’s Great Lakes cluster and U.S. Department of Defense (DoD) supercomputing resources for aerodynamic-flow simulation and resolvent-based estimation and control. I developed methods for estimating flow fields from sparse measurements and designing feedback controllers, with applications to laminar airfoil wakes and large-eddy simulation of turbulent airfoil flow.

### RWTH Aachen University

For my master’s research at RWTH Aachen, I ran the launcher-flow simulation on the Cray XC40 at the Stuttgart High Performance Computing Center, using 50 nodes with 24 CPU cores per node (1,200 cores total). See my [master’s thesis, Section 6.2](https://publications.rwth-aachen.de/record/794112/files/794112.pdf). My development work focused on parallel implementation in the Zonal Flow Solver for fully coupled RANS–LES simulation. I developed interpolation and parallel data exchange across overlapping meshes with different resolutions, and applied the method to turbulent boundary layers and a launcher-type backward-facing-step configuration.

### Extreme-scale computing training

In August 2023, I participated in the Argonne Training Program on Extreme-Scale Computing (ATPESC) as a selected participant. This U.S. Department of Energy–funded program complemented my research experience in high-performance scientific computing.

</section>
