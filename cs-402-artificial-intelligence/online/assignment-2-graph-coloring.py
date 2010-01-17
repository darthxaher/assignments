#!/usr/bin/pythonimport copyadjacencent = {1: (3, 4, 5, 6),	2: (5, 6),	3: (1, 4, 5),	4: (1, 3, 6),	5: (1, 2, 3, 6),	6: (1, 2, 4, 5)}colors = ['Red', 'Green', 'Blue']def call_dfs(graph):	# return if no free space is found to color	if graph.values().index(None) == -1: return graph	outcome = graph	for node in graph.keys():		outcome = dfs(node, graph)		if outcome != None:			# if outcome is a valid graph, break, otherwise finish the loop			break	# if solution found, return the solution, else return the original graph	return outcomedef dfs(node, graph):	global colors	global adjacencent	outcome = graph	# only if the node is free	if graph[node] == None:		for color in colors:			# coloring the node			graph[node] = color			# check if this color is good			for neighbour in adjacencent[node]:				# color is bad				if graph[node] == graph[neighbour]:					return None			# color is good, prepare the next node to color			if node < len(graph):				outcome = dfs(node+1, graph)				if outcome == None:	# node and neighbour same color					# try the next color					continue				else:					return outcome			else:				# there is no place to color				return graph	return outcomeif __name__ == '__main__':	graph = dict(zip([x for x in range(1, 7)], [None for x in range(1, 7)]))	out = call_dfs(graph)	print out