## 1. Problem Explanation on Finding Files

A file structure is a tree, therefore I employed in order DFS to traverse the structure and find the files.

I ought written a recursive function for that question which needs input the suffix, path, and the list of required files that are found till now.
Run time complexity: O(depth X Avg. number of directory each level)
Space complexity: O(depth)