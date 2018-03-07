{% load json_util %}
{% spaceless %}
{% comment %}
https://support.siteimprove.com/hc/en-gb/articles/206343703-Adding-Siteimprove-Analytics-JavaScript-to-your-website
{% endcomment %}
{% if siteimprove_code %}
(function() {
    var sz = document.createElement('script');
    sz.type = 'text/javascript';
    sz.async = true;
    sz.src = '//siteimproveanalytics.com/js/siteanalyze_' + {{ siteimprove_code|json_encode|safe }} + '.js';
    var s = document.getElementsByTagName('script')[0];
    s.parentNode.insertBefore(sz, s);
})();
{% endif %}
{% endspaceless %}
