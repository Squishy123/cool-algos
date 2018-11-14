class BinaryTree {
    constructor(value, left, right) {
        this.value = value;
        this.left = left;
        this.right = right;
    }
}

let mat = [];
function drawTree(tree) {
    if(!tree) return;

    return tree.value + (tree.left) ? drawTree(tree.left): '' + (tree.right) ? drawTree(tree.right): '';
}

tree = new BinaryTree('a', new BinaryTree('b', new BinaryTree('d'), new BinaryTree('e')), new BinaryTree('c', new BinaryTree('f')));
console.log(drawTree(tree));