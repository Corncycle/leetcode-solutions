class Solution:
    def simplifyPath(self, path: str) -> str:
        class Dir:
            def __init__(self, name, parent) -> None:
                self.name = name
                self.parent = parent
                self.child = None

        def handleSegment(segment):
            if segment:
                if segment == "..":
                    if self.curr.parent:
                        self.curr = self.curr.parent
                        self.curr.child = None
                elif segment != ".":
                    self.curr.child = Dir("/" + segment, self.curr)
                    self.curr = self.curr.child

        i = 0
        self.curr = Dir("", None)

        while i < len(path) and path[i] == "/":
            i += 1

        currSegment = ""
        while i < len(path):
            if path[i] == "/":
                handleSegment(currSegment)
                currSegment = ""
            else:
                currSegment = currSegment + path[i]
            i += 1
        handleSegment(currSegment)

        fullPath = []
        while self.curr.parent:
            fullPath.append(self.curr.name)
            self.curr = self.curr.parent
        
        if len(fullPath) == 0:
            return "/"

        return "".join(reversed(fullPath))