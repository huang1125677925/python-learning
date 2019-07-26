#!/usr/bin/env bash
echo 'hhelo world'


awk '/^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-([0-9]{4})$/' log.txt