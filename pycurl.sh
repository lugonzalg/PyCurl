#!/bin/bash

if [[ "$1" = "run" ]]; then
    docker run -it -v ${PWD}/src/:/tmp pycurl_enviroment /bin/bash
fi
