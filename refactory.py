#!/usr/bin/env python

"""
Script to automatically update the imports to
match pysystemtrade project structure and package tree
"""

import fnmatch
import os
import shutil
import stat

IMPORT_RULES = {
    'prefix': 'pysystemtrade.',
    'import_statement_search': [
        'sysdata.',
        'systems.',
        'syscore.',
        'syslogdiag.',
        'syssims.',
        'sysbrokers.',
    ],
    'replace': {
        'Config("systems.provided.example.exampleconfig.yaml")': 'Config("{{PREFIX}}.systems.provided.example.exampleconfig.yaml")',
        'DEFAULT_FILENAME = "systems.provided.defaults.yaml"': 'DEFAULT_FILENAME = "{{PREFIX}}.systems.provided.defaults.yaml"',
        'sysdata.tests.exampleconfig.yaml': '{{PREFIX}}.sysdata.tests.exampleconfig.yaml',
        'sysdata.legacycsv': '{{PREFIX}}.sysdata.legacycsv',
        'systems.provided.futures_chapter15.futuresconfig.yaml': '{{PREFIX}}.systems.provided.futures_chapter15.futuresconfig.yaml',
        'syscore.algos.robust_vol_calc': '{{PREFIX}}.syscore.algos.robust_vol_calc',
        'systems.provided.example.rules.ewmac_forecast_with_defaults': '{{PREFIX}}.systems.provided.example.rules.ewmac_forecast_with_defaults',
        'syscore.algos.forecast_scalar': '{{PREFIX}}.syscore.algos.forecast_scalar',
        'syscore.correlations.CorrelationEstimator': '{{PREFIX}}.syscore.correlations.CorrelationEstimator',
        'syscore.divmultipliers.diversification_multiplier_from_list': '{{PREFIX}}.syscore.divmultipliers.diversification_multiplier_from_list',
        'syscore.optimisation.GenericOptimiser': '{{PREFIX}}.syscore.optimisation.GenericOptimiser',
        'syscore.correlations.correlation_single_period': '{{PREFIX}}.syscore.correlations.correlation_single_period',
        'syscore.algos.mean_estimator': '{{PREFIX}}.syscore.algos.mean_estimator',
        'syscore.algos.vol_estimator': '{{PREFIX}}.syscore.algos.vol_estimator',
        'syscore.capital.fixed_capital': '{{PREFIX}}.syscore.capital.fixed_capital',
        'systems.provided.futures_chapter15.rules.ewmac': '{{PREFIX}}.systems.provided.futures_chapter15.rules.ewmac',
        'systems.provided.futures_chapter15.rules.carry': '{{PREFIX}}.systems.provided.futures_chapter15.rules.carry',

    }}


def find_replace(topdir, file_pattern, rules={}):
    for dirpath, dirs, files in os.walk(topdir, topdown=True):
        dirs[:] = [d for d in dirs if d != '.git']

        if isinstance(file_pattern, list):
            file_list = []
            for pattern in file_pattern:
                file_list += [os.path.join(dirpath, filename) for filename in fnmatch.filter(files, pattern)]

        else:
            file_list = [os.path.join(dirpath, filename) for filename in fnmatch.filter(files, file_pattern)]

        for file in file_list:
            with open(file, mode="r") as file_read:
                file_text = file_read.read()

            matched = False
            for find, replace in rules.items():
                if find in file_text:
                    matched = True

                file_text = file_text.replace(find, replace)

            if matched is True:
                os.remove(file)
                print("Writing Changes to {0}".format(file))

                with open(file, mode='w+') as file_write:
                    file_write.write(file_text)


def get_file_extension(file_name):
    return os.path.splitext(file_name)[1][1:]


def copytree(src, dst, symlinks=False, ignore=None):
    if not os.path.exists(dst):
        os.makedirs(dst)
        shutil.copystat(src, dst)
    lst = os.listdir(src)

    if ignore:

        file_list = []
        for file in lst:
            if any(ignore_name in file for ignore_name in ignore) or get_file_extension(
                    file) in ignore or file in ignore:
                continue

            file_list.append(file)

        lst = file_list

    for item in lst:
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if symlinks and os.path.islink(s):
            if os.path.lexists(d):
                os.remove(d)
            os.symlink(os.readlink(s), d)
            try:
                st = os.lstat(s)
                mode = stat.S_IMODE(st.st_mode)
                os.lchmod(d, mode)
            except:
                pass  # lchmod not available
        elif os.path.isdir(s):
            copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)


def refactor_import_statement(build=True, directory=None):
    match_pattern = 'from {prefix}{import_statement}'

    import_statements = IMPORT_RULES['import_statement_search']
    prefix = IMPORT_RULES['prefix']

    replacement_rules = {

    }

    for import_statement in import_statements:
        if build is True:
            replacement_rules[
                match_pattern.format(import_statement=import_statement, prefix="")] = match_pattern.format(
                import_statement=import_statement, prefix=prefix)
        else:
            replacement_rules[
                match_pattern.format(import_statement=import_statement, prefix=prefix)] = match_pattern.format(
                import_statement=import_statement, prefix="")

    for find, replace in IMPORT_RULES['replace'].items():
        prefix_replace = replace.replace("{{PREFIX}}", IMPORT_RULES['prefix']).replace(
            '..', '.')

        replacement_rules[find if build is True else prefix_replace] = prefix_replace if build is True else find

    find_replace(topdir=directory, file_pattern=['*.py', '*.yaml'], rules=replacement_rules)


if __name__ == "__main__":
    project_directory, _filename = os.path.split(os.path.abspath(__file__))
    pysystem_package_dir = os.path.join(project_directory, "pysystemtrade")

    print("Preparing Refactor")
    refactor_import_statement(build=True, directory=pysystem_package_dir)
    print("Refactor Complete")
