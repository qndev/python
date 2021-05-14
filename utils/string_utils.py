class StringUtils:
    @staticmethod
    def check_for_blanks(string: str) -> bool:
        if string and string.strip():
            return False
        return True
