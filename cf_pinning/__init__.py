import os
import json
import re

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


def get_replacements(sections, section_name, pins=pinning):
    replacements = {}
    for dep in sections[section_name]:
        for name, versions in pins.items():
            version = versions[section_name]
            pin = '%s %s' % (name, version)
            dep_split = dep.split(' ', 1)
            actual_name = dep_split[0]
            actual_version = '' if len(dep_split) == 1 else dep_split[1]
            if actual_version == '*':
                continue
            if re.match(r'^\s*%s\s*' % name, actual_name) and dep != pin:
                        replacements['- ' + str(dep)] = '- ' + pin
    return replacements


def replace_strings(replacements, raw_text):
    for orig, new in replacements.items():
        raw_text = re.sub(
            # Use capture groups to get the indentation correct.
            # (|#.*) replaces (#.*)? to circumvent the "unmatched group" error
            # see: https://bugs.python.org/issue1519638
            r'(^\s*)%s(\s*)(|#.*)$' % re.escape(orig),
            r'\1%s\2\3' % new,
            raw_text,
            flags=re.MULTILINE
        )
        return raw_text
