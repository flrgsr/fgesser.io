evaluating community detection results
######################################

:date: 2015-7-15 20:06
:tags: GSoC, Community Detection
:category: GSoC
:slug: evaluating-community-detection-results
:summary:
:status: published



**************************************
Introduction
**************************************


We want to evaluate the results of the community detection algorithm over some real world data.
For this purpose we used 29 subjects from the ABIDE dataset (http://fcon_1000.projects.nitrc.org/indi/abide/) (Yale Site). 

These 29 subjects have later been split up into 2 groups (n=14 and n=15) according to the behavioural meta data available within in the dataset.
To concentrate on evaluating the community detection algorithm we made use of the preprocessed timeseries.
These ROI's timeseries have been extracted according to the CC400 Atlas.



**********************************
Automatization and "Mini Pipeline"
**********************************

In order to process and analyse the data in an automated manner a "mini pipeline" has been developed.

Processing:
-----------

 - load the \*.1D files from disk into a pandas data frame
 - compute the correlation
 - threshold the correlation matrix
 - get a graph representation of the trehsolded adjacency matrix
 - run the community detection algorithm on this graph


Analysis:
---------

 - compute and print out metrics of each detected community (size and number of nodes of each community)
 - annotate the graph with the detected communites
 - color code the nodes of the graph corresponding to the which communiy it belongs and plot the result
 - compute the community size distribution per level and superimpose the result in one plot
 - compute In-Degree/Out-Degree ratio per community
   

*******
Results
*******

By way of illustrating the computed plots for one subject are depicted in the following:

.. figure:: ../images/community_evaluation/subject_0_community_network.png

	Here we can see the rendered graph with its nodes color coded according to the community it belongs to.
	On the left side of the periphery of the circle we see a lot of the singletons (each node altering color form neighbour to neighbour).

.. figure:: ../images/community_evaluation/subject_0_community_size_distribution_level_2.png

	This figure depicts a plot of the community size distribution for one subject.
	The commmunit detection algorithm computed a dendrogram of 3 levels (0-2). 
	The community size distribution for each level is superimposed on each other in this plot.
	The figure exhibts a common pattern: The community size distrubtion follows approximately a declining exponential curve - a lot of small communites, less large ones.
	Referring  to figure 1 we see here clearly the large amount of singletons per level (approx. ~55 on level 2)

The plot was generated with the help of the pandas package and its powerful groupby function.

.. code-block:: Python

	df = pd.DataFrame([(level,val) for level, dct in enumerate(comm_map)
			for val in dct.values()], columns=['level', 'size'])
	size_count = df.groupby(['level'])['size'].apply(lambda x: x.value_counts())
	size_count = size_count.reset_index()
	size_count.columns = ['level', 'community size', 'number of communities']

Group results
-----------------

In the following depicts each boxplot the statistic about the community size distribution grouped per level 


.. figure:: ../images/community_evaluation/box_plot_group1.png

	Results for Group 1

.. figure:: ../images/community_evaluation/box_plot_group2.png

	Results for Group 2

Conclusion
----------

Further investigations and experimentations with larger datasets or data extracted by an atlas which gives more ROI's are necessary to really see group differences.

********
Appendix
********

Raw Data exemplified for Group 1
--------------------------------

The above boxplot for Group 1 was generated from this dataframe. 

+-------+-------+----------------+-------------------------------+
| index | level | community size | average number of communities |
+=======+=======+================+===============================+
| 0     | 0     | 1              | 73.2647058824                 |
+-------+-------+----------------+-------------------------------+
| 1     | 0     | 2              | 20.65                         |
+-------+-------+----------------+-------------------------------+
| 2     | 0     | 3              | 12.325                        |
+-------+-------+----------------+-------------------------------+
| 3     | 0     | 4              | 5.35                          |
+-------+-------+----------------+-------------------------------+
| 4     | 0     | 5              | 3.7027027027                  |
+-------+-------+----------------+-------------------------------+
| 5     | 0     | 6              | 2.58333333333                 |
+-------+-------+----------------+-------------------------------+
| 6     | 0     | 7              | 1.64705882353                 |
+-------+-------+----------------+-------------------------------+
| 7     | 0     | 8              | 1.72413793103                 |
+-------+-------+----------------+-------------------------------+
| 8     | 0     | 9              | 2.0                           |
+-------+-------+----------------+-------------------------------+
| 9     | 0     | 10             | 3.14285714286                 |
+-------+-------+----------------+-------------------------------+
| 10    | 0     | 11             | 1.38461538462                 |
+-------+-------+----------------+-------------------------------+
| 11    | 0     | 12             | 1.0                           |
+-------+-------+----------------+-------------------------------+
| 12    | 0     | 13             | 1.4                           |
+-------+-------+----------------+-------------------------------+
| 13    | 0     | 14             | 1.38461538462                 |
+-------+-------+----------------+-------------------------------+
| 14    | 0     | 15             | 1.0                           |
+-------+-------+----------------+-------------------------------+
| 15    | 0     | 16             | 1.5                           |
+-------+-------+----------------+-------------------------------+
| 16    | 0     | 17             | 1.0                           |
+-------+-------+----------------+-------------------------------+
| 17    | 0     | 18             | 1.0                           |
+-------+-------+----------------+-------------------------------+
| 18    | 0     | 19             | 2.0                           |
+-------+-------+----------------+-------------------------------+
| 19    | 0     | 20             | 1.27272727273                 |
+-------+-------+----------------+-------------------------------+
| 20    | 0     | 21             | 1.0                           |
+-------+-------+----------------+-------------------------------+
| 21    | 0     | 22             | 1.0                           |
+-------+-------+----------------+-------------------------------+
| 22    | 0     | 23             | 1.2                           |
+-------+-------+----------------+-------------------------------+
| 23    | 0     | 24             | 1.0                           |
+-------+-------+----------------+-------------------------------+
| 24    | 0     | 25             | 1.0                           |
+-------+-------+----------------+-------------------------------+
| 25    | 0     | 26             | 1.0                           |
+-------+-------+----------------+-------------------------------+
| 26    | 0     | 27             | 1.0                           |
+-------+-------+----------------+-------------------------------+
| 27    | 0     | 28             | 1.0                           |
+-------+-------+----------------+-------------------------------+
| 28    | 0     | 29             | 1.0                           |
+-------+-------+----------------+-------------------------------+
| 29    | 0     | 30             | 1.0                           |
+-------+-------+----------------+-------------------------------+
| 30    | 0     | 31             | 1.0                           |
+-------+-------+----------------+-------------------------------+
| 31    | 0     | 32             | 1.0                           |
+-------+-------+----------------+-------------------------------+
| 32    | 0     | 33             | 1.0                           |
+-------+-------+----------------+-------------------------------+
| 33    | 0     | 36             | 1.0                           |
+-------+-------+----------------+-------------------------------+
| 34    | 0     | 37             | 1.0                           |
+-------+-------+----------------+-------------------------------+
| 35    | 0     | 39             | 1.0                           |
+-------+-------+----------------+-------------------------------+
| 36    | 0     | 41             | 1.0                           |
+-------+-------+----------------+-------------------------------+
| 37    | 0     | 44             | 1.0                           |
+-------+-------+----------------+-------------------------------+
| 38    | 0     | 45             | 1.0                           |
+-------+-------+----------------+-------------------------------+
| 39    | 0     | 46             | 1.0                           |
+-------+-------+----------------+-------------------------------+
| 40    | 0     | 50             | 1.0                           |
+-------+-------+----------------+-------------------------------+
| 41    | 0     | 52             | 1.0                           |
+-------+-------+----------------+-------------------------------+
| 42    | 0     | 53             | 1.0                           |
+-------+-------+----------------+-------------------------------+
| 43    | 0     | 62             | 1.0                           |
+-------+-------+----------------+-------------------------------+
| 44    | 1     | 1              | 73.325                        |
+-------+-------+----------------+-------------------------------+
| 45    | 1     | 2              | 5.225                         |
+-------+-------+----------------+-------------------------------+
| 46    | 1     | 3              | 4.2                           |
+-------+-------+----------------+-------------------------------+
| 47    | 1     | 4              | 2.72413793103                 |
+-------+-------+----------------+-------------------------------+
| 48    | 1     | 5              | 2.28571428571                 |
+-------+-------+----------------+-------------------------------+
| 49    | 1     | 6              | 1.5                           |
+-------+-------+----------------+-------------------------------+
| 50    | 1     | 7              | 1.0                           |
+-------+-------+----------------+-------------------------------+
| 51    | 1     | 8              | 1.0                           |
+-------+-------+----------------+-------------------------------+
| 52    | 1     | 15             | 1.0                           |
+-------+-------+----------------+-------------------------------+
| 53    | 2     | 1              | 84.9166666667                 |
+-------+-------+----------------+-------------------------------+
| 54    | 2     | 2              | 1.83333333333                 |
+-------+-------+----------------+-------------------------------+
| 55    | 2     | 3              | 1.0                           |
+-------+-------+----------------+-------------------------------+
