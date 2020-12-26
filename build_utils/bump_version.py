import re
import sys

if __name__ == "__main__":

    version_file = sys.argv[1]

    print("Getting version from file: %s" % version_file )

    version = None

    with open(version_file, 'r+') as f:

        text = f.read()
        m = re.search("version: (.*)", text)

        if m:
            version = m.group(1)

        if version:

            print("Found version: %s" % version)

        else:

            print("No version found in file: %s" % version_file)
            sys.exit(1)

        version_split = version.split(".")
        version_split[-1] = str(int(version_split[-1]) + 1)

        new_version = ".".join(version_split)
        print("New Version: %s" % new_version)
        text = text.replace("version: %s" % version, "version: %s" % new_version)

    with open(version_file, 'w') as f:
        f.write(text)
