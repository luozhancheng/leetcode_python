
from typing import List



class Solution:
    def __init__(self):
        self.root = {}
        self.endWord = "#"
        self.dx = [-1, 1, 0, 0]
        self.dy = [0, 0, -1, 1]
        self.result = set()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            node = node.setdefault(c, {})
        node[self.endWord] = self.endWord

    def dfs(self, board, i, j, cur_word, cur_dict):
        cur_word += board[i][j]
        cur_dict = cur_dict[board[i][j]]
        if self.endWord in cur_dict:
            self.result.add(cur_word)

        tmp, board[i][j] = board[i][j], "@"

        for k in range(4):
            x, y = i + self.dx[k], j + self.dy[k]
            if 0 <= x < self.m and 0 <= y < self.n \
                and board[x][y] != "@" and board[x][y] and board[x][y] in cur_dict:
                self.dfs(board, x, y, cur_word, cur_dict)

        board[i][j] = tmp


    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        print("finding word")

        if not board or not board[0]:
            return []
        if not words:
            return []

        for word in words:
            self.insert(word)

        self.m, self.n = len(board), len(board[0])

        #defs
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] in self.root:
                    self.dfs(board, i, j, "", self.root)


        return list(self.result)


def run():
    words = ["oath", "pea", "eat", "rain"]
    board = [
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']]

    s = Solution()
    ret = s.findWords(board, words)
    print(ret)


