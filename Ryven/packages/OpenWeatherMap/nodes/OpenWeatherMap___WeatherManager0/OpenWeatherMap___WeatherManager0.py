from NENV import *


# API METHODS

# self.main_widget()        <- access to main widget


# Ports
# self.input(index)                   <- access to input data
# self.set_output_val(self, index, val)    <- set output data port value
# self.exec_output(index)             <- executes an execution output

# self.create_input(type_, label, widget_name=None, widget_pos='under', pos=-1)
# self.delete_input(index or input)
# self.create_output(type_, label, pos=-1)
# self.delete_output(index or output)


# Logging
# mylog = self.new_log('Example Log')
# mylog.log('I\'m alive!!')
# self.log_message('hello global!', 'global')
# self.log_message('that\'s not good', 'error')

# ------------------------------------------------------------------------------

from pyowm import OWM


class WeatherManager_Node(Node):
    def __init__(self, params):
        super(WeatherManager_Node, self).__init__(params)

        # self.special_actions['action name'] = {'method': M(self.action_method)}
        # ...

    # don't call self.update_event() directly, use self.update() instead
    def update_event(self, input_called=-1):
        if input_called==0:
            owm = OWM(self.input(1))
            mgr = owm.weather_manager()
            self.set_output_val(1, mgr)
            self.exec_output(0)

    def get_data(self):
        data = {}
        # ...
        return data

    def set_data(self, data):
        pass # ...


    def remove_event(self):
        pass