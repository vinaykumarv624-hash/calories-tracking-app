from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
import datetime

class CalorieTrackerApp(App):
    def build(self):
        self.daily_food = 0
        self.workout_burn = 0
        self.steps = 0
        self.maintenance = 2500
        self.weight = 91.0
        self.history = []
        
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        title = Label(text='My Calorie Tracker', font_size=26, bold=True, size_hint_y=None, height=60)
        main_layout.add_widget(title)
        
        input_layout = GridLayout(cols=2, spacing=10, size_hint_y=None, height=300)
        
        self.food_input = TextInput(hint_text='Food (e.g. 450)', multiline=False)
        input_layout.add_widget(Label(text='Food Calories:'))
        input_layout.add_widget(self.food_input)
        
        self.workout_input = TextInput(hint_text='Burn (e.g. 150)', multiline=False)
        input_layout.add_widget(Label(text='Workout Burn:'))
        input_layout.add_widget(self.workout_input)
        
        self.steps_input = TextInput(hint_text='Steps (e.g. 9000)', multiline=False)
        input_layout.add_widget(Label(text="Today's Steps:"))
        input_layout.add_widget(self.steps_input)
        
        main_layout.add_widget(input_layout)
        
        btn_layout = BoxLayout(spacing=10, size_hint_y=None, height=50)
        btn_layout.add_widget(Button(text='Add Food', on_press=self.add_food))
        btn_layout.add_widget(Button(text='Add Workout', on_press=self.add_workout))
        btn_layout.add_widget(Button(text='Log Steps', on_press=self.log_steps))
        main_layout.add_widget(btn_layout)
        
        main_layout.add_widget(Button(text='Show Summary', on_press=self.show_summary, size_hint_y=None, height=50))
        main_layout.add_widget(Button(text='New Day', on_press=self.new_day, size_hint_y=None, height=50))
        
        self.summary_label = Label(text='Summary will appear here...', size_hint_y=None, height=280)
        scroll = ScrollView()
        scroll.add_widget(self.summary_label)
        main_layout.add_widget(scroll)
        
        return main_layout
    
    def add_food(self, instance):
        try:
            cals = int(self.food_input.text)
            self.daily_food += cals
            self.food_input.text = ''
            self.show_summary(None)
        except:
            self.summary_label.text = "Please enter valid number!"
    
    def add_workout(self, instance):
        try:
            burn = int(self.workout_input.text)
            self.workout_burn += burn
            self.workout_input.text = ''
            self.show_summary(None)
        except:
            self.summary_label.text = "Please enter valid number!"
    
    def log_steps(self, instance):
        try:
            self.steps = int(self.steps_input.text)
            self.steps_input.text = ''
            self.show_summary(None)
        except:
            self.summary_label.text = "Please enter valid number!"
    
    def show_summary(self, instance):
        net = self.daily_food - self.workout_burn
        deficit = self.maintenance - net
        text = f"""
Date: {datetime.date.today()}
Food Intake : {self.daily_food} kcal
Workout Burn : {self.workout_burn} kcal
Net Calories : {net} kcal
Deficit      : {deficit} kcal

Steps        : {self.steps}
Weight       : {self.weight} kg
        """
        self.summary_label.text = text
    
    def new_day(self, instance):
        self.daily_food = 0
        self.workout_burn = 0
        self.steps = 0
        self.summary_label.text = "New day started! Good luck"

if __name__ == '__main__':
    CalorieTrackerApp().run()
