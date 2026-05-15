from collections import defaultdict


class Polynomial:
    """
    Data structure for storing polynomial input/output.
    Internally maps exponent (int) -> coefficient (int).

    Examples:
        3x^2 + 2x - 1  =>  {2: 3, 1: 2, 0: -1}
        5x              =>  {1: 5}
        7               =>  {0: 7}
    """

    def __init__(self, terms=None):
        self.terms = {}
        if terms:
            for exp, coeff in terms.items():
                if coeff != 0:
                    self.terms[exp] = coeff

    def __add__(self, other):
        result = defaultdict(int, self.terms)
        for exp, coeff in other.terms.items():
            result[exp] += coeff
        return Polynomial(dict(result))

    def __sub__(self, other):
        result = defaultdict(int, self.terms)
        for exp, coeff in other.terms.items():
            result[exp] -= coeff
        return Polynomial(dict(result))

    def __mul__(self, other):
        # Every term in self multiplied by every term in other
        # Coefficients multiply, exponents add
        result = defaultdict(int)
        for e1, c1 in self.terms.items():
            for e2, c2 in other.terms.items():
                result[e1 + e2] += c1 * c2
        return Polynomial(dict(result))

    def __neg__(self):
        return Polynomial({exp: -coeff for exp, coeff in self.terms.items()})

    def __eq__(self, other):
        return self.terms == other.terms

    def __repr__(self):
        if not self.terms:
            return "0"

        parts = []
        for exp in sorted(self.terms, reverse=True):
            coeff = self.terms[exp]
            if exp == 0:
                parts.append(str(coeff))
            elif exp == 1:
                if coeff == 1:
                    parts.append("x")
                elif coeff == -1:
                    parts.append("-x")
                else:
                    parts.append(f"{coeff}x")
            else:
                if coeff == 1:
                    parts.append(f"x^{exp}")
                elif coeff == -1:
                    parts.append(f"-x^{exp}")
                else:
                    parts.append(f"{coeff}x^{exp}")

        result = parts[0]
        for part in parts[1:]:
            if part.startswith("-"):
                result += f" - {part[1:]}"
            else:
                result += f" + {part}"
        return result


# --------------- Recursive Descent Parser ---------------
#
# Grammar (by precedence, lowest to highest):
#   expr   -> term (('+' | '-') term)*
#   term   -> factor ('*' factor)*
#   factor -> '-' factor | '(' expr ')' | atom
#   atom   -> [number][x['^'number]]
#
# This naturally gives * higher precedence than +/-.

class Parser:
    def __init__(self, text):
        self.text = text.replace(" ", "")
        self.pos = 0
        self.depth = 0  # tracks recursion depth for indentation

    def _indent(self):
        return "  " * self.depth

    def _remaining(self):
        return self.text[self.pos:]

    def parse(self):
        print(f"Parsing: \"{self.text}\"")
        print(f"{'─' * 50}")
        result = self._expr()
        if self.pos != len(self.text):
            raise ValueError(f"Unexpected char '{self.text[self.pos]}' at pos {self.pos}")
        print(f"{'─' * 50}")
        print(f"Final result: {result}  (terms={result.terms})")
        return result

    # ---- grammar rules ----

    def _expr(self):
        """expr -> term (('+' | '-') term)*"""
        print(f"{self._indent()}EXPR  pos={self.pos} remaining=\"{self._remaining()}\"")
        self.depth += 1
        node = self._term()
        while self.pos < len(self.text) and self.text[self.pos] in "+-":
            op = self.text[self.pos]
            self.pos += 1
            print(f"{self._indent()}  op='{op}', left={node}")
            right = self._term()
            prev = node
            node = node + right if op == "+" else node - right
            print(f"{self._indent()}  {prev} {op} {right} = {node}")
        self.depth -= 1
        print(f"{self._indent()}  => EXPR returns: {node}")
        return node

    def _term(self):
        """term -> factor ('*' factor)*"""
        print(f"{self._indent()}TERM  pos={self.pos} remaining=\"{self._remaining()}\"")
        self.depth += 1
        node = self._factor()
        while self.pos < len(self.text) and self.text[self.pos] == "*":
            self.pos += 1
            print(f"{self._indent()}  op='*', left={node}")
            right = self._factor()
            prev = node
            node = node * right
            print(f"{self._indent()}  ({prev}) * ({right}) = {node}")
        self.depth -= 1
        print(f"{self._indent()}  => TERM returns: {node}")
        return node

    def _factor(self):
        """factor -> '-' factor | '(' expr ')' | atom"""
        print(f"{self._indent()}FACTOR  pos={self.pos} remaining=\"{self._remaining()}\"")
        self.depth += 1
        if self.pos < len(self.text) and self.text[self.pos] == "-":
            self.pos += 1
            print(f"{self._indent()}  negation")
            inner = self._factor()
            result = -inner
            self.depth -= 1
            print(f"{self._indent()}  => FACTOR returns: -{inner} = {result}")
            return result
        if self.pos < len(self.text) and self.text[self.pos] == "(":
            self.pos += 1  # skip '('
            print(f"{self._indent()}  parenthesized sub-expression")
            node = self._expr()
            if self.pos >= len(self.text) or self.text[self.pos] != ")":
                raise ValueError("Missing closing parenthesis")
            self.pos += 1  # skip ')'
            self.depth -= 1
            print(f"{self._indent()}  => FACTOR returns: ({node})")
            return node
        result = self._atom()
        self.depth -= 1
        print(f"{self._indent()}  => FACTOR returns: {result}")
        return result

    def _atom(self):
        """atom -> [number][x['^'number]]   (at least one part present)"""
        coeff = None
        exp = 0

        # optional coefficient (integer)
        if self.pos < len(self.text) and self.text[self.pos].isdigit():
            start = self.pos
            while self.pos < len(self.text) and self.text[self.pos].isdigit():
                self.pos += 1
            coeff = int(self.text[start : self.pos])

        # optional variable 'x'
        if self.pos < len(self.text) and self.text[self.pos] == "x":
            self.pos += 1
            exp = 1
            if coeff is None:
                coeff = 1
            # optional '^' exponent
            if self.pos < len(self.text) and self.text[self.pos] == "^":
                self.pos += 1
                start = self.pos
                while self.pos < len(self.text) and self.text[self.pos].isdigit():
                    self.pos += 1
                exp = int(self.text[start : self.pos])

        if coeff is None:
            raise ValueError(f"Expected number or variable at pos {self.pos}")

        result = Polynomial({exp: coeff})
        print(f"{self._indent()}ATOM  => {result}  (coeff={coeff}, exp={exp})")
        return result


def resolve(expression: str) -> Polynomial:
    """Parse and simplify a polynomial expression string."""
    return Parser(expression).parse()


# --------------- Tests ---------------

if __name__ == "__main__":
    tests = [
        ("x + 2x","3x"),
        ("(x+1)*x",            "x^2 + x"),
        ("(x+1)*(x-1)",        "x^2 - 1"),
        ("x^2 + 2*x + 1",     "x^2 + 2x + 1"),
        ("3*x^2 + 2*x^2",     "5x^2"),
        ("(x+1)*(x+1)",       "x^2 + 2x + 1"),
        ("(2*x+3)*(x-1)",     "2x^2 + x - 3"),
        ("5",                   "5"),
        ("x",                   "x"),
        ("-x",                  "-x"),
        ("-(x+1)",             "-x - 1"),
        ("(x+1)*(x+2)*(x+3)", "x^3 + 6x^2 + 11x + 6"),
    ]

    print("=== Polynomial Expression Resolver ===\n")
    all_pass = True
    for expr, expected in tests:
        result = resolve(expr)
        status = "PASS" if str(result) == expected else "FAIL"
        if status == "FAIL":
            all_pass = False
        print(f"  {status}  {expr:30s} => {result}")
        if status == "FAIL":
            print(f"        expected: {expected}")

    print(f"\n{'All tests passed!' if all_pass else 'Some tests failed.'}")
