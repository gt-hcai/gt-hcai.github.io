---
title: "Highlights"
permalink: /highlights/
layout: single
---

This page presents the highlights from the HCAI community: events organized by its members, prizes, recruitments, funded projects, and more.
{: .page__lead}

{% assign rows = site.data.highlights | sort: "date" | reverse %}
{% assign years = rows | group_by_exp: "h", "h.date | slice: 0, 4" %}

{% for y in years %}
<h2 class="highlight-year">{{ y.name }}</h2>
<ul class="highlight-list">
  {% for h in y.items %}
  <li class="highlight-item">
    <time class="highlight-date" datetime="{{ h.date }}">{{ h.date | date: "%-d %B" }}</time>
    <div class="highlight-text">{{ h.description | markdownify }}</div>
  </li>
  {% endfor %}
</ul>
{% endfor %}
