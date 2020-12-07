#!/usr/bin/env bash

inotify-hookable -q -w ./ -C "\.py$=""clear && python $1"""
