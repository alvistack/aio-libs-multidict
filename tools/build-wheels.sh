#!/bin/bash
PYTHON_VERSIONS="cp34-cp34m cp35-cp35m cp36-cp36m"

# Avoid creation of __pycache__/*.py[c|o]
export PYTHONDONTWRITEBYTECODE=1

package_name="$1"
if [ -z "$package_name" ]
then
    &>2 echo "Please pass package name as a first argument of this script ($0)"
    exit 1
fi

echo "Compile wheels"
for PYTHON in ${PYTHON_VERSIONS}; do
    /opt/python/${PYTHON}/bin/pip install -r /io/requirements-wheel.txt
    /opt/python/${PYTHON}/bin/pip wheel /io/ -w /io/dist/
done

echo "Bundle external shared libraries into the wheels"
for whl in /io/dist/${package_name}*.whl; do
    auditwheel repair "$whl" -w /io/dist/
done

echo "Install packages and test"
for PYTHON in ${PYTHON_VERSIONS}; do
    /opt/python/${PYTHON}/bin/pip install "$package_name" --no-index -f file:///io/dist
    /opt/python/${PYTHON}/bin/py.test /io/tests
done