
def get_trie(words):
    trie = {}
    for wrd in words:
        cur = trie

        for ch in wrd:
            cur = cur.setdefault(ch, {})

        cur['wrd'] = wrd
    return trie


def depth_first_search(res, board, i, j, trie):
    # found one
    if trie.get('wrd'):
        res.append(trie['wrd'])
        # de-duplicate
        trie['wrd'] = None
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] not in trie:
        return
    c, board[i][j] = board[i][j], '#'
    depth_first_search(res, board, i - 1, j, trie[c])
    depth_first_search(res, board, i + 1, j, trie[c])
    depth_first_search(res, board, i, j - 1, trie[c])
    depth_first_search(res, board, i, j + 1, trie[c])
    board[i][j] = c


def find_words(board, words):
    trie = get_trie(words)
    res = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            depth_first_search(res, board, i, j, trie)
    return res


words = ["oath","pea","eat","rain"]
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
