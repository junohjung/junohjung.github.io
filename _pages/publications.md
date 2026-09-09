---
{"permalink": "/publications/", "title": "Publications"}
---
<p class="section-intro">Journal articles and conference proceedings, followed by ongoing work. <a href="https://scholar.google.com/citations?user=CN8U92sAAAAJ">Google Scholar</a></p>

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

