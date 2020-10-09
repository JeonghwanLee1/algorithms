def preorder(tree,node):
    result = []
    if 'r' not in node and 'l' not in node:
        return [node['elem']]

    result.append(node['elem'])
    if 'l' in node:
        result.extend(preorder(tree,tree[node['l']]))
    if 'r' in node:
        result.extend(preorder(tree,tree[node['r']]))

    return result

def inorder(tree,node):
    result = []
    if 'r' not in node and 'l' not in node:
        return [node['elem']]

    if 'l' in node:
        result.extend(inorder(tree,tree[node['l']]))

    result.append(node['elem'])

    if 'r' in node:
        result.extend(inorder(tree,tree[node['r']]))

    return result

def postorder(tree,node):
    result = []
    if 'r' not in node and 'l' not in node:
        return [node['elem']]

    if 'l' in node:
        result.extend(postorder(tree,tree[node['l']]))
    if 'r' in node:
        result.extend(postorder(tree,tree[node['r']]))

    result.append(node['elem'])
    return result

N = int(input())
tree = {}
for _ in range(N):
    node = {}
    e,l,r = input().split()
    node['elem'] = e
    if l != '.':
        node['l'] = l
    if r != '.':
        node['r'] = r
    tree[e] = node

print(''.join(preorder(tree,tree['A'])))
print(''.join(inorder(tree,tree['A'])))
print(''.join(postorder(tree,tree['A'])))
