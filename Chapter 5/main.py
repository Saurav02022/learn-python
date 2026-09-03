# ==============================================================================
# PYTHON DATA STRUCTURES
# ==============================================================================

# A Python dictionary is a collection of key-value pairs, and a Python set is an
# unordered collection of unique values.

# ------------------------------------------------------------------------------
# Python Dictionary
# ------------------------------------------------------------------------------
# * Definition: A container that links a unique key to a specific value.
# * Syntax: {"name": "Alice", "age": 25}
# * Main use: Looking up information quickly by using a specific name or key 
#             instead of a numeric position.

# Code Example:
user_profile = {
    "username": "coder123",
    "email": "coder@example.com",
    "login_count": 5
}

# Looking up a value using its key
print(user_profile["email"])  # Output: coder@example.com


# ------------------------------------------------------------------------------
# Python Set
# ------------------------------------------------------------------------------
# * Definition: A container that holds only unique items without any duplicate
#               values or keys.
# * Syntax: {"apple", "banana", "cherry"}
# * Main use: Removing duplicate items from a group or testing if an item is present.

# Code Example:
# Creating a set with duplicate items
raw_tags = {"python", "coding", "python", "web", "coding"}

# Duplicates are automatically removed
print(raw_tags)  # Output: {'python', 'coding', 'web'}

# Testing if an item exists in the set
print("web" in raw_tags)  # Output: True


# ==============================================================================
# JAVASCRIPT COMPARISON
# ==============================================================================

# A JavaScript object is most similar to a Python dictionary because both use 
# key-value pairs, while a Python set is different because it only stores 
# single unique values.

# ------------------------------------------------------------------------------
# Comparison Table
# ------------------------------------------------------------------------------
# | Feature           | Python Dictionary | Python Set  | JavaScript Object |
# |-------------------|-------------------|-------------|-------------------|
# | Structure         | Key-value         | Values only | Key-value         |
# | Unique items?     | Unique keys       | Unique items| Unique keys       |
# | Holds functions?  | No                | No          | Yes               |

# ------------------------------------------------------------------------------
# Key Comparisons
# ------------------------------------------------------------------------------

# * Python Dictionary vs JavaScript Object: 
#   Both link a key to a value. In Python, keys can be numbers, strings, or 
#   tuples. In JavaScript, keys are usually strings or symbols, and JavaScript 
#   objects can also store functions (methods).

# Code Example (Python Dictionary):
# Strict data storage, keys can be numeric or tuples
py_dict = {101: "Active Status", ("lat", "lon"): "Location"}
print(py_dict[101])  # Output: Active Status

# Code Example (JavaScript Object Syntax for reference):
# const jsObject = {
#     id: 101,
#     greet: function() { return "Hello from JS!"; }
# };
# console.log(jsObject.id);       // Output: 101
# console.log(jsObject.greet());  // Output: Hello from JS!


# * Python Set vs JavaScript Object: 
#   A Python set holds a list of unique items without keys. A JavaScript object 
#   is not a set, but developers sometimes use object keys with a value of true 
#   to act like a set. JavaScript also has its own Set type which matches 
#   Python's set directly.

# Code Example (Python Set):
# Built-in unique item tracker
allowed_ids = {101, 102, 103}

# Code Example (JavaScript Emulation Syntax for reference):
# const allowedIdsObj = { 101: true, 102: true, 103: true };
# const allowedIdsSet = new Set([101, 102, 103]);
