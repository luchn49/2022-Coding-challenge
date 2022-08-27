#!/bin/bash
gunicorn -w 10 -b 0.0.0.0:8001 -t 300 app:app \
--access-logfile=- \
--log-level debug \
--capture-output \
--error-logfile=-
