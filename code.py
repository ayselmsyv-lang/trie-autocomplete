class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, prefix, max_results=10):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]
        results = []
        self._dfs(node, prefix, results, max_results)
        return results

    def _dfs(self, node, word, results, max_results):
        if len(results) >= max_results:
            return
        if node.is_end:
            results.append(word)
        for ch, child in node.children.items():
            self._dfs(child, word + ch, results, max_results)


dictionary={
  "1": "apple",
  "2": "application",
  "3": "apply",
  "4": "aperture",
  "5": "arc",
  "6": "archive",
  "7": "array",
  "8": "assert",
  "9": "banana",
  "10": "band",
  "11": "bandwidth",
  "12": "base",
  "13": "batch",
  "14": "buffer",
  "15": "build",
  "16": "bundle",
  "17": "cache",
  "18": "callback",
  "19": "cat",
  "20": "class",
  "21": "clone",
  "22": "cluster",
  "23": "compile",
  "24": "config",
  "25": "daemon",
  "26": "data",
  "27": "debug",
  "28": "declare",
  "29": "delta",
  "30": "deploy",
  "31": "detect",
  "32": "device",
  "33": "echo",
  "34": "edge",
  "35": "emit",
  "36": "encode",
  "37": "endpoint",
  "38": "engine",
  "39": "entry",
  "40": "error",
  "41": "fetch",
  "42": "filter",
  "43": "flag",
  "44": "float",
  "45": "fork",
  "46": "format",
  "47": "frame",
  "48": "function",
  "49": "graph",
  "50": "grep",
  "51": "grid",
  "52": "group",
  "53": "guard",
  "54": "handle",
  "55": "hash",
  "56": "header",
  "57": "heap",
  "58": "hook",
  "59": "host",
  "60": "import",
  "61": "index",
  "62": "input",
  "63": "insert",
  "64": "instance",
  "65": "iterator",
  "66": "join",
  "67": "json",
  "68": "kernel",
  "69": "key",
  "70": "kill",
  "71": "label",
  "72": "lambda",
  "73": "latency",
  "74": "layer",
  "75": "lexer",
  "76": "link",
  "77": "list",
  "78": "local",
  "79": "lock",
  "80": "log",
  "81": "loop",
  "82": "map",
  "83": "match",
  "84": "merge",
  "85": "method",
  "86": "mock",
  "87": "model",
  "88": "module",
  "89": "mutex",
  "90": "node",
  "91": "null",
  "92": "object",
  "93": "offset",
  "94": "open",
  "95": "output",
  "96": "overflow",
  "97": "parse",
  "98": "patch",
  "99": "path",
  "100": "pipe",
  "101": "pointer",
  "102": "pool",
  "103": "port",
  "104": "process",
  "105": "proxy",
  "106": "push",
  "107": "query",
  "108": "queue",
  "109": "race",
  "110": "read",
  "111": "record",
  "112": "recursion",
  "113": "render",
  "114": "repo",
  "115": "reset",
  "116": "return",
  "117": "retry",
  "118": "root",
  "119": "router",
  "120": "runtime",
  "121": "save",
  "122": "schema",
  "123": "scope",
  "124": "search",
  "125": "select",
  "126": "send",
  "127": "serialize",
  "128": "server",
  "129": "set",
  "130": "shell",
  "131": "socket",
  "132": "sort",
  "133": "split",
  "134": "stack",
  "135": "stream",
  "136": "string",
  "137": "struct",
  "138": "sync",
  "139": "table",
  "140": "tag",
  "141": "task",
  "142": "thread",
  "143": "token",
  "144": "trace",
  "145": "trie",
  "146": "type",
  "147": "union",
  "148": "update",
  "149": "user",
  "150": "validate",
  "151": "value",
  "152": "variable",
  "153": "vector",
  "154": "version",
  "155": "view",
  "156": "void",
  "157": "worker",
  "158": "write",
  "159": "yield",
  "160": "zone"
}

trie = Trie()
for word in dictionary.values():
    trie.insert(word)

# usage
print(trie.search(input("input your prefix: ")))  
