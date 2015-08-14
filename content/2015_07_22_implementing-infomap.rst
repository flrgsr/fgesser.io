implementing infomap
####################

:date: 2015-7-22 20:14
:tags: GSoC, Infomap, Map Equation, Python
:category: GSoC
:slug: implementing-infomap
:summary:
:status: published


********************
Implementing Infomap
********************


In previous entries it was already mentioned:
Besides the Louvain algorithm there is another popular choice among community detecion algorithms: *Infomap*

Louvain vs Infomap
------------------

The is a bit of ambiguity in the terminilogy here:

What is commonly understood as the Louvain method consists actually of a more general underlying heuristic and the introduction of a quality measure.

Louvain *Method* : A specific optimization algorithm based on modularity
	Modularity optimization is a special case of a larger problem: Finding communities by optimizing some quality function Q. 
	The Louvain method takes Q = M (Moduliarty), and seeks partitions with maximal modularity.

Louvain *Framework* : General heuristic to locally optimize a quality function Q 
	A general approach indepedent from a concrete quality function Q.    


The Infomap algorithm follows the general heuristic of the Louvain *Framework* by locally moving nodes, however attempts to indentify communities by minimizing the 
map equation L, an entropy-based measure of the partition quality [1]_ [2]_.


The Map Equation
----------------

The term ``map`` in map equation comes from the notion that clustering of real-world networks with respect to flow resembles cartography of traffic infrastructure 
for better navigation.

Optimizing the map equation over possible module assignments identifies modules in which flow stays for a relatively long time, much like geographical maps identify 
cities as regions in which traffic stays for a relative long time. Flow can refer to real flow of, for example, passengers moving between airports, or flow of random 
walkers guided by the nodes and links of the network as a proxy for the real flow.
But given the network structure, what is the optimal number of modules and the optimal assignment of nodes into those modules? 

The map equation answers these questions using the
fundamental principles of information theory. All regularities
in data can be used to compress the data, such that the
degree of compression becomes a measure for the success
in finding regularities in the data. The map equation takes
advantage of this minimum description principle by measuring
the description length of a random walker on a network [3]_.

The map equation L(M) gives the average number of bits per step that it takes to describe an infinite random walk on a network partitioned according to M:

.. figure:: ../images/infomap/map.png



This equation comprises two terms: first is the entropy of the
movement between modules, and second is the entropy of
movements within modules (where exiting the module also is
considered a movement). Each is weighted by the frequency with
which it occurs in the particular partitioning. Here, q_arc is the
probability that the random walk switches modules on any given
step. H(Q) is the entropy of the module names, i.e., the entropy
of the underlined codewords. H(Pi) is the entropy of
the within-module movements, including the exit code for
module i. The weight p^i_arc is the fraction of within-module
movements that occur in module i, plus the probability of exiting
module i [1]_.

For more details for the formal aspects:
 http://www.pnas.org/content/suppl/2008/01/10/0706851105.DC1/06851SuppAppendix.pdf 



.. [1] Rosvall, M., & Bergstrom, C. T. (2008). Maps of random walks on complex networks reveal community structure. Pnas, 105(4), 1118–1123. http://doi.org/10.1073/pnas.0706851105
.. [2] Rosvall, M., Axelsson, D., & Bergstrom, C. T. (2010). The map equation. The European Physical Journal Special Topics, 178(1), 13–23. http://doi.org/10.1140/epjst/e2010-01179-1
.. [3] Bae, S.-H., Halperin, D., West, J., Rosvall, M., & Howe, B. (2013). Scalable Flow-Based Community Detection for Large-Scale Network Analysis (pp. 303–310). Presented at the 2013 IEEE 13th International Conference on Data Mining Workshops (ICDMW), IEEE. http://doi.org/10.1109/ICDMW.2013.138