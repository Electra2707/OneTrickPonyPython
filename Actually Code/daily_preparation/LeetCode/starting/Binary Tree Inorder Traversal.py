"""Binary Tree Inorder Traversal
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:

Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
"""
from typing import List, Optional
import turtle


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Define a helper function that takes a node and a list
        def helper(node, lst):
            # If the node is not None
            if node:
                # Visit the left subtree
                helper(node.left, lst)
                # Append the node's value to the list
                lst.append(node.val)
                # Visit the right subtree
                helper(node.right, lst)

        # Initialize an empty list to store the values
        result = []
        # Call the helper function on the root node and the result list
        helper(root, result)
        # Return the result list
        return result
# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         if not root:
#             return []
#         l1 = []
#         while root:
#             l1.append(root.val)
#             root = root.left
#         try:
#             l1.append(root.left.val)
#         except:
#             pass
#         return l1

# Define a function that draws a node and its branches


def draw_node(node, t):
    # If the node is not None
    if node:
        # Move forward by 100 units
        t.forward(100)
        # Write the node's value
        t.write(node.val)
        # Save the current position and heading
        pos = t.pos()
        head = t.heading()
        # Turn left by 45 degrees
        t.left(45)
        # Draw the left subtree
        draw_node(node.left, t)
        # Go back to the saved position and heading
        t.penup()
        t.setpos(pos)
        t.setheading(head)
        t.pendown()
        # Turn right by 90 degrees
        t.right(90)
        # Draw the right subtree
        draw_node(node.right, t)


# Create a turtle object with some settings
t = turtle.Turtle()
t.speed(1)  # Set the speed of drawing
t.penup()  # Lift up the pen so it doesn't leave a trail
t.backward(200)  # Move backward by 200 units to make space for the tree
t.pendown()  # Put down the pen

# Create an example tree with values [1,null,2,3]
root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
node1 = TreeNode(1)
node2 = TreeNode(2, TreeNode(3))
node3 = TreeNode(4, TreeNode(5), TreeNode(6))

# Call the draw_node function on the root node and the turtle object
draw_node(root, t)
turtle.exitonclick()

t.clear()
draw_node(node1, t)
turtle.exitonclick()

t.clear()
draw_node(node2, t)
turtle.exitonclick()

t.clear()
draw_node(node3, t)
turtle.exitonclick()

# Exit when you click on turtle window
