import argparse
import re
import subprocess


def main(args):
	handle_out = subprocess.check_output(['handle.exe', r'Preferences\undo.cfg'])

	for line in handle_out.split('\n'):
		match = re.match(
			r'{} .*pid: (?P<procid>\d+).* File \s+(?P<handle>[A-F0-9]+):'.format(args.process), 
			line)
		if not match:
			continue
		groups = match.groupdict()
		print 'killing handle {} from procid {}'.format(groups['handle'], groups['procid'])
		subprocess.check_call(['handle.exe', '-c', groups['handle'], '-p', groups['procid'], '-y'])
		return
	print "Couldn't find the handle {} in {}, exiting".format(args.file, args.process)
	

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--process', 
		help='Kill the handle of this process', default='CefSubprocess.exe')
	parser.add_argument('--file', 
		help='Part of the path of the file handle to kill', default=r'Preferences\undo.cfg')
	args = parser.parse_args()
	main(args)