class TreeAncestor:
    """ Kth Ancestor of a Tree Node
    User Accepted:779
    User Tried:3540
    Total Accepted:854
    Total Submissions:9056
    Difficulty:Hard
    You are given a tree with n nodes numbered from 0 to n-1 in the form of a parent array where parent[i] is the parent of node i. The root of the tree is node 0.
    
    Implement the function getKthAncestor(int node, int k) to return the k-th ancestor of the given node. If there is no such ancestor, return -1.
    
    The k-th ancestor of a tree node is the k-th node in the path from that node to the root.
    
    Example:
    
    Input:
    ["TreeAncestor","getKthAncestor","getKthAncestor","getKthAncestor"]
    [[7,[-1,0,0,1,1,2,2]],[3,1],[5,2],[6,3]]
    
    Output:
    [null,1,0,-1]
    
    Explanation:
    TreeAncestor treeAncestor = new TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2]);
    
    treeAncestor.getKthAncestor(3, 1);  // returns 1 which is the parent of 3
    treeAncestor.getKthAncestor(5, 2);  // returns 0 which is the grandparent of 5
    treeAncestor.getKthAncestor(6, 3);  // returns -1 because there is no such ancestor
    """

    def __init__(self, n: int, parent: list[int]):
        # 题目意思很简单，告诉你 0 - n-1 这些节点的父节点(0没有父节点)，让你快速找出
        # 一个节点的第k个父节点

        # 如果不考虑效率的话会非常的简单，但是这个题目对效率的容忍度很低
        # 使用时间换空间
        pass

    def getKthAncestor(self, node: int, k: int) -> int:
        pass
