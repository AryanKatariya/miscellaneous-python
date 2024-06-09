#!/usr/bin/python3

import argparse,subprocess as ss

def str_to_list(arg):
	return arg.split(",")

parser=argparse.ArgumentParser(description="This tool will give ip address for different subdomain")
parser.add_argument("-s",type=str_to_list,help="provide subdomain",required=False)
parser.add_argument("-d",type=str,help="provide domain name",required=True)
a=parser.parse_args()


for i in a.s:
	host=ss.getoutput("host -t a {}.{}".format(i,a.d))
	print(host)
