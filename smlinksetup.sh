#!/bin/bash

create_smlink() {
  if [ -L "$HOME/$2$1" ]; then
    echo "Found Existing SmLink"
    rm -ir "$HOME/$2$1"
  elif [ -f "$HOME/$2$1" ]; then
    echo "Found Existing File"
    mv -i "$HOME/$2$1" "$HOME/$2$1.bak"
  elif [ -d "$HOME/$2$1" ]; then
    echo "Found Existing Directory"
    mvdir -i "$HOME/$2$1" "$HOME/$2$1_bak"
  else
    echo "No Exiting Files Found"
  fi
  ln -sr "./$1" "$HOME/$2$1"
}

while getopts 'npqz' OPTION; do
  case "$OPTION" in
    n)
      echo "Setup NVIM"
      create_smlink "nvim" ".config/"
      echo "SmLink Created NVIM"
      ;;
    p)
      echo "Setup PICOM"
      create_smlink "picom" ".config/"
      echo "SmLink Created PICOM"
      ;;
    q)
      echo "Setup QTILE"
      create_smlink "qtile" ".config/"
      echo "SmLink Created QTILE"
      ;;
    z)
      echo "Setup ZSH"
      create_smlink ".zshrc"
      echo "SmLink Created ZSH"
      ;;
    ?)
      echo "Usage $0 [-n for NVIM] [-p for PICOM] [-q for QTILE] [-z for ZSH]"
      exit 1
      ;;
  esac
done
shift "$(($OPTIND -1))"
