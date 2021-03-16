import time
import sys

#declaring a private node class
class _LLNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    #magic method defining print format. Now we can call print(Node)
    def __str__(self):
        return str(self.key) + ": " + str(self.value)

#implementing dictionary using linked list
class LLDictionary:
    def __init__(self):
        #initializes the linked list object
        self._front = None
        self._size = 0

    #magic method to use function len
    def __len__(self):
        return self._size

    #magic method to see if key is in dictionary, returns true if in dictionary
    def __contains__(self, key):
        return not self._find(self._front, key) is None

    #magic method given a key, it returns corresponding value ex dict[key]
    def __getitem__(self, key):
        node = self._find(self._front, key)

        if node is None:
            raise KeyError("Item does not exist")

        return node.value

    #recursively searches through binary tree to find key-value pair
    #with specified given key. If found it returns node with given key.
    def _find(self, node, key):
        if node is None:
            return None

        if key == node.key:
            return node

        else:
            return self._find(node.next, key)

    #magic method that allows its instances to set internal values ex. dict[5] = "John"
    def __setitem__(self, key, value):
        if self._front is None:
            self._front = _LLNode(key, value)
            self._size += 1
        else:
            self._insert(self._front, key, value)

    #internal function that inserts key-value pair in dictionary
    def _insert(self, node, key, value):
        #if key exists, it is updated
        if node.key == key:
            node.value = value
        #if key does not exist, recursive function finds empty space for new key
        elif key != node.key:
            if node.next is not None:
                self._insert(node.next, key, value)
            else:
                # inserts new node at end of linked list
                node.next = _LLNode(key, value)
                self._size += 1

    def pop(self, key):
        #Takes a key and deletes the corresponding entry in the linked list
        value = self[key]
        self._front = self._remove(self._front, key)
        self._size -= 1
        return value

    def _remove(self, node, key):
        # Called by the pop function to remove the entry with the corresponding key
        # Key is not found, raise an exception
        assert node is not None, "Cannot remove non-existent key."

        # Searches for the key
        if key != node.key:
            node.next = self._remove(node.next, key)

        # deletes the key when found and replaces it with the next node
        else:
            temp = node.next
            node = None
            return temp

        return node

    def print_dict(self):
        # Calls the _print_tree function
        if self._front is not None:
            self._print_tree(self._front)

    def _print_tree(self, node):
        # Recursively prints all the nodes in the dictionary
        if node is not None:
            print(node)
            self._print_tree(node.next)

def main():
    sys.setrecursionlimit(10 ** 6)
    dict = LLDictionary()
    for i in range(1, 5004):
        dict[i] = "Jack" + str(i)

    # Calculating time, searching for 99
    start_time = time.time()
    results = 5000 in dict
    print("searching 5000: --- %s seconds ---" % (time.time() - start_time))
    # Calculating time, searching for 20
    start_time = time.time()
    results = 3000 in dict
    print("searching 3000: --- %s seconds ---" % (time.time() - start_time))

    # Time for inserting
    start_time = time.time()
    dict[3425] = "Jack3425"
    print("inserting-3425: --- %s seconds ---" % (time.time() - start_time))
    # Time for inserting
    start_time = time.time()
    dict[-3425] = "Jack-3425"
    print("inserting-3425: --- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()
