"""
scaffoldgraph.analysis.representation

Module contains general functions for scaffold analysis
"""


def get_virtual_scaffolds(scaffoldgraph):
    """Get 'virtual' scaffolds in within a scaffold graph

    Virtual scaffolds represent scaffolds that are not directly obtained from
    any molecule of the collection, but generated by the pruning process.
    Virtual scaffolds may provide promising starting points for the synthesis
    or acquisition of compounds complementing the current collection.

    Parameters
    ----------
    scaffoldgraph : (ScaffoldGraph)
    """
    virtual = []
    for scaffold in scaffoldgraph.get_scaffold_nodes():
        mol_count = 0
        for succ in scaffoldgraph.successors(scaffold):
            if scaffoldgraph.nodes[succ].get('type') == 'molecule':
                mol_count += 1
        if mol_count == 0:
            virtual.append(scaffold)
    return virtual


def get_singleton_scaffolds(scaffoldgraph):
    """Get singleton scaffolds within a scaffold graph

    Singleton scaffolds represent scaffolds that are direct members of only
    one compound in the current collection.

    Parameters
    ----------
    scaffoldgraph : (ScaffoldGraph)
    """
    singletons = []
    for scaffold in scaffoldgraph.get_scaffold_nodes():
        mol_count = 0
        for succ in scaffoldgraph.successors(scaffold):
            if scaffoldgraph.nodes[succ].get('type') == 'molecule':
                mol_count += 1
        if mol_count == 1:
            singletons.append(scaffold)
    return singletons