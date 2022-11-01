class TrieNode:
     
    # Trie node class
    def __init__(self):
        self.children = [None]*26
 
        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False
class Trie:
 def __init__(self):
  self.root=self.getNode()
 def getNode(self):
  return TrieNode()
 def insert(self,key):
		
		# If not present, inserts key into trie
		# If the key is prefix of trie node,
		# just marks leaf node
		pCrawl = self.root
		#length = len(key)
		for level in key: #range(length):
			index =ord(level)-ord('a') #self._charToIndex(key[l])

			# if current character is not present
			if not pCrawl.children[index]:
				pCrawl.children[index] = self.getNode()
			pCrawl = pCrawl.children[index]
        
		# mark last node as leaf
		pCrawl.isEndOfWord = True
 def search(self, key):
		
		# Search key in the trie
		# Returns true if key presents
		# in trie, else false
		pCrawl = self.root
		#length = len(key)
		for level in key: #range(length):
			index =ord(level)-ord('a') #self._charToIndex(key[level])
			if not pCrawl.children[index]:
				return False
			pCrawl = pCrawl.children[index]

		return pCrawl.isEndOfWord
  #print(test.children[0])
tab=["debut","voir","test","trouve"]
test=Trie()
for j in tab:
 test.insert(j)
print(test.search("debute"))
'''def printtrie(node):
 queue=[]
 if node :
  queue.append(node)
  temp=queue.pop(0)
  print(temp.root.children)
print(printtrie(test))
voir="un petit test"
for i in voir:
 print(i)'''
