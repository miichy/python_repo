#!/usr/bin/env python
# -*- coding=utf-8 -*-
# function: find the context line and replace it
# author:miichy.liu
# 2015-09-10


def replace_op(ctx_key,ctx_value,file):
	lines = open(file).readlines()
	for  lnum,line in enumerate(lines):
		if line.find(ctx_key) >= 0:
			#line.replace(line,ctx_key+ctx_value)
			line = ctx_key+ctx_value
			print lnum,line

if __name__ == "__main__":
	replace_op("a","b","a.txt")
