
from bs4 import BeautifulSoup
import sys
import itertools


def read_soup():
	with open(sys.argv[1], 'r') as infile:
		return infile.read()

soup = BeautifulSoup(read_soup())

#print(soup.prettify())


#def print_node_and_children(node):
#	if node.name is not None:
#		print(node.name)
#		for a in node.children:
#			print_node_and_children(a)
#
#print_node_and_children(soup)


#for child in soup.recursiveChildGenerator():
#	name = getattr(child, "name", None)
#	if name is not None:
#		print name
#	elif not child.isspace():  # leaf node, don't print spaces
#		print child
#	print("x")

def print_n_tabs(n):
	for _ in itertools.repeat(None, n):
		sys.stdout.write('    ')


def recursiveChildren(x, indent):
	if "childGenerator" in dir(x):

		for child in x.childGenerator():
			name = getattr(child, "name", None)
			if name is not None:
				print_n_tabs(indent)
				print (child.name)
				recursiveChildren(child, indent+1)
			else:
				if not child.isspace():  # Just to avoid printing "\n" parsed from document
					print_n_tabs(indent)
					print ('\"%s\"' % child)
	else:
		print ("no cg")

recursiveChildren(soup, 0)
