#!/usr/bin/env bash

inotify-hookable -q -w ./ -C "\.py$=$1"
