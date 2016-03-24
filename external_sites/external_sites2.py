import sys
import collections


sites = collections.defaultdict(str)
for filename in sys.argv[1:]:
    for line in open(filename):
        i = 0
        while True:
            site = None
            i = line.find("http://", i)
            if i > -1:
                i += len("http://")
                for j in range(i, len(line)):
                    if not (line[j].isalnum() or line[j] in ".-"):
                        site = line[i:j].lower()
                        break
                if site and "." in site:
                    sites[site] = filename
                i = j
            else:
                break
for site in sorted(sites):
    print("{0} is referred to in: {1}".format(site, sites[site]))
