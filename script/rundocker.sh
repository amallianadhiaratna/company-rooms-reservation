#!/usr/bin/env bash
set -a && source docker.env && set +a
docker-compose build
docker-compose up