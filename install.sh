#!/usr/bin/env bash
# This Programm Write by Mr.nope
# K-Tool v1.4.0

if [[ "$(id -u)" -ne 0 ]]; then
  echo "
  Please, Run This Programm as Root!"
  exit 1
fi
function main() {
  printf '\033]2;K-Tool/Installing\a'
  clear
  echo "Installing..."
  chmod +x ktool.py
  apt install python
  apt install python3
  apt install python3-pip
  pip3 install --upgrade pip
  echo ""
  echo "Finish...!"
  echo ""
  exit 1
}
main