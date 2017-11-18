#!/usr/bin/env python
from PajekFactory import PajekFactory
import ujson
from misc import open_file


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Creates Pajek (.net) files from JSON")
    parser.add_argument('outfile')
    parser.add_argument('--temp-dir', help="Directory to store temporary files in", default=None)
    parser.add_argument('infile', nargs='+')
    arguments = parser.parse_args()

    pjk = PajekFactory(temp_dir=arguments.temp_dir)

    for filename in arguments.infile:
        with open_file(filename) as f:
            for line in f:
                entry = ujson.loads(line)
                if "references" in entry:
                    for citation in entry["references"]:
                        pjk.add_edge(entry["id"], citation)

    with open_file(arguments.outfile, "w") as f:
        pjk.write(f)

