from subprocess import Popen, PIPE

# update pip
cmd = Popen(["pip", "install", "--upgrade", "pip"], stdout=PIPE)
print(cmd.communicate(), "\n")

# get all outdated packages
cmd = Popen(["pip", "list", "--outdated"], stdout=PIPE)
packages: list = str(cmd.communicate()).split("\\n")[2:-1]
print("Needs update:\n", packages, "\n")

# update all packages
for itr in packages:
	itr = itr[:itr.index(" ")]
	cmd = Popen(["pip", "install", itr, "--upgrade"], stdout=PIPE)
	print(cmd.communicate(), "\n")

print("\n")
# list should be empty
cmd = Popen(["pip", "list", "--outdated"], stdout=PIPE)
print(cmd.communicate())