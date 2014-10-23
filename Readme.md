## bibgraph

`bibgraph` builds a citation graph from an _annotated_ bibtex file.

Bibgraph expects to find the following fields:
1. `cites` on every entry to be added to the graph; this contains a
   list of (keys of )entries cited by that entry
2. `tags` (optional) marking the status of that document; the
   following tags are supported:
   1. `i` - in progress
   2. `t` - to read
   3. `r` - read
   4. `m` - append this tag to each entry you have fully mapped
      (i.e. checked all interesting references and works that refer to
      it and added them to the bibliography graph)

An example entry for a paper citing `zhang2009fpga` which is `in
progress` and `mapped`:

```
@inproceedings{kestur2012towards,
   title = {{Towards a universal FPGA matrix-vector multiplication architecture}},
   author = {Kestur, Srinidhi and Davis, John D and Chung, Eric S},
   booktitle = FCCM,
   pages = {9--16},
   year = {2012},
   cites = {zhang2009fpga},
   tags = {im}
}
```

## Suggested Workflow

1. Pick a paper
2. Set it as `t`
3. Add it to the bibliography graph
4. Add all _interesting_ references (based on title and context)
5. Add all work citing the paper (e.g. using Google Scholar's _Cited By_ feature)
6. Set is as `m`
7. Play some _Mass Effect_...

## Requires

1. `graphviz` - get with `apt-get install graphviz`

2. `python2.7` - if it's not there - __REALLY?!__

3. `pip` - get with `apt-get install pip`

4. Some python packages: `pip install bibtexparser pydot2 networkx`

## Running

`python bibgraph.py /path/to/your/bibliography.bib`

This produces a `bib.png` file a the bibliography graph like the one below.

![Example bibgraph](/bib.png?raw=true "Example bibgraph")
