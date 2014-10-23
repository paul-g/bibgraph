import sys
import bibtexparser
import networkx as nx
import pydot
from subprocess import call


def unpack(citationString):
    return [s.strip() for s in citationString.split(',')]


def main():
    bibfile = sys.argv[1]

    with open(bibfile) as bibtex_file:
        bibtex = bibtexparser.load(bibtex_file)

    citations = {}

    for key, entry in bibtex.entries_dict.iteritems():
        cites = entry.get('cites')
        if cites:
            print key
            print cites
            citations[key] = unpack(cites)

    G = nx.DiGraph()
    for key, entry in citations.iteritems():
        for cit in entry:
            G.add_edge(key, cit)
    
    print citations
    nx.write_dot(G, "test.dot")

    call(["gvpr", "-c", "-f", "filter.gvpr", "test.dot", "-o", "test_nice.dot"])
    call(["ccomps -x test_nice.dot | dot | gvpack -array1 | neato -Tpng -n2 -o test.png"], shell=True)
    

if __name__ == '__main__':
    main()
