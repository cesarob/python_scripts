#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

from optparse import OptionParser
import os
import sys

def get_files(dir,ext):
	"""
	It returns from a directory the list of files matching an extension.
	"""
	result = []
	ext = ext.lower()
	contents = os.listdir(dir)
	for filename in contents:
		fullpath = os.path.join(dir, filename)
		pos = filename.lower().rfind('.' + ext)
		if os.path.isfile(fullpath) and pos != -1:
			result.append(filename)

	return result

def remove_extensions(list):
	"""
	From a list of filenames generates the same list of filenames without extensions
	"""
	result = []
	for filename in list:
		pos = filename.rfind('.')
		result.append(filename[:pos])
	
	return result


def process(jpg_dir, raw_dir):
	"""
	Removes from the raw dir the files that doesn't math the jpg file.
	"""
	jpg_files = get_files(jpg_dir, 'jpg')
	raw_files = get_files(raw_dir, 'nef')
	jpg_matches = remove_extensions(jpg_files)
	raw_matches = remove_extensions(raw_files)

	# We can start to process the files...
	for i in range(len(raw_matches)):
		candidate = raw_matches[i]
		if not candidate in jpg_matches:
			print "removing " + raw_files[i].lower()
			os.remove(os.path.join(raw_dir, raw_files[i]))


def error(msg):
	sys.stderr.write("Error: " + msg + "\n")
	sys.exit(1)
	


if ( __name__  == "__main__") :		
	sUsage =  """
	%prog <dir jpg files> <dir raw files>
	Clean raw directory bases in the information of the jpg files.
	Only support extensions: jpg and nef.
	"""	
	parser = OptionParser(usage=sUsage)	 	
	(options,args) = parser.parse_args()
	if len(args) != 2: 			
		error("Wrong number of arguments")

	jpg_dir = args[0]
	raw_dir = args[1]

	if os.path.exists(jpg_dir) and os.path.exists(raw_dir) and \
		os.path.isdir(jpg_dir) and os.path.isdir(raw_dir):
		process(jpg_dir, raw_dir)
	else:
		error("Invalid directories in the arguments")

	
		

