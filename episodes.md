---
layout: default
title: פודקאסט השבוע במזרח התיכון
---

<h1>{{ page.title }}</h1>

{% for episode in site.data.episodes %}
<div class="episode">
  <h3>{{ episode.title }}</h3>
  <p><em>{{ episode.published }}</em></p>
  <audio controls>
    <source src="{{ episode.audio_url }}" type="audio/mpeg">
    הדפדפן שלך לא תומך בנגן אודיו.
  </audio>
  <p>{{ episode.description | truncatewords: 30 }}</p>
  <a href="{{ episode.link }}">לצפייה בפרק המלא</a>
</div>
<hr>
{% endfor %}