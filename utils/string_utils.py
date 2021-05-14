class StringUtils:
    @staticmethod
    def check_for_blanks(string):
        if string and string.strip(): 
            return False    
        return True
