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
    tags = {}

    for key, entry in bibtex.entries_dict.iteritems():
        cites = entry.get('cites')
        if cites:
            print key
            print cites
            citations[key] = unpack(cites)
        t = entry.get('tags')
        if t:
            tags[key] = t

    G = nx.DiGraph()
    for key, entry in citations.iteritems():
        for cit in entry:
            G.add_edge(key, cit)
    
    print citations

    pydot_G = nx.to_pydot(G)
    for node in pydot_G.get_nodes():
        print node.get_name()
        t = node.get_name()
        if t and tags.get(t):
            node.set('nodetype', tags.get(t))
        else:
            node.set('nodetype', 't')

    pydot_G.write('bib.dot')

    call(["gvpr", "-c", "-f", "filter.gvpr", "bib.dot", "-o", "bib_nice.dot"])
    call(["ccomps -x bib_nice.dot | dot | gvpack -array1 | neato -Tpng -n2 -o bib.png"], shell=True)
    

if __name__ == '__main__':
    main()
