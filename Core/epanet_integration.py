import epanettools.epanettools as epa


def epanet_import(epainputfile,network = None):
    ### This function will import an epanet .inp file and output the data into the hyd_Trans network file type
    ### It requires the input filename, and a network
    es = epa.EPANetSimulation(epainputfile)
    noNodes = len(es.network.nodes)
    noLinks = len(es.network.links)
    print("There are ", noNodes, " in the network")
    print("There are ", noLinks, " in the network")



