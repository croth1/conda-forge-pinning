import os
import json
import re

__version__ = '2017.2.18'

parent_dir = os.path.dirname(os.path.realpath(__file__))
pin_path = os.path.join(parent_dir, 'pinning.json')

with open(pin_path) as pin_handle:
    pinning = {}
    for pkg, pin in json.load(pin_handle).items():
        if isinstance(pin, list):
            build_pin, run_pin = pin
            pinning[pkg] = {'build': build_pin, 'run': run_pin}
        else:
            pinning[pkg] = {'build': pin, 'run': pin}
