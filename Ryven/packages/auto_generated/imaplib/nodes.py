import ryvencore_qt as rc
import imaplib


class AutoNode_imaplib_Int2AP(rc.Node):
    title = 'Int2AP'
    description = '''Convert integer to A-P string representation.'''
    init_inputs = [
        rc.NodeInputBP(label='num'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imaplib.Int2AP(self.input(0)))
        


class AutoNode_imaplib_Internaldate2tuple(rc.Node):
    title = 'Internaldate2tuple'
    description = '''Parse an IMAP4 INTERNALDATE string.

    Return corresponding local time.  The return value is a
    time.struct_time tuple or None if the string has wrong format.
    '''
    init_inputs = [
        rc.NodeInputBP(label='resp'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imaplib.Internaldate2tuple(self.input(0)))
        


class AutoNode_imaplib_ParseFlags(rc.Node):
    title = 'ParseFlags'
    description = '''Convert IMAP4 flags response to python tuple.'''
    init_inputs = [
        rc.NodeInputBP(label='resp'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imaplib.ParseFlags(self.input(0)))
        


class AutoNode_imaplib_Time2Internaldate(rc.Node):
    title = 'Time2Internaldate'
    description = '''Convert date_time to IMAP4 INTERNALDATE representation.

    Return string in form: '"DD-Mmm-YYYY HH:MM:SS +HHMM"'.  The
    date_time argument can be a number (int or float) representing
    seconds since epoch (as returned by time.time()), a 9-tuple
    representing local time, an instance of time.struct_time (as
    returned by time.localtime()), an aware datetime instance or a
    double-quoted string.  In the last case, it is assumed to already
    be in the correct format.
    '''
    init_inputs = [
        rc.NodeInputBP(label='date_time'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, imaplib.Time2Internaldate(self.input(0)))
        