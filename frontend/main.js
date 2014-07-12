/*jshint node: true, browser: true */
"use strict";

var $ = require("jquery");
var qforms = require("./quick_forms");

qforms("form.pjax", document.body);

// XXX: DEBUG
var timer = 0;
var counter = $("<p>time since last full page refresh: <span /> s</p>").
	prependTo(document.body).children().text(timer);
setInterval(function() {
	timer++;
	counter.text(timer);
}, 1000);
