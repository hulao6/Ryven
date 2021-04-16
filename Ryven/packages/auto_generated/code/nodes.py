import ryvencore_qt as rc
import code


class AutoNode_code_compile_command(rc.Node):
    title = 'compile_command'
    doc = '''Compile a command and determine whether it is incomplete.

    Arguments:

    source -- the source string; may contain \n characters
    filename -- optional filename from which source was read; default
                "<input>"
    symbol -- optional grammar start symbol; "single" (default), "exec"
              or "eval"

    Return value / exceptions raised:

    - Return a code object if the command is complete and valid
    - Return None if the command is incomplete
    - Raise SyntaxError, ValueError or OverflowError if the command is a
      syntax error (OverflowError and ValueError can be produced by
      malformed literals).
    '''
    init_inputs = [
        rc.NodeInputBP(label='source'),
rc.NodeInputBP(label='filename'),
rc.NodeInputBP(label='symbol'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, code.compile_command(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_code_interact(rc.Node):
    title = 'interact'
    doc = '''Closely emulate the interactive Python interpreter.

    This is a backwards compatible interface to the InteractiveConsole
    class.  When readfunc is not specified, it attempts to import the
    readline module to enable GNU readline if it is available.

    Arguments (all optional, all default to None):

    banner -- passed to InteractiveConsole.interact()
    readfunc -- if not None, replaces InteractiveConsole.raw_input()
    local -- passed to InteractiveInterpreter.__init__()
    exitmsg -- passed to InteractiveConsole.interact()

    '''
    init_inputs = [
        rc.NodeInputBP(label='banner'),
rc.NodeInputBP(label='readfunc'),
rc.NodeInputBP(label='local'),
rc.NodeInputBP(label='exitmsg'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, code.interact(self.input(0), self.input(1), self.input(2), self.input(3)))
        