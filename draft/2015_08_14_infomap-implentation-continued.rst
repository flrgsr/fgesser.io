infomap implentation continued
##############################

:date: 2015-8-14 19:50
:tags: GSoC, Infomap, Map Equation, Python
:category: GSoC
:slug: infomap-implentation-continued
:summary:
:status: draft

*****************************
Week Friday, August 14, 2015
*****************************


Implementing Infomap
--------------------

Work has continued to implement the infomap algorithm assuming an undirected graph as input.
For the complexity of the implementation it is "lucky" that the preprocessing (correlation, thresholding) currently carried out in CPAC and in Neuroimaging generally 
produces undirected graphs. Restricting the input of innfomap to unirected graphs simplifies the forumulation of the **map equation**. 
A detailed reasoning and derivation of it can be found in [1]_ (Page 7)

The current status of the implementation can always be found on github: https://github.com/roijo/C-PAC_complexitytools/blob/master/CPAC/community/algorithms/infomap.py

Progress
--------

Commit history can be found both in the fork of CPAC (https://github.com/roijo/C-PAC_complexitytools/commits/master/CPAC/community/algorithms) as well as own the private github for earlier iterations (https://github.com/flrgsr/community-detection/commits?author=flrgsr) of the rewrite.

This week was spend mainly on hunting down and fixing bugs. 
While for smaller test graphs the correct result could be obtaiend in comparison to the reference implementation it diverge in the case where larger graphs
are given as an input. 
The source of this bug is however very much likely related to the bookkeeping logic around the main algorithm. 

As the intended deployment of this community detection algorithm as part of CPAC requires absolute reliability and stability across various input
datasets the testing was assigned the highest priority. 

Outlook
-------

- Clearance of functional errors
- Introducing more regression tests in order to keep the code maintainable after merged with CPAC
- Detailed documentation of module
- Integration as coherent workflow/module into CPAC



.. [1] Rosvall, M., Axelsson, D., & Bergstrom, C. T. (2010). The map equation. The European Physical Journal Special Topics, 178(1), 13–23. http://doi.org/10.1140/epjst/e2010-01179-1