/*jshint node: true, browser: true */
"use strict";

var $ = require("jquery");
window.jQuery = $; // shim required for pjax
require("pjax");

// `selector` identifies the respective form(s)
// `context` determines the scope of event delegation
module.exports = function(selector, context) {
	context = context.jquery ? context : $(context);

	context.on("submit", selector, function(ev) {
		$.pjax.submit(ev, selector, { fragment: selector });
	});

	var indicator;
	context.on("pjax:send", function(ev, xhr, options) {
		indicator = overlay(options.container);
	}).on("pjax:complete", function() {
		indicator.remove();
	});
};

// creates an overlay on top of the given `container`
function overlay(container) {
	var indicator = $('<div class="modal-backdrop fade in" />');
	var pos = container.offset();
	indicator.css({
		position: "absolute",
		top: pos.top,
		left: pos.left,
		width: container.width(),
		height: container.height()
	}).appendTo(container);
	return indicator;
}
