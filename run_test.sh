#!/bin/bash

docker run -v $(pwd):/sources -w /sources -t python_dev pytest
