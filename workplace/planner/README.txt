Language: Python
Version: 2.7

Files:

1. input.py : Hold a string of route map
2. graph.py : Convert the input string to meaning full Graph.
			example: {'A':{'B': 5, 'D': 5, 'E': 7},
					  'B':{'C': 4},
					  ........
					  ........
					  }
3. route.py : Have used Dijistra and BFS
			def shortestpath => finds shortest path between given two nodes
			example: Uncomment lines
				# r = Route()
				# print r.shortestpath('E','A')

				and run the file using command 

				>>python route.py

				output wil be => (distance, [path])


			def BFS => to find number of possible routes between given two nodes
			example: Uncomment lines
				# r = Route()
				# print r.BFS('E','A')
				# print r.count

				and execute the file, using command 

				>> python route.py
				output wil be = > PATH 1 : ['C', 'E', 'B'] 
								  PATH 2 : ['C', 'D', 'E', 'B']
								  2 (number of path)

4. queue.py : is helper file for BFS
5. test.py : have written few test cases
			execute this file, using
			>> python route.py
			