import code
from contextlib import redirect_stdout, redirect_stderr

from packaging.version import Version
from ryvencore.addons.Logging import LoggingAddon

from ryven.node_env import *
guis = import_guis(__file__)


class NodeBase(Node):
    version = 'v0.2'
    GUI = guis.SpecialNodeGuiBase

    def have_gui(self):
        return hasattr(self, 'gui')


class DualNodeBase(NodeBase):
    """For nodes that can be active and passive"""

    GUI = guis.DualNodeBaseGui

    def __init__(self, params, active=True):
        super().__init__(params)

        self.active = active
        # if active:
        #     self.actions['make passive'] = {'method': self.make_passive}
        # else:
        #     self.actions['make active'] = {'method': self.make_active}

    def make_passive(self):
        # del self.actions['make passive']

        self.delete_input(0)
        self.delete_output(0)
        self.active = False

        # self.actions['make active'] = {'method': self.make_active}

    def make_active(self):
        # del self.actions['make active']

        self.create_input(type_='exec', insert=0)
        self.create_output(type_='exec', insert=0)
        self.active = True

        # self.actions['make passive'] = {'method': self.make_passive}

    def get_state(self) -> dict:
        return {
            'active': self.active
        }

    def set_state(self, data: dict, version):
        self.active = data['active']


# -------------------------------------------


class Checkpoint_Node(DualNodeBase):
    """Provides a simple checkpoint to reroute your connections"""

    title = 'checkpoint'
    init_inputs = [
        NodeInputType(type_='data'),
    ]
    init_outputs = [
        NodeOutputType(type_='data'),
    ]
    GUI = guis.CheckpointNodeGui

    def __init__(self, params):
        super().__init__(params)

        self.display_title = ''

        self.active = False

    """
    state transitions
    """

    def clear_ports(self):
        # remove all outputs
        for i in range(len(self.outputs)):
            self.delete_output(0)

        # remove all inputs
        for i in range(len(self.inputs)):
            self.delete_input(0)

    def make_active(self):
        # self.active = True
        #
        # # rebuild inputs and outputs
        # self.clear_ports()
        # self.create_input(type_='exec')
        # self.create_output(type_='exec')
        #
        # # update actions
        # del self.actions['make active']
        # self.actions['make passive'] = {
        #     'method': self.make_passive
        # }
        # self.actions['remove output'] = {
        #     '0': {'method': self.remove_output, 'data': 0}
        # }

        num_outputs = len(self.outputs)
        self.clear_ports()
        super().make_active()
        for i in range(1, num_outputs):
            self.add_output()


    def make_passive(self):
        # self.active = False
        #
        # # rebuild inputs and outputs
        # self.clear_ports()
        # self.create_input(type_='data')
        # self.create_output(type_='data')
        #
        # # update actions
        # del self.actions['make passive']
        # self.actions['make active'] = {
        #     'method': self.make_active
        # }
        # self.actions['remove output'] = {
        #     '0': {'method': self.remove_output, 'data': 0}
        # }

        num_outputs = len(self.outputs)
        super().make_passive()
        self.clear_ports()
        for i in range(num_outputs):
            self.add_output()

    # """Actions"""

    def add_output(self):
        index = len(self.outputs)

        if self.active:
            self.create_output(type_='exec')
        else:
            self.create_output(type_='data')

        # self.actions['remove output'][str(index)] = {
        #     'method': self.remove_output,
        #     'data': index,
        # }

    def remove_output(self, index):
        self.delete_output(index)

        # del self.actions['remove output'][str(len(self.outputs))]

    """
    update
    """

    def update_event(self, inp=-1):
        if self.active and inp == 0:
            for i in range(len(self.outputs)):
                self.exec_output(i)

        elif not self.active:
            data = self.input(0)
            for i in range(len(self.outputs)):
                self.set_output_val(i, data)

    """
    state reload
    """

    # def get_state(self) -> dict:
    #     return {
    #         **super().get_state(),
    #         'num outputs': len(self.outputs),
    #     }
    #
    # def set_state(self, data: dict, version):
    #     self.actions['remove output'] = {
    #         {'method': self.remove_output, 'data': i}
    #         for i in range(data['num outputs'])
    #     }
    #
    #     if data['active']:
    #         self.make_active()


class Button_Node(NodeBase):
    title = 'Button'
    init_inputs = []
    init_outputs = [
        NodeOutputType(type_='exec')
    ]
    GUI = guis.ButtonNodeGui

    def update_event(self, inp=-1):
        self.exec_output(0)


class Print_Node(DualNodeBase):
    title = 'Print'
    init_inputs = [
        NodeInputType(type_='exec'),
        NodeInputType(),  # dtype=dtypes.Data(size='m')
    ]
    init_outputs = [
        NodeOutputType(type_='exec'),
    ]
    # color = '#5d95de'

    def __init__(self, params):
        super().__init__(params, active=True)

    def update_event(self, inp=-1):
        if inp == 0:
            print(self.input(1 if self.active else 0).payload)


import logging


class Log_Node(DualNodeBase):
    title = 'Log'
    init_inputs = [
        NodeInputType(type_='exec'),
        NodeInputType('msg', type_='data'),
    ]
    init_outputs = [
        NodeOutputType(type_='exec'),
    ]
    GUI = guis.LogNodeGui

    logs = {}   # {int: Logger}
    in_use = set()  # make sure we don't reuse numbers on copy & paste

    def __init__(self, params):
        super().__init__(params, active=True)

        self.number: int = None
        self.logger: logging.Logger = None
        # self.active_target: int = None

    def place_event(self):
        if self.number is None:
            # didn't load; initialize
            self.number = len(self.logs)
            self.logs[self.number] = \
                self.logs_ext().new_logger(self, 'Log Node')
            self.in_use.add(self.number)
            # self.active_target = self.number

    def logs_ext(self) -> LoggingAddon:
        return self.get_addon('Logging')

    def update_event(self, inp=-1):
        if inp == 0:
            msg = self.input(1 if self.active and inp == 0 else 0).payload
            self.logs[self.number].log(logging.INFO, msg=msg)
            # TODO: support more than INFO, with a dropdown menu in main widget

    def get_state(self) -> dict:
        return {
            **super().get_state(),
            'number': self.number,
            # 'active_target': self.active_target,
        }

    def set_state(self, data: dict, version):
        if Version(version) < Version('0.2'):
            # ignore old version
            return
        super().set_state(data, version)
        n = data['number']
        if n not in self.in_use:
            self.number = n
        else:
            # number already in use; generate a new one
            # happens on copy & paste
            self.number = len(self.logs)

        # the logging addon will have re-created the logger
        # for us already
        self.logs[self.number] = \
            self.logs_ext().new_logger(self, 'Log Node')

        # if self.session.gui and self.main_widget():
        #     self.main_widget().set_target(self.target)


class Clock_Node(NodeBase):
    title = 'clock'
    init_inputs = [
        NodeInputType('delay'),
        NodeInputType('iterations'),
    ]
    init_outputs = [
        NodeOutputType(type_='exec')
    ]
    GUI = guis.ClockNodeGui

    # When running with GUI, this node uses QTime which doesn't
    # block the GUI. When running without GUI, it uses time.sleep()

    def __init__(self, params):
        super().__init__(params)

        self.running_with_qt = False

    def place_event(self):
        self.running_with_qt = self.GUI is not None

        if self.running_with_qt:
            from qtpy.QtCore import QTimer
            self.timer = QTimer()
            self.timer.timeout.connect(self.timeouted)
            self.iteration = 0

    def timeouted(self):
        self.exec_output(0)
        self.iteration += 1
        if -1 < self.input(1).payload <= self.iteration:
            self.stop()

    def start(self):
        if self.running_with_qt:
            self.timer.setInterval(self.input(0).payload)
            self.timer.start()
        else:
            import time
            for i in range(self.input(1).payload):
                self.exec_output(0)
                time.sleep(self.input(0).payload/1000)

    def stop(self):
        assert self.running_with_qt
        self.timer.stop()
        self.iteration = 0

    def toggle(self):
        # triggered from main widget
        if self.running_with_qt:
            if self.timer.isActive():
                self.stop()
            else:
                self.start()
        # toggling is impossible when using time.sleep()

    def update_event(self, inp=-1):
        if self.running_with_qt:
            self.timer.setInterval(self.input(0).payload)

    def remove_event(self):
        if self.running_with_qt:
            self.stop()


class Slider_Node(NodeBase):
    title = 'slider'
    init_inputs = [
        NodeInputType('scl'),
        NodeInputType('round'),
    ]
    init_outputs = [
        NodeOutputType(),
    ]
    GUI = guis.SliderNodeGui

    def __init__(self, params):
        super().__init__(params)

        self.val = 0

    def place_event(self):
        self.update()

    def update_event(self, inp=-1):
        v = self.input(0).payload * self.val
        if self.input(1).payload:
            v = round(v)
        self.set_output_val(0, Data(v))

    def get_state(self) -> dict:
        return {'val': self.val}

    def set_state(self, data: dict, version):
        self.val = data['val']


class _DynamicPorts_Node(NodeBase):
    init_inputs = []
    init_outputs = []
    GUI = guis.DynamicPortsGui

    # def __init__(self, params):
    #     super().__init__(params)
    #
    #     self.actions['add input'] = {'method': self.add_inp}
    #     self.actions['add output'] = {'method': self.add_out}
    #
    #     self.num_inputs = 0
    #     self.num_outputs = 0

    def add_input(self):
        self.create_input()

        # index = self.num_inputs
        # self.actions[f'remove input {index}'] = {
        #     'method': self.remove_inp,
        #     'data': index
        # }
        #
        # self.num_inputs += 1

    def remove_input(self, index):
        self.delete_input(index)
        # self.num_inputs -= 1
        # del self.actions[f'remove input {self.num_inputs}']

    def add_output(self):
        self.create_output()

        # index = self.num_outputs
        # self.actions[f'remove output {index}'] = {
        #     'method': self.remove_out,
        #     'data': index
        # }
        #
        # self.num_outputs += 1

    def remove_output(self, index):
        self.delete_output(index)
        # self.num_outputs -= 1
        # del self.actions[f'remove output {self.num_outputs}']

    # def get_state(self) -> dict:
    #     return {
    #         'num inputs': self.num_inputs,
    #         'num outputs': self.num_outputs,
    #     }

    # def set_state(self, data: dict):
    #     self.num_inputs = data['num inputs']
    #     self.num_outputs = data['num outputs']


class Exec_Node(_DynamicPorts_Node):
    title = 'exec'
    GUI = guis.ExecNodeGui

    def __init__(self, params):
        super().__init__(params)

        self.code = None

    # def place_event(self):
    #     pass

    def update_event(self, inp=-1):
        exec(self.code)

    def get_state(self) -> dict:
        return {
            **super().get_state(),
            'code': self.code,
        }

    def set_state(self, data: dict, version):
        super().set_state(data, version)
        self.code = data['code']


class Eval_Node(NodeBase):
    title = 'eval'
    init_inputs = [
        # NodeInputType(),
    ]
    init_outputs = [
        NodeOutputType(),
    ]
    GUI = guis.EvalNodeGui

    def __init__(self, params):
        super().__init__(params)

        # self.actions['add input'] = {'method': self.add_param_input}

        self.number_param_inputs = 0
        self.expression_code = None

    def place_event(self):
        if self.number_param_inputs == 0:
            self.add_param_input()

    def add_param_input(self):
        self.create_input()

        # index = self.number_param_inputs
        # self.actions[f'remove input {index}'] = {
        #     'method': self.remove_param_input,
        #     'data': index
        # }

        self.number_param_inputs += 1

    def remove_param_input(self, index):
        self.delete_input(index)
        self.number_param_inputs -= 1
        # del self.actions[f'remove input {self.number_param_inputs}']

    def update_event(self, inp=-1):
        inp = [self.input(i) for i in range(self.number_param_inputs)]
        self.set_output_val(0, eval(self.expression_code))

    def get_state(self) -> dict:
        return {
            'num param inputs': self.number_param_inputs,
            'expression code': self.expression_code,
        }

    def set_state(self, data: dict, version):
        self.number_param_inputs = data['num param inputs']
        self.expression_code = data['expression code']


class Interpreter_Node(NodeBase):
    """Provides a python interpreter via a basic console with access to the
    node's properties."""
    title = 'interpreter'
    init_inputs = []
    init_outputs = []
    GUI = guis.InterpreterConsoleGui

    """
    commands
    """

    def clear(self):
        self.hist.clear()
        self._hist_updated()

    def reset(self):
        self.interp = code.InteractiveInterpreter(locals=locals())

    COMMANDS = {
        'clear': clear,
        'reset': reset,
    }

    """
    behaviour
    """

    def __init__(self, params):
        super().__init__(params)

        self.interp = None
        self.hist: [str] = []
        self.buffer: [str] = []

        self.reset()

    def _hist_updated(self):
        if self.have_gui():
            self.gui.main_widget().interp_updated()

    def process_input(self, cmds: str):
        m = self.COMMANDS.get(cmds)
        if m is not None:
            m()
        else:
            for l in cmds.splitlines():
                self.write(l)  # print input
                self.buffer.append(l)
            src = '\n'.join(self.buffer)

            def run_src():
                more_inp_required = self.interp.runsource(src, '<console>')
                if not more_inp_required:
                    self.buffer.clear()

            if self.session.gui:
                with redirect_stdout(self), redirect_stderr(self):
                    run_src()
            else:
                run_src()

    def write(self, line: str):
        self.hist.append(line)
        self._hist_updated()


class Storage_Node(NodeBase):
    """Sequentially stores all the data provided at the input in an array.
    A COPY of the storage array is provided at the output"""

    title = 'store'
    init_inputs = [
        NodeInputType(),
    ]
    init_outputs = [
        NodeOutputType(),
    ]
    GUI = guis.StorageNodeGui

    def __init__(self, params):
        super().__init__(params)

        self.storage = []

        # self.actions['clear'] = {'method': self.clear}

    def clear(self):
        self.storage.clear()
        self.set_output_val(0, Data([]))

    def update_event(self, inp=-1):
        self.storage.append(self.input(0))
        self.set_output_val(0, Data(self.storage.copy()))

    def get_state(self) -> dict:
        return {
            'data': self.storage,
        }

    def set_state(self, data: dict, version):
        self.storage = data['data']


import uuid


class LinkIN_Node(NodeBase):
    """
    Whenever a link IN node receives data (or an execution signal),
    if there is a linked LinkOUT node, it will receive the data
    and propagate it further.
    Notice that this breaks the data flow, which can have substantial
    performance implications and is generally not recommended.
    """

    title = 'link IN'
    init_inputs = [
        NodeInputType(),
    ]
    init_outputs = []  # no outputs
    GUI = guis.LinkIN_NodeGui

    # instances registration
    INSTANCES = {}  # {UUID: node}

    def __init__(self, params):
        super().__init__(params)
        self.display_title = 'link'

        # register
        self.ID: uuid.UUID = uuid.uuid4()
        self.INSTANCES[str(self.ID)] = self

        # self.actions['add input'] = {
        #     'method': self.add_inp
        # }
        # self.actions['remove inp'] = {}
        # self.actions['copy ID'] = {
        #     'method': self.copy_ID
        # }

        self.linked_node: LinkOUT_Node = None

    def add_input(self):
        # index = len(self.inputs)

        self.create_input()

        # self.actions['remove inp'][str(index)] = {
        #     'method': self.rem_inp,
        #     'data': index,
        # }
        if self.linked_node is not None:
            self.linked_node.add_output()

    def remove_input(self, index):
        self.delete_input(index)
        # del self.actions['remove inp'][str(len(self.inputs))]
        if self.linked_node is not None:
            self.linked_node.remove_output(index)

    def update_event(self, inp=-1):
        if self.linked_node is not None:
            self.linked_node.set_output_val(inp, self.input(inp))

    def get_state(self) -> dict:
        return {
            'ID': str(self.ID),
        }

    def set_state(self, data: dict, version):
        if data['ID'] in self.INSTANCES:
            # this happens when some existing node has been copied and pasted.
            # we only want to rebuild links when loading a project, considering
            # new links when copying nodes might get quite complex
            pass
        else:
            del self.INSTANCES[str(self.ID)]     # remove old ref
            self.ID = uuid.UUID(data['ID'])      # use original ID
            self.INSTANCES[str(self.ID)] = self  # set new ref

            # resolve possible pending link builds from OUT nodes that happened
            # to get initialized earlier
            LinkOUT_Node.new_link_in_loaded(self)

    def remove_event(self):
        # break existent link
        if self.linked_node:
            self.linked_node.linked_node = None
            self.linked_node = None


class LinkOUT_Node(NodeBase):
    """The complement to the link IN node"""

    title = 'link OUT'
    init_inputs = []  # no inputs
    init_outputs = []  # will be synchronized with linked IN node
    GUI = guis.LinkOUT_NodeGui

    INSTANCES = []
    PENDING_LINK_BUILDS = {}
    # because a link OUT node might get initialized BEFORE it's corresponding
    # link IN, it then stores itself together with the ID of the link IN it's
    # waiting for in PENDING_LINK_BUILDS

    @classmethod
    def new_link_in_loaded(cls, n: LinkIN_Node):
        for out_node, in_ID in cls.PENDING_LINK_BUILDS.items():
            if in_ID == str(n.ID):
                out_node.link_to(n)

    def __init__(self, params):
        super().__init__(params)
        self.display_title = 'link'

        self.INSTANCES.append(self)
        self.linked_node: LinkIN_Node = None

        # self.actions['link to ID'] = {
        #     'method': self.choose_link_ID
        # }

    # def choose_link_ID(self):
    #     """opens a small input dialog for providing a copied link IN ID"""
    #
    #     from qtpy.QtWidgets import QDialog, QMessageBox, QVBoxLayout, QLineEdit
    #
    #     class IDInpDialog(QDialog):
    #         def __init__(self):
    #             super().__init__()
    #             self.id_str = None
    #             self.setLayout(QVBoxLayout())
    #             self.line_edit = QLineEdit()
    #             self.layout().addWidget(self.line_edit)
    #             self.line_edit.returnPressed.connect(self.return_pressed)
    #
    #         def return_pressed(self):
    #             self.id_str = self.line_edit.text()
    #             self.accept()
    #
    #     d = IDInpDialog()
    #     d.exec_()
    #
    #     if d.id_str is not None:
    #         n = LinkIN_Node.INSTANCES.get(d.id_str)
    #         if n is None:
    #             QMessageBox.warning(title='link failed', text='couldn\'t find a valid link in node')
    #         else:
    #             self.link_to(n)

    def link_to(self, n: LinkIN_Node):
        self.linked_node = n
        n.linked_node = self

        o = len(self.outputs)
        i = len(self.linked_node.inputs)

        # remove outputs if there are too many
        for j in range(i, o):
            self.delete_output(0)

        # add outputs if there are too few
        for j in range(o, i):
            self.create_output()

        self.update()

    def add_output(self):
        # triggered by linked_node
        self.create_output()

    def remove_output(self, index):
        # triggered by linked_node
        self.delete_output(index)

    def update_event(self, inp=-1):
        if self.linked_node is None:
            return

        # update ALL ports
        for i in range(len(self.outputs)):
            self.set_output_val(i, self.linked_node.input(i))

    def get_state(self) -> dict:
        if self.linked_node is None:
            return {}
        else:
            return {
                'linked ID': str(self.linked_node.ID),
            }

    def set_state(self, data: dict, version):
        if len(data) > 0:
            n: LinkIN_Node = LinkIN_Node.INSTANCES.get(data['linked ID'])
            if n is None:
                # means that the OUT node gets initialized before it's link IN
                self.PENDING_LINK_BUILDS[self] = data['linked ID']
            elif n.linked_node is None:
                # pair up
                n.linked_node = self
                self.linked_node = n

    def remove_event(self):
        # break existent link
        if self.linked_node:
            self.linked_node.linked_node = None
            self.linked_node = None


# -------------------------------------------


nodes = [
    Checkpoint_Node,
    Button_Node,
    Print_Node,
    Log_Node,
    Clock_Node,
    Slider_Node,
    Exec_Node,
    Eval_Node,
    Storage_Node,
    LinkIN_Node,
    LinkOUT_Node,
    Interpreter_Node,
]
