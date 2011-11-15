import itertools
def git_description():
	import subprocess
	ps = subprocess.Popen(
	 ["git", "describe", "--always"],
	 stdout=subprocess.PIPE,
	 universal_newlines=True)
	(out, err) = ps.communicate()
	return out.strip()
def get_titanium_version():
	d=git_description()
	v='1.2.0'
	d=list(itertools.islice(itertools.chain((d[:-len(i)] for i in map("".join, itertools.product("-.:~",["win","w","osx","mac","linux","lin","l","unix","dar","os2","os2-"],["","32","64"])) if d.endswith(i)), [d]), 1))[0]
	return d if d.startswith(v) else v + ("" if len(d) == 0 or d[0] in ".-_~:" else ".") + d
