#!/usr/bin/python
import argparse
import os
import sys
from interactive_cmd import InteractiveCMD
from command_controler import CommandControler
from gpg_tools import GPGTools

FILE = 'secrets'

class Main:

	def main(argv):
		gpg = GPGTools(file=FILE)
		icmd = InteractiveCMD(gpg)
		cmdc = CommandControler(gpg)
		if os.path.isfile(FILE):
			parser = argparse.ArgumentParser(description='Manager for sensible information under PGP')
			parser.add_argument('-i','--interactive', help='display the interactive menu for pwd-manager',
				action='store_true')
			parser.add_argument('-l','--list', help='list all the stored identifiers', action='store_true')
			parser.add_argument('-u','--user', metavar='identifier', help='return the username for the given identifier')
			parser.add_argument('-p','--password', metavar='identifier', help='return the password for the given identifier')
			parser.add_argument('-ur','--url', metavar='identifier', help='return the URL for the given identifier')
			parser.add_argument('-o','--other', metavar='identifier', help='return the other for the given identifier')
			parser.add_argument('-a','--all', metavar='identifier', help='display all values for the given identifier')
			parser.add_argument('-ak','--addkey', nargs = 2, metavar=('identifier', '{"user":"<user>", ...}') , help='add element to secrets, second argument must be a valid json string. Allowed keys user, password, url and other')
			parser.add_argument('-mk','--modkey', nargs = 2, metavar=('identifier', '{"user":"<new_user>", ...}') , help='modify element to secrets, second argument must be a valid json string. Allowed keys user, password, url and other')
			parser.add_argument('-mi','--modid', nargs = 2, metavar=('old_identifier','new_identifier'), help='modify id from an element')
			parser.add_argument('-d','--delete', nargs = 1, metavar='identifier', help='modify element to secrets, second argument must be a valid json string')
			args = parser.parse_args()
			if args.interactive: icmd.interactive_menu()
			elif args.list: cmdc.show_keys()
			elif args.user: cmdc.get_key_value(args.user, 'user')
			elif args.password: cmdc.get_key_value(args.password, 'pass')
			elif args.url: cmdc.get_key_value(args.url, 'url')
			elif args.other: cmdc.get_key_value(args.other, 'other')
			elif args.all: cmdc.get_key_value(args.all, 'all')
			elif args.addkey: cmdc.add_content_id_json(args.addkey[0], str(args.addkey[1:][0]))
			elif args.modkey: cmdc.modify_content(args.modkey[0], str(args.modkey[1:][0]))
			elif args.modid: cmdc.modify_id(args.modid[0], args.modid[1])
			elif args.delete: cmdc.del_id(args.delete[0])
			else: parser.print_help()
		else:
			parser = argparse.ArgumentParser(description='''Manager for sensible information under PGP. Use -i/--interactive
				or -ak/--addkey to introduce your first key and for more option will be displayed.''')
			parser.add_argument('-i','--interactive', help='display the interactive menu for pwd-manager',
				action='store_true')
			parser.add_argument('-ak','--addkey', nargs = 2, metavar=('identifier', '{"user":"<user>", ...}') , help='add element to secrets, second argument must be a valid json string. Allowed keys user, password, url and other')
			args = parser.parse_args()
			if args.interactive: icmd.interactive_menu()
			elif args.addkey: cmdc.add_content_id_json(args.addkey[0], str(args.addkey[1:][0]))
			else: parser.print_help()

if __name__ == '__main__':
	m = Main();
	m.main()
