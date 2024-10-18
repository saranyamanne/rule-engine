#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  examples/csv_filter.py
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are
#  met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following disclaimer
#    in the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of the project nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
#  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
#  A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
#  OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#  SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
#  LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
#  DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
#  THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#  OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

import argparse
import csv
import functools
import os
import sys

get_path = functools.partial(os.path.join, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(get_path('lib'))

import rule_engine

DESCRIPTION = """\
Apply a rule to the specified CSV file. The first row of the CSV file must be
the field names which will be used as the symbols for the rule.
"""

# specify a custom resolve function that checks if the symbol is a column name
# in the csv file and if not replaces underscores with spaces
def resolve_item(thing, name):
	if not name in thing:
		name = name.replace('_', ' ')
	return rule_engine.resolve_item(thing, name)

def main():
	parser = argparse.ArgumentParser(
		conflict_handler='resolve',
		description=DESCRIPTION,
		formatter_class=argparse.RawDescriptionHelpFormatter
	)
	parser.add_argument('csv_file', type=argparse.FileType('r'), help='the CSV file to filter')
	parser.add_argument('rule', help='the rule to apply')
	arguments = parser.parse_args()

	# need to define a custom context to use a custom resolver function
	context = rule_engine.Context(resolver=resolve_item)
	try:
		rule = rule_engine.Rule(arguments.rule, context=context)
	except rule_engine.RuleSyntaxError as error:
		print(error.message)
		return 0

	csv_reader = csv.DictReader(arguments.csv_file)
	csv_writer = csv.DictWriter(sys.stdout, csv_reader.fieldnames, dialect=csv_reader.dialect)
	for row in rule.filter(csv_reader):
		csv_writer.writerow(row)
	return 0

if __name__ == '__main__':
	sys.exit(main())
