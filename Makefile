publish:
	rm -fr build dist .egg create_django_skeleton.egg-info
	pip3 install 'twine>=1.5.0'
	python3 setup.py sdist bdist_wheel
	twine upload dist/*
	rm -fr build dist .egg create_django_skeleton.egg-info
