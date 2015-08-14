Making sense of Communities
###########################

:date: 2015-6-4 12:11
:tags: GSoC, Community Detection, Neuroimaging
:category: GSoC
:slug: taming-communities
:summary:
:status: draft

************
Introduction
************

In order to experiment and interpret the output of the community algorithm I cached and extracted the graph that gets computed during the C-PAC workflow.
This enables me to have a quicker turnover on trying out things more interactivly wihtout the time-consuming waiting of the build up of the correlation matrix.
At this stage of investigation the previous steps on how I went up with this particular data is irrelevant. That is not to say to forget about the other parts, they will
be revisted at a later stage and are open for optimization. Here it was important to first have a running system which can be tested on real world data and investigated in
terms of if the communites obtained make sense in a neuroimaging setting.

***************
Data extraction
***************

Once the correlation matrix is thresholded to a binary adjacency matrix the graph can be transformed into a networkx graph structure via.

.. code-block:: python

	def build_graph(adjacenyMatrix):
	G = nx.from_numpy_matrix(adjacenyMatrix)

*Networkx* offers very efficient data strucutes to hold large data sets. 

.. code-block:: python

	G.number_of_nodes()
	81602

.. code-block:: python
	
	G.number_of_edges()
	804740	

.. code-block:: python

    import pickle
    pickle.dump(Graph, open('pickledGraph'))

.. code-block:: python

    G = pickle.load(open('pickledGraph'))

.. code-block:: python
	
	partitionDump.items()
    [
	(967, 1),
	(968, 165),
	(969, 4),
	(970, 4),
	(971, 4),
	(972, 4),
	(973, 27),
	(974, 27),
	(975, 27),
	(976, 27),
	(977, 27),
	(978, 27),
	(979, 1),
	(980, 1),
	(981, 1),
	(982, 1),
	(983, 1),
	(984, 1),
	(985, 1),
	(986, 1),
	(987, 1),
	(988, 1),
	(989, 27),
	(990, 27),
	(991, 27),
	(992, 27),
	(993, 27),
	(994, 27),
	(995, 27),
	(996, 27),
	(997, 71),
	(998, 71),
	(999, 8),
 	...]	

A graph with these attributes uses only ~50MB on disk as a pickled python object.	

The graph and the results of the *Louvain* algorithm were both serialized to disk in order to be decoupled from the current (debug-) session for more comfortable
investigation.

*************************
Results and visualization
*************************

Parameters of the computed graph partitions
===========================================

The results of the *Louvain* community detection algorithm on this graph are as follows:

.. code-block:: python
 
	import CPAC.community_detection.louvain as lou
	lou.modularity(partitionDump, G)
	0.8681385957598554

The algorithm could achive a modularity of ~0.87 on the graph fed into. This result is consistent over several implementations of the *Louvain Method*. Other approaches for
community detecion like *InfoMap* achive very similar results on the same graph.

.. code-block:: python

	#Louvain community detection algorithm from disk
	partitionDump = pickle.load(open('partitionDump'))
	len(set(partitionDump.values()))
	17855

The number of detected communities (17567) is considerable large. Due to inherent properties of the fMRI modularity this is expectable. 


visualization
=============


.. figure:: ../images/communities-size-distribution.png

Figure 1 depicts the distribution of sizes across all detected modularity classes (communites). It is clearly visible that only approx. ~20 communites consists of more than 
500 nodes.


.. figure:: ../images/graphviz.png

Figure 2 is visualization of the detected communities in the OpenOrd Layout [1]_. This visualization gives a more graphic view of how only approx. ~20 communites out of the 
~17k have a large enough number of nodes to be considerd as clusters.


.. .. image:: ../images/pie-chart.png
.. 	:width: 528
.. 	:height: 1054
.. 	:scale: 50

Pain Points
===========

Having a funcitoning workflow is just one part of it. Interpreting the results the algorithm spews out is another and import issue, especially in the context of scientific
software. I first didn't had this aspect in mind put it turned out to be one of the major pain points this week. Ideally we would want to have as output of the workflow
the graph remapped to a standard brain template, neatly parcellated into communites like it is seen in the Neuroimaing Literature [2]_ [3]_. Unfortunalety research papers
seldom come with the code/software attached that was used to process the data. The *Open Science* movement seems to be a promising remedey to these issues combining data
sharing with open sour'ed reasearch code.





.. [1]  Martin, S., Brown, W. M., Klavans, R., & Boyack, K. W. (2011). OpenOrd: an open-source toolbox for large graph layout (Vol. 7868, p. 786806). Presented at the Proceedings of the SPIE. http://doi.org/10.1117/12.871402
.. [2]  Zuo, X.-N., Ehmke, R., Mennes, M., Imperati, D., Castellanos, F. X., Sporns, O., & Milham, M. P. (2012). Network centrality in the human functional connectome. Cerebral Cortex (New York, N.Y. : 1991), 22(8), 1862–1875. http://doi.org/10.1093/cercor/bhr269
.. [3] Meunier, D., Lambiotte, R., & Bullmore, E. T. (2010). Modular and Hierarchically Modular Organization of Brain Networks. Frontiers in Neuroscience, 4, 1–11. http://doi.org/10.3389/fnins.2010.00200