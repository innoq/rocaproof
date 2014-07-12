/*jshint node: true, browser: true */
"use strict";

var $ = require("jquery");
window.jQuery = $; // shim required for pjax
require("pjax");

// `formSelector` identifies the respective form(s)
// `context` determines the scope of event delegation
// `containerSelector` optionally identifies the container element to be
// replaced, defaulting to `formSelector`
module.exports = function(formSelector, context, containerSelector) {
	context = context.jquery ? context : $(context);
	containerSelector = containerSelector || formSelector;

	context.on("submit", formSelector, function(ev) {
		$.pjax.submit(ev, containerSelector, { fragment: containerSelector });
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
