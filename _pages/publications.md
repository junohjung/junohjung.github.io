---
{"permalink": "/publications/", "title": "Publications"}
---
<p class="section-intro">Journal articles, conference proceedings, ongoing work, and theses. <a href="https://scholar.google.com/citations?user=CN8U92sAAAAJ">Google Scholar</a></p>

## Journal articles

{% assign papers = site.publications | where: 'group', 'published' | sort: 'year' | reverse %}
{% for paper in papers %}{% include publication-entry.html paper=paper %}{% endfor %}

## Conference proceedings

{% assign papers = site.publications | where: 'group', 'conference' | sort: 'order' %}
{% for paper in papers %}{% include publication-entry.html paper=paper %}{% endfor %}

## Under review & work in progress

<p class="section-intro">Publication status as of September 2026.</p>
{% assign papers = site.publications | where: 'group', 'ongoing' | sort: 'order' | reverse %}
{% for paper in papers %}{% include publication-entry.html paper=paper %}{% endfor %}

## Theses

<article class="publication" id="masters-thesis">
<div class="pub-year">2018</div>
<div>
<h3><a href="https://doi.org/10.18154/RWTH-2020-07411">Development of a fully coupled zonal RANS/LES method for the simulation of a turbulent backward-facing step flow</a></h3>
<p class="pub-authors">Junoh Jung</p>
<p class="pub-venue">Master’s thesis, Aerospace Engineering · RWTH Aachen University</p>
<p class="pub-links"><a href="https://publications.rwth-aachen.de/record/794112/files/794112.pdf">Thesis PDF</a><a href="/research/#zonal-rans-les">Project &amp; video</a></p>
</div>
</article>
