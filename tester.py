from solution import *

class TestResult :
    def __init__(self) :
        self.incorrect = 0

        self.p1_test()
        self.p2_test()
        self.p3_test()
        self.p4_test()

        if self.incorrect < 2 :
            print("You Passed.")
        else :
            print("You Did Not Passed.")


    def p1_test(self) :

        try :
            assert problem_1(2, 2) == 1
            assert problem_1(3, 7) == 17
            assert problem_1(10, 15) == 145
            print("Problem 1: Correct")
        
        except AssertionError :
            self.incorrect += 1
            print("Problem 1: Incorrect")

    
    def p2_test(self) :

        try :
            assert problem_2('ATTGCCACTC', 'TAACGTTGAG') == 6
            assert problem_2('ACACCTG', 'TGTCGAC') == 4
            assert problem_2('GTCACCTCCTT', 'AAGTGGAGGAA') == 1
            assert problem_2('ATCCCATTC', 'TAGGGTAAG') == 0
            print("Problem 2: Correct")
        
        except AssertionError :
            self.incorrect += 1
            print("Problem 2: Incorrect")

        
    def p3_test(self) :

        try :
            assert problem_3(-1000) == "Error"
            assert problem_3(100) == 99
            assert problem_3(1111) == 1001
            assert problem_3(50920) == 50905
            print("Problem 3: Correct")
        
        except AssertionError :
            self.incorrect += 1
            print("Problem 3: Incorrect")

    
    def p4_test(self) :

        try : 
            assert problem_4("ICS", "PJZ", "TURINGS") == "ABYPUNZ"
            assert problem_4("JOKE", "JOKE", "HELLO") == "HELLO"
            assert problem_4("MR.COLLINS", "GL.WIFFCHM", "WORLD!") == "QILFX!"
            print("Problem 4: Correct")
        
        except AssertionError :
            self.incorrect += 1
            print("Problem 4: Incorrect")

TestResult()