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

My published work combines physics-based flow simulation with machine learning to improve coarse-grid spectral-element computations. This research addresses the balance between predictive accuracy and computational cost in large-scale fluid simulation.

The framework integrates a learned component with a numerical flow solver. It brings together computational fluid dynamics and scientific machine learning within a framework designed for large-scale computing.

### Representative publication

**Jung, J.**, Constantinescu, E., Balin, R., and Lusch, B. (2026). *A hybrid physics–machine-learning framework for enhancing a coarse-grid spectral element solver for large-scale computing.* AIAA Aviation Forum, AIAA 2026-4474. [Paper](https://doi.org/10.2514/6.2026-4474)

</section>

<section class="research-topic" markdown="1">

<h2 id="flow-estimation-and-control"><span class="research-index">02 / </span>Flow estimation and control</h2>

My doctoral research uses the input–output dynamics of fluid flows to connect disturbances, measurements, and actuation. Resolvent-based models provide a physics-based foundation for estimating flow fields from limited measurements and designing feedback controllers.

### Estimation and control of an airfoil wake

My work on a laminar airfoil wake develops resolvent-based estimation and feedback control using surface sensors and actuators. It examines how a model of the flow dynamics can support the suppression of wake fluctuations and the modification of aerodynamic performance.

**Jung, J.**, Bhagwat, R., and Towne, A. (2025). *Resolvent-based estimation and control of a laminar airfoil wake.* Journal of Fluid Mechanics, 1016, A41. [Paper](https://doi.org/10.1017/jfm.2025.10423)

### Estimation of a turbulent wake

My work on turbulent-wake estimation combines flow measurements with resolvent-based models to estimate unmeasured flow fluctuations. This study extends the estimation methodology to a turbulent aerodynamic flow.

**Jung, J.**, and Towne, A. (2026). *Resolvent-based estimation of a turbulent wake.* Journal of Fluid Mechanics, 1033, A22. [Paper](https://doi.org/10.1017/jfm.2026.11444)

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

</section>

<section class="research-topic" markdown="1">

<h2 id="scientific-computing"><span class="research-index">04 / </span>Scientific computing and research experience</h2>

My research experience spans numerical-method development, aerodynamic-flow analysis, and parallel scientific computing. I work with C/C++, Python, Fortran, MPI, and GPU computing, supported by experience on university, Department of Defense, and DOE computing systems.

| Research setting | Area of experience |
| --- | --- |
| **Argonne National Laboratory** | Hybrid physics–ML methods and high-performance computational fluid dynamics |
| **University of Michigan** | Resolvent-based flow estimation and control; aerodynamic flows and numerical simulation |
| **RWTH Aachen University** | Coupled RANS–LES methods, separated turbulent flows, and parallel implementation |

My teaching and mentoring experience includes supporting 101 students in introductory fluid mechanics at Michigan and participating as a mentor in Argonne GPU Hackathons. These activities complement my research in fluid mechanics and computational science.

</section>
