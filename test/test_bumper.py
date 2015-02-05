import subprocess


def test_bump():
  subprocess.check_call(['bump', '-h'])
