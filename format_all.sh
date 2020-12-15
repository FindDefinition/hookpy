isort -rc --atomic . && \
yapf -i --recursive -vv ./hookpy ./test
yapf -i -vv setup.py