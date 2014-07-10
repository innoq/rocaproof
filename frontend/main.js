/*jshint node: true, browser: true */
"use strict";

var $ = require("jquery");
window.jQuery = $; // shim required for pjax
require("pjax");

var doc = $(document.body);

var selector = "form.pjax";
doc.on("submit", selector, function(ev) {
	$.pjax.submit(ev, selector, { fragment: selector });
});
var indicator = $('<div class="modal-backdrop fade in" />');
doc.on("pjax:send", function(ev, xhr, options) {
	var form = options.container;
	var pos = form.offset();
	indicator.css({
		position: "absolute",
		top: pos.top,
		left: pos.left,
		width: form.width(),
		height: form.height()
	}).appendTo(form);
}).on("pjax:complete", function() {
	indicator.detach(); // not strictly necessary
});

// XXX: DEBUG
var timer = 0;
var counter = $("<p>time since last full page refresh: <span /> s</p>").
	prependTo(doc).children().text(timer);
setInterval(function() {
	timer++;
	counter.text(timer);
}, 1000);
