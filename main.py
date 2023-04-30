#!/bin/python3
import subprocess

def restart_dash_to_dock():
    subprocess.run(["gnome-extensions", "disable", "dash-to-dock@micxgx.gmail.com"])
    subprocess.run(["gnome-extensions", "enable", "dash-to-dock@micxgx.gmail.com"])

if __name__ == "__main__":
    restart_dash_to_dock()