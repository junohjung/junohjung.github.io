---
layout: single
permalink: /research-mgm/
title: "Research"
excerpt: "Scalable hybrid physics–machine learning for reliable prediction and control, with proposed research on transient heat transport for data-center cooling."
---

<!-- MGM-focused research page, prepared from Fellowship_Proposal_2026_Jung.pdf.
     The separate permalink allows this page to coexist with /research/.
     This file uses the existing single layout and requires no new image assets. -->

<p class="eyebrow">Fluid mechanics &amp; heat transport · Scientific machine learning · High-performance computing</p>
<p class="lead">Scalable hybrid physics–machine learning for reliable prediction and control.</p>

I develop computational methods that connect physics-based simulation, machine learning, and flow estimation and control. My research addresses the information that affordable models and limited measurements leave unresolved: which physical processes and internal states are needed to predict how a system responds to a change in its inputs?

My proposed Maria Goeppert Mayer Fellowship research brings this question to **transient heat transport for data-center cooling**. I aim to determine what a computationally affordable model must retain to predict how much, and how quickly, changing coolant flow cools a hotspot. This direction connects my background in multi-fidelity turbulence simulation and resolvent-based estimation and control with my current work on differentiable hybrid physics–ML frameworks at Argonne National Laboratory.

<p class="action-links"><a class="primary-link" href="#proposed-fellowship-research">Proposed fellowship research</a> · <a href="#hybrid-physics-ml-foundation">Current research foundation</a> · <a href="#research-preparation">Preparation and leadership</a></p>

<section class="research-topic" markdown="1">

<h2 id="proposed-fellowship-research"><span class="research-index">01 / </span>Predicting cooling responses in data centers</h2>

<p class="project-meta"><span class="status">Proposed MGM fellowship research</span></p>

**Scalable and Differentiable Hybrid Physics–Machine Learning Modeling of Transient Heat Transport for Reliable Data Center Cooling**

<p class="research-question">What thermal information must a lower-cost model retain to predict the magnitude and timing of a hotspot’s response to a coolant-flow adjustment?</p>

A model can reproduce a hotspot’s baseline temperature while mispredicting its response to a change in cooling. I hypothesize that unresolved heat exchange near channel walls and missing information about heat stored within the metal can explain these response errors. The proposed research will identify when each mechanism matters, develop corrections where needed, and test whether better predictions improve cooling decisions.

The study will progress from a heated channel to multichannel cold plates. The physical models will couple coolant flow, heat transport in the water, and conduction and heat storage in the metal. High-resolution simulations will provide reference data for evaluating lower-cost models.

### Aim 1 — Identify the thermal information needed for cooling decisions

I will use targeted wall refinement, additional solid-temperature states, and controlled heating histories to distinguish heat-exchange errors from missing heat-storage information. Physical and flow-conditioned linear models will establish when learning adds value. More complex or history-dependent corrections will be introduced where the evidence justifies them.

An **offline experiment-selection agent** will choose informative flow changes, simulation fidelity, and observation periods. It will select numerical experiments; pump commands will remain the responsibility of a separate predictive controller. The initial experiment-selection approach requires no large language model, and its value will be compared with fixed and uncertainty-based selection at equal cost.

### Aim 2 — Learn corrections that preserve cooling responses

I will extend **Diff-NekRS** to differentiate through transient thermal simulations and water–metal heat exchange. The objective is to learn energy-conserving heat-transfer corrections that reproduce both temperature histories and their response to a flow adjustment.

Paired numerical experiments will compare two flow-command histories under the same heating, initial states, and prior history. Their temperature differences will reveal the magnitude and timing of the cooling response. Temperature-only and response-aware learning will use identical data and budgets. Thermal-gradient verification and tests of distributed training will precede scale-up to larger plates and longer histories.

### Aim 3 — Test whether better predictions improve hotspot management

A standard predictive controller will use each fixed model to adjust a single total-flow input. Independent high-resolution simulations will provide feedback for the numerical control tests. All prediction models will be compared using the same controller, observations, and actuator limits.

The evaluation will measure pumping energy at matched temperature limits and hotspot temperatures at matched energy budgets, accounting for final stored heat or full thermal recovery. Physical validation will depend on access to suitable transient measurements or an existing test loop and will be reported separately from numerical verification.

### Expected contribution

The intended outcome is a tested connection between **missing thermal information, model correction, and cooling performance**, together with reusable models and benchmarks. The three-year progression is to establish verified baselines and identify response errors, develop and compare learned corrections, and evaluate cooling decisions and computational scaling. This would provide a foundation for future cooling digital twins and thermal-management research.

</section>

<section class="research-topic" markdown="1">

<h2 id="hybrid-physics-ml-foundation"><span class="research-index">02 / </span>Hybrid physics–ML research foundation</h2>

<p class="research-question">How can governing equations and data improve the physical information retained by computationally affordable models?</p>

My current research combines physical models with data-driven approximation in numerical solvers and continuous field reconstruction. These complementary methods provide the computational and methodological foundation for the proposed thermal-transport research.

### Differentiable simulation and solver-in-the-loop learning

**Diff-NekRS** is a scalable differentiable framework for multi-timestep solver-in-the-loop training. It connects neural corrections with the evolution of the numerical solution, combining a physics-based flow solver with derivatives needed for training. My distributed differentiable training work has been tested at up to **1,020 MPI ranks on Aurora**. Extending this capability to coupled thermal dynamics is part of the proposed fellowship research.

My related work on **weak-form learning** investigates differentiable corrections within finite-element formulations. Together, these efforts address how learned components can improve affordable simulations while retaining the structure of the underlying numerical methods.

### Physics-informed reconstruction: PI-BSR

**Physics-informed B-spline reconstruction (PI-BSR)** is the reconstruction component of my broader hybrid physics–ML research program. It fits continuous B-spline fields using flow data together with governing-equation residuals and conservation-balance information. This spline-based approach to physics–data integration complements neural corrections embedded in numerical solvers.

The work began during my 2023 Argonne Givens Associateship and has been accepted by *Computer Methods in Applied Mechanics and Engineering*. It provides experience in combining physical information with data to improve continuous flow representations.

### Adaptive multi-fidelity workflows

I also investigate agent-orchestrated workflows that coordinate numerical simulations and learned models for stable hybrid physics–ML simulation. This work provides a foundation for the fellowship’s proposed offline selection of informative numerical experiments.

</section>

<section class="research-topic" markdown="1">

<h2 id="research-preparation"><span class="research-index">03 / </span>From unresolved flow physics to reliable control</h2>

My training brings together the physical, numerical, and computational perspectives needed to connect model fidelity with prediction and control.

| Research background | Established experience | Connection to the proposed research |
| --- | --- | --- |
| **RWTH Aachen — M.S. in Aerospace Engineering** | Fully coupled zonal RANS–LES for separated turbulent flows; interpolation and parallel exchange across meshes with different resolutions | Combining model fidelities and identifying where additional physical resolution is needed |
| **University of Michigan — Ph.D. in Mechanical Engineering** | Resolvent-based estimation and control of aerodynamic flows; causal estimation and input–output dynamics | Inferring unobserved states and evaluating the dynamics needed to predict responses to actuation |
| **Argonne — Postdoctoral research** | Differentiable spectral-element and finite-element modeling, hybrid physics–ML methods, and distributed training | Developing and verifying learned corrections within scalable physical simulations |

My first-author *Journal of Fluid Mechanics* studies on laminar airfoil wakes and turbulent wakes establish the estimation-and-control foundation. The fellowship would extend this background through a focused investigation of transient thermal transport, complemented by proposed collaboration in heat-transfer verification.

### Independent research and leadership

- **Argonne LDRD, 2026:** Sole principal investigator of a \$25,000 project on agent-orchestrated multi-fidelity simulation.
- **ALCF Director’s Discretionary program, 2026:** Principal investigator of a project awarded 45,000 node-hours for differentiable hybrid physics–ML simulations.
- **Teaching and mentoring:** Supported 101 students in introductory fluid mechanics at Michigan and participated as a mentor in Argonne GPU Hackathons.

These experiences support my ability to define research questions, organize computational campaigns, and lead method development. The fellowship would establish a distinct direction centered on thermal information, cooling-response prediction, and the consequences of model errors for control.

</section>

<section class="research-topic" markdown="1">

<h2 id="argonne-research-vision"><span class="research-index">04 / </span>A research program at Argonne</h2>

My long-term goal is to build an independent research program in a DOE national laboratory, developing scalable hybrid physics–ML methods for reliable prediction and control of complex physical systems.

The proposed work connects **AI for Science** with **transient thermal management of AI/HPC systems**, drawing on applied mathematics and computational science and offering relevance to microelectronics. I plan to combine my existing experience with Aurora and distributed training with proposed collaborations in numerical methods, scientific machine learning, and thermal verification. Pilot studies would guide future computing-allocation requests and the progression to larger simulations.

The research aims to produce physical understanding, verified numerical methods, and reusable benchmarks. Its broader direction is to determine which unresolved transport processes and unobserved states a model must retain for its predictions to support reliable decisions.

</section>

<section class="research-topic" markdown="1">

<h2 id="selected-work">Selected research supporting this direction</h2>

- **Diff-NekRS: A Scalable Differentiable Framework for Multi-Timestep Solver-in-the-Loop Training.** Jung, Balin, Lusch, and Constantinescu. arXiv preprint, 2026. [Publication details](/publications/#diff-nekrs-preprint-2026)
- **Physics-Informed B-spline Reconstruction of Flow Data.** Jung, Lenz, Constantinescu, and Peterka. *Computer Methods in Applied Mechanics and Engineering*, accepted, 2026. [Publication details](/publications/#pibsr-2026)
- **Resolvent-based estimation of a turbulent wake.** Jung and Towne. *Journal of Fluid Mechanics*, 1033, A22, 2026. [Publication details](/publications/#turbulent-wake-2026)
- **Resolvent-based estimation and control of a laminar airfoil wake.** Jung, Bhagwat, and Towne. *Journal of Fluid Mechanics*, 1016, A41, 2025. [Publication details](/publications/#laminar-airfoil-wake-2025)

[Full publication list](/publications/) · [Curriculum vitae](/cv/) · [Teaching and talks](/teaching-talks/)

</section>
