.PHONY: server watch bundle clean

export PATH := ./node_modules/.bin:$(PATH)
export BROWSERIFY_OPTIONS := -o backend/static/bundle.js frontend/main.js

server:
	./server

watch: dist
	`which watchify` -v $$BROWSERIFY_OPTIONS

bundle:
	mkdir -p dist
	`which browserify` $$BROWSERIFY_OPTIONS

clean:
	find . -name "*.pyc" -print0 | xargs -0 rm || true
