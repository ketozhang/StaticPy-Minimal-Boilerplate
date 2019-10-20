local:
	pipenv run python app.py

build:
	pipenv run python app.py build;

.PHONY: static
static:
	pipenv run python freeze.py

freeze:
	make static

clean:
	rm -rf docs/ ; \
	rm -rf docs.bak/ ; \
	rm -rf templates/*.bak ; \
	rm -rf templates/notes/ ; \
	rm -rf templates/posts/; \


publish:
	make static && \
	find demo/ -mindepth 1 \
		! \( -name ".*" -o -name "_*" \) -exec rm -r {} \; ;\
	rsync -a docs/ demo/ &&\
	rm -rf docs

push:
	git add demo &&\
	git commit -m "build demo" &&\
	git subtree push --prefix demo origin gh-pages

