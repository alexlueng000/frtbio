#!/bin/bash
source venv/bin/activate
exec celery -A tasks worker --loglevel=info