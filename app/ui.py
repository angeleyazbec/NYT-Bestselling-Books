from tkinter import *
#from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class BestBook:
    def __init__(self,book_checker:BookChecker):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.score_label=Label(text="Score:0",fg="white",bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)
        self.canvas=Canvas(width=300,height=250,bg="white")
