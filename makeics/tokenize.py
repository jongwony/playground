from collections import namedtuple


class Token(object):
    """Tokenize Date"""

    def __init__(self):
        self.Token = namedtuple('Token', ['type', 'value'])
        self.tokenDict = dict()

    def generate_tokens(self, pat, query):
        scanner = pat.scanner(query)
        for m in iter(scanner.match, None):
            tok = self.Token(m.lastgroup, m.groupdict()[m.lastgroup])
            if tok.type != 'WS':
                yield tok

    def generate_dict(self, pat, query):
        scanner = pat.scanner(query)
        for m in iter(scanner.match, None):
            if m.lastgroup != 'WS':
                self.tokenDict[m.lastgroup] = m.groupdict()[m.lastgroup]
        return self.tokenDict
