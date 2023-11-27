import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class MyGrid(Widget):
    question = ObjectProperty(None)
    answer = ObjectProperty(None)
    score = ObjectProperty(None)
    do = ObjectProperty(None)
    result = ObjectProperty(None)

    lq = {"1+1":"2", "2+5":"7", "12+16":"28", "54+43":"97", "563+325":"888"}
    i = 0

    def btn(self):
        self.do.text = "Next"
        print(list(self.lq.keys()))
        if self.i > 5 : self.result.text = "Try Next Time!!!!"
        else:
            if self.i < 5:
                self.question.text = list(self.lq.keys())[self.i]
            if self.i > 0:
                if self.answer.text == list(self.lq.values())[self.i - 1]:
                    self.result.text = "Right!!!!"
                    self.answer.text = ""
                    self.score.text = str(int(self.score.text) + 1)
                else:
                    self.result.text = "Wrong!!!!"
                    self.answer.text = ""
            self.i+=1
            if self.i > 5: self.result.text = "Your Final Score is: " + self.score.text

        




class QuizApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    QuizApp().run()