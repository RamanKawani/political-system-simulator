# system.py

class TreeNode:
    def __init__(self, name, value=None):
        self.name = name  # Name of the node (e.g., "Government", "Electoral System")
        self.value = value  # Value of the node (e.g., "Democratic Republic")
        self.children = []  # Child nodes (e.g., specific government types)

    def add_child(self, child_node):
        """Add a child to this node (e.g., a specific value or option)."""
        self.children.append(child_node)
    
    def set_value(self, value):
        """Set the value of this node."""
        self.value = value

    def __str__(self):
        """String representation of the tree node."""
        return f"{self.name}: {self.value if self.value else 'No value set'}"


class PoliticalSystem:
    def __init__(self):
        # Create the root node for the political system
        self.root = TreeNode("Political System")
        
        # Add components (branches) to the political system
        self.government = TreeNode("Government Type")
        self.electoral_system = TreeNode("Electoral System")
        self.political_parties = TreeNode("Political Parties")
        self.parliament = TreeNode("Parliament/Legislature")
        self.neo_traditional_system = TreeNode("Neo-Traditional Systems")
        
        # Add these components as children of the root node
        self.root.add_child(self.government)
        self.root.add_child(self.electoral_system)
        self.root.add_child(self.political_parties)
        self.root.add_child(self.parliament)
        self.root.add_child(self.neo_traditional_system)

        # Initialize specific components with some default values
        self.setup_default_system()
    
    def setup_default_system(self):
        """Set default values for the system's branches."""
        # Government types (e.g., Republic, Monarchy, etc.)
        self.government.add_child(TreeNode("Democratic Republic"))
        self.government.add_child(TreeNode("Monarchy"))
        self.government.add_child(TreeNode("Authoritarian"))
        
        # Electoral systems (e.g., Proportional, Majoritarian)
        self.electoral_system.add_child(TreeNode("Proportional Representation"))
        self.electoral_system.add_child(TreeNode("Majoritarian"))

        # Political parties (empty at the start)
        self.political_parties.add_child(TreeNode("Party A"))
        self.political_parties.add_child(TreeNode("Party B"))
        
        # Parliament setup (default)
        self.parliament.add_child(TreeNode("100 Seats"))

        # Neo-traditional systems (e.g., Tribal Council, Chiefdom)
        self.neo_traditional_system.add_child(TreeNode("Tribal Council"))
        self.neo_traditional_system.add_child(TreeNode("Chiefdom"))
    
    def get_current_state(self):
        """Return the current state of the political system in a tree format."""
        return self.root
    
    def set_value(self, category, value):
        """Set the value for a particular category in the tree (e.g., government type)."""
        if category == "Government Type":
            self.government.set_value(value)
        elif category == "Electoral System":
            self.electoral_system.set_value(value)
        elif category == "Political Parties":
            self.political_parties.set_value(value)
        elif category == "Parliament/Legislature":
            self.parliament.set_value(value)
        elif category == "Neo-Traditional Systems":
            self.neo_traditional_system.set_value(value)

    def print_tree(self, node=None, level=0):
        """Recursively print the tree structure."""
        node = node or self.root
        print("  " * level + str(node))
        for child in node.children:
            self.print_tree(child, level + 1)

