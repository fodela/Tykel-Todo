from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.properties import ListProperty,StringProperty
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton,MDRaisedButton
from kivy.uix.widget import Widget
from kivy.factory import Factory

class HomeScreen(Screen):
    def __init__(self,*args, **kwargs):
        super().__init__()
        self.taxk = Factory.EachPersonalSwippableTask()
    pass

class TaskAdder(Screen):
    pass

# class EachPersonalSwippableTask():
#     pass

class TodoApp(MDApp):
    
    color_primary = ListProperty((13/255, 11/255, 84/255,1))
    color_primary_transparent=ListProperty((13/255, 11/255, 84/255,.5))
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
    
    def add_task_form(self):
        
        if not self.addTaskDialog:
            
            self.addTaskDialog = MDDialog(
                                            title = 'Add Task:',
                                            type = 'custom',
                                            content_cls=TaskAdder(),
                                            size_hint = (.8,.3),
                                            buttons=[
                                                MDFlatButton(
                                                    text = 'Cancel',
                                                    # on_release = self.close_dialog()
                                                ),
                                                MDRaisedButton(
                                                    text = 'Add',text_color = self.color_pink,
                                                    #  on_release= self.close_dialog()
                                                )
                                            ]
                                            )
            self.addTaskDialog.open()
            self.addTaskDialog = None

    def add_task(self):
        # print(HomeScreen().ids.taskList)
        # HomeScreen().ids.taskList.add_widget(Button())
        pass


    def close_dialog(self):
        self.addTaskDialog.dismiss(force=True)
            
        
    def delete_task(self,specific_task):
        specific_task.parent.remove_widget(specific_task)

    def task_state(self,specific_task):
        if not specific_task.strikethrough:
            specific_task.strikethrough = True
            specific_task.color = self.color_white_transparent
        else :
            specific_task.strikethrough = False
            specific_task.color = self.color_white

if __name__ == "__main__":
    TodoApp().run()