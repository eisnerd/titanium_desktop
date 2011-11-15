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
	return d if d.startswith(v) else v + ("" if len(d) == 0 or d[0] in ".-_~:" else ".") + d
