---
layout: page
title: Search Results
---

<!-- List where search results will be rendered -->
<ul id="search-results"></ul>

<script>
// Template to generate the JSON to search
window.store = {
{% for post in site.posts %}
"{{ post.url | slugify }}": {
"title": "{{ post.title | xml_escape }}",
"author": "{{ post.author | xml_escape }}",
"category": "{{ post.category | xml_escape }}",
"content": {{ post.content | strip_html | strip_newlines | jsonify }},
"url": "{{ post.url | xml_escape | relative_url }}"
}
{% unless forloop.last %},{% endunless %}
{% endfor %}
};
</script>

<!-- Import lunr.js from unpkg.com -->
<script src="{{site.baseurl}}/assets/javascripts/lunr/lunr.js"></script>
<script src="{{site.baseurl}}/assets/javascripts/lunr-languages/lunr.stemmer.support.js"></script>
<script src="{{site.baseurl}}/assets/javascripts/lunr-languages/lunr.multi.js"></script>
<script src="{{site.baseurl}}/assets/javascripts/lunr-languages/lunr.he.js"></script>
<!-- Custom search script which we will create below -->
<script src="{{site.baseurl}}/assets/javascripts/search.js"></script>