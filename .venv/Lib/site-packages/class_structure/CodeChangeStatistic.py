class CodeChangeStatistic:
    def __int__(self):
        lines_added = 0
        lines_changed = 0
        lines_removed = 0
        lines_same = 0
        lines_similar = 0

    def __init__(self, lines_added, lines_changed, lines_removed, lines_same=0, lines_similar=0):
        self.lines_added = lines_added
        self.lines_changed = lines_changed
        self.lines_removed = lines_removed
        self.lines_same = lines_same
        self.lines_similar = lines_similar

    def set_lines_same(self, line_same):
        self.lines_same = line_same

    def set_lines_similar(self, line_similar):
        self.line_similar = line_similar

    def set_lines_added(self, lines_added):
        self.lines_added = lines_added

    def set_lines_changed(self, lines_changed):
        self.lines_changed = lines_changed

    def set_lines_removed(self, lines_removed):
        self.lines_removed = lines_removed

    def increment_lines_similar(self, lines_similar):
        self.lines_similar += lines_similar

    def increment_lines_same(self, lines_same):
        self.lines_same += lines_same

    def increment_lines_added(self, lines_added):
        self.lines_added += lines_added

    def increment_lines_changed(self, lines_changed):
        self.lines_changed += lines_changed

    def increment_lines_removed(self, lines_removed):
        self.lines_removed += lines_removed

    def merge(self, code_change_statistic):
        self.increment_lines_added(code_change_statistic.lines_added)
        self.increment_lines_removed(code_change_statistic.lines_removed)
        self.increment_lines_changed(code_change_statistic.lines_changed)

    def has_changed(self):
        changed = False
        if self.lines_changed > 0:
            changed = True
        if self.lines_added > 0:
            changed = True
        if self.lines_removed > 0:
            changed = True
        return changed

    def to_string(self):
        return "Lines Added: " + str(self.lines_added) + " Lines Changed: " + str(self.lines_changed) + " Lines Removed " + str(self.lines_removed)