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
	make static
	pipenv lock -r  > requirements.txt
	git add -A
	git commit
	git push origin master

