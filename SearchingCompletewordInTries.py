def search_key(root, key): 
	# Initialize the currentNode pointer with the root node 
	currentNode = root 

	# Iterate across the length of the string 
	for c in key: 
		# Check if the node exist for the current character in the Trie 
		if currentNode.childNode[ord(c) - ord('a')] is None: 
			# Given word does not exist in Trie 
			return False

		# Move the currentNode pointer to the already existing node for current character 
		currentNode = currentNode.childNode[ord(c) - ord('a')] 

	# Return if the wordCount is greater than 0 
	return currentNode.wordCount > 0
