from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.properties import ListProperty,StringProperty
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

class HomeScreen(Screen):
    pass

class TaskAdder(Screen):
    pass

class TodoApp(MDApp):
    color_primary = ListProperty((13/255, 11/255, 84/255,1))
    color_secondary = ListProperty((79/255, 84/255, 161/255,1))
    color_white = ListProperty((1,1,1,1))
    color_pink = ListProperty((224/255, 61/255, 224/255,1))
    color_blue = ListProperty((0,0,1,1))
    color_white_transparent = ListProperty((1,1,1,.5))
    addTaskDialog = None
    addedTodo = StringProperty('Newly added')
    def __init__(self):
        Window.size = (350,600)
        super().__init__()
        
    def add_task(self):
        if not self.addTaskDialog:
            self.addTaskDialog = MDDialog(
                                            title = 'Add Task:',
                                            type = 'custom',
                                            content_cls=TaskAdder(),
                                            size_hint = (.8,.3),
                                            buttons=[
                                                MDFlatButton(
                                                    text = 'Cancel',text_color = self.color_pink
                                                ),
                                                MDFlatButton(
                                                    text = 'Add',text_color = self.color_pink
                                                )
                                            ]
                                            )
            self.addTaskDialog.open()
            self.addTaskDialog = None

if __name__ == "__main__":
    TodoApp().run()