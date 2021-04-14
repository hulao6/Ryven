import ryvencore_qt as rc
import operator


class AutoNode_operator___abs__(rc.Node):
    title = '__abs__'
    description = '''Same as abs(a).'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.__abs__(self.input(0)))
        


class AutoNode_operator___add__(rc.Node):
    title = '__add__'
    description = '''Same as a + b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.__add__(self.input(0), self.input(1)))
        


class AutoNode_operator___and__(rc.Node):
    title = '__and__'
    description = '''Same as a & b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.__and__(self.input(0), self.input(1)))
        


class AutoNode_operator___concat__(rc.Node):
    title = '__concat__'
    description = '''Same as a + b, for a and b sequences.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.__concat__(self.input(0), self.input(1)))
        


class AutoNode_operator___contains__(rc.Node):
    title = '__contains__'
    description = '''Same as b in a (note reversed operands).'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.__contains__(self.input(0), self.input(1)))
        


class AutoNode_operator___delitem__(rc.Node):
    title = '__delitem__'
    description = '''Same as del a[b].'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.__delitem__(self.input(0), self.input(1)))
        


class AutoNode_operator___eq__(rc.Node):
    title = '__eq__'
    description = '''Same as a == b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.__eq__(self.input(0), self.input(1)))
        


class AutoNode_operator___floordiv__(rc.Node):
    title = '__floordiv__'
    description = '''Same as a // b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.__floordiv__(self.input(0), self.input(1)))
        


class AutoNode_operator___ge__(rc.Node):
    title = '__ge__'
    description = '''Same as a >= b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.__ge__(self.input(0), self.input(1)))
        


class AutoNode_operator___getitem__(rc.Node):
    title = '__getitem__'
    description = '''Same as a[b].'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.__getitem__(self.input(0), self.input(1)))
        


class AutoNode_operator___gt__(rc.Node):
    title = '__gt__'
    description = '''Same as a > b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.__gt__(self.input(0), self.input(1)))
        


class AutoNode_operator___iadd__(rc.Node):
    title = '__iadd__'
    description = '''Same as a += b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.__iadd__(self.input(0), self.input(1)))
        


class AutoNode_operator___iand__(rc.Node):
    title = '__iand__'
    description = '''Same as a &= b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.__iand__(self.input(0), self.input(1)))
        


class AutoNode_operator___iconcat__(rc.Node):
    title = '__iconcat__'
    description = '''Same as a += b, for a and b sequences.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.__iconcat__(self.input(0), self.input(1)))
        


class AutoNode_operator___ifloordiv__(rc.Node):
    title = '__ifloordiv__'
    description = '''Same as a //= b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.__ifloordiv__(self.input(0), self.input(1)))
        


class AutoNode_operator___ilshift__(rc.Node):
    title = '__ilshift__'
    description = '''Same as a <<= b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.__ilshift__(self.input(0), self.input(1)))
        


class AutoNode_operator___imatmul__(rc.Node):
    title = '__imatmul__'
    description = '''Same as a @= b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.__imatmul__(self.input(0), self.input(1)))
        


class AutoNode_operator___imod__(rc.Node):
    title = '__imod__'
    description = '''Same as a %= b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.__imod__(self.input(0), self.input(1)))
        


class AutoNode_operator___imul__(rc.Node):
    title = '__imul__'
    description = '''Same as a *= b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.__imul__(self.input(0), self.input(1)))
        


class AutoNode_operator___index__(rc.Node):
    title = '__index__'
    description = '''Same as a.__index__()'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.__index__(self.input(0)))
        


class AutoNode_operator___inv__(rc.Node):
    title = '__inv__'
    description = '''Same as ~a.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.__inv__(self.input(0)))
        


class AutoNode_operator___invert__(rc.Node):
    title = '__invert__'
    description = '''Same as ~a.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.__invert__(self.input(0)))
        


class AutoNode_operator___ior__(rc.Node):
    title = '__ior__'
    description = '''Same as a |= b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.__ior__(self.input(0), self.input(1)))
        


class AutoNode_operator___ipow__(rc.Node):
    title = '__ipow__'
    description = '''Same as a **= b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.__ipow__(self.input(0), self.input(1)))
        


class AutoNode_operator___irshift__(rc.Node):
    title = '__irshift__'
    description = '''Same as a >>= b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.__irshift__(self.input(0), self.input(1)))
        


class AutoNode_operator___isub__(rc.Node):
    title = '__isub__'
    description = '''Same as a -= b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.__isub__(self.input(0), self.input(1)))
        


class AutoNode_operator___itruediv__(rc.Node):
    title = '__itruediv__'
    description = '''Same as a /= b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.__itruediv__(self.input(0), self.input(1)))
        


class AutoNode_operator___ixor__(rc.Node):
    title = '__ixor__'
    description = '''Same as a ^= b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.__ixor__(self.input(0), self.input(1)))
        


class AutoNode_operator___le__(rc.Node):
    title = '__le__'
    description = '''Same as a <= b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.__le__(self.input(0), self.input(1)))
        


class AutoNode_operator___lshift__(rc.Node):
    title = '__lshift__'
    description = '''Same as a << b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.__lshift__(self.input(0), self.input(1)))
        


class AutoNode_operator___lt__(rc.Node):
    title = '__lt__'
    description = '''Same as a < b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.__lt__(self.input(0), self.input(1)))
        


class AutoNode_operator___matmul__(rc.Node):
    title = '__matmul__'
    description = '''Same as a @ b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.__matmul__(self.input(0), self.input(1)))
        


class AutoNode_operator___mod__(rc.Node):
    title = '__mod__'
    description = '''Same as a % b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.__mod__(self.input(0), self.input(1)))
        


class AutoNode_operator___mul__(rc.Node):
    title = '__mul__'
    description = '''Same as a * b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.__mul__(self.input(0), self.input(1)))
        


class AutoNode_operator___ne__(rc.Node):
    title = '__ne__'
    description = '''Same as a != b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.__ne__(self.input(0), self.input(1)))
        


class AutoNode_operator___neg__(rc.Node):
    title = '__neg__'
    description = '''Same as -a.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.__neg__(self.input(0)))
        


class AutoNode_operator___not__(rc.Node):
    title = '__not__'
    description = '''Same as not a.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.__not__(self.input(0)))
        


class AutoNode_operator___or__(rc.Node):
    title = '__or__'
    description = '''Same as a | b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.__or__(self.input(0), self.input(1)))
        


class AutoNode_operator___pos__(rc.Node):
    title = '__pos__'
    description = '''Same as +a.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.__pos__(self.input(0)))
        


class AutoNode_operator___pow__(rc.Node):
    title = '__pow__'
    description = '''Same as a ** b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.__pow__(self.input(0), self.input(1)))
        


class AutoNode_operator___rshift__(rc.Node):
    title = '__rshift__'
    description = '''Same as a >> b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.__rshift__(self.input(0), self.input(1)))
        


class AutoNode_operator___setitem__(rc.Node):
    title = '__setitem__'
    description = '''Same as a[b] = c.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
rc.NodeInputBP(label='c'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.__setitem__(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_operator___sub__(rc.Node):
    title = '__sub__'
    description = '''Same as a - b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.__sub__(self.input(0), self.input(1)))
        


class AutoNode_operator___truediv__(rc.Node):
    title = '__truediv__'
    description = '''Same as a / b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.__truediv__(self.input(0), self.input(1)))
        


class AutoNode_operator___xor__(rc.Node):
    title = '__xor__'
    description = '''Same as a ^ b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.__xor__(self.input(0), self.input(1)))
        


class AutoNode_operator__abs(rc.Node):
    title = '_abs'
    description = '''Return the absolute value of the argument.'''
    init_inputs = [
        rc.NodeInputBP(label='x'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator._abs(self.input(0)))
        


class AutoNode_operator_abs(rc.Node):
    title = 'abs'
    description = '''Same as abs(a).'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.abs(self.input(0)))
        


class AutoNode_operator_add(rc.Node):
    title = 'add'
    description = '''Same as a + b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.add(self.input(0), self.input(1)))
        


class AutoNode_operator_and_(rc.Node):
    title = 'and_'
    description = '''Same as a & b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.and_(self.input(0), self.input(1)))
        


class AutoNode_operator_concat(rc.Node):
    title = 'concat'
    description = '''Same as a + b, for a and b sequences.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.concat(self.input(0), self.input(1)))
        


class AutoNode_operator_contains(rc.Node):
    title = 'contains'
    description = '''Same as b in a (note reversed operands).'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.contains(self.input(0), self.input(1)))
        


class AutoNode_operator_countOf(rc.Node):
    title = 'countOf'
    description = '''Return the number of times b occurs in a.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.countOf(self.input(0), self.input(1)))
        


class AutoNode_operator_delitem(rc.Node):
    title = 'delitem'
    description = '''Same as del a[b].'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.delitem(self.input(0), self.input(1)))
        


class AutoNode_operator_eq(rc.Node):
    title = 'eq'
    description = '''Same as a == b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.eq(self.input(0), self.input(1)))
        


class AutoNode_operator_floordiv(rc.Node):
    title = 'floordiv'
    description = '''Same as a // b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.floordiv(self.input(0), self.input(1)))
        


class AutoNode_operator_ge(rc.Node):
    title = 'ge'
    description = '''Same as a >= b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.ge(self.input(0), self.input(1)))
        


class AutoNode_operator_getitem(rc.Node):
    title = 'getitem'
    description = '''Same as a[b].'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.getitem(self.input(0), self.input(1)))
        


class AutoNode_operator_gt(rc.Node):
    title = 'gt'
    description = '''Same as a > b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.gt(self.input(0), self.input(1)))
        


class AutoNode_operator_iadd(rc.Node):
    title = 'iadd'
    description = '''Same as a += b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.iadd(self.input(0), self.input(1)))
        


class AutoNode_operator_iand(rc.Node):
    title = 'iand'
    description = '''Same as a &= b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.iand(self.input(0), self.input(1)))
        


class AutoNode_operator_iconcat(rc.Node):
    title = 'iconcat'
    description = '''Same as a += b, for a and b sequences.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.iconcat(self.input(0), self.input(1)))
        


class AutoNode_operator_ifloordiv(rc.Node):
    title = 'ifloordiv'
    description = '''Same as a //= b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.ifloordiv(self.input(0), self.input(1)))
        


class AutoNode_operator_ilshift(rc.Node):
    title = 'ilshift'
    description = '''Same as a <<= b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.ilshift(self.input(0), self.input(1)))
        


class AutoNode_operator_imatmul(rc.Node):
    title = 'imatmul'
    description = '''Same as a @= b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.imatmul(self.input(0), self.input(1)))
        


class AutoNode_operator_imod(rc.Node):
    title = 'imod'
    description = '''Same as a %= b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.imod(self.input(0), self.input(1)))
        


class AutoNode_operator_imul(rc.Node):
    title = 'imul'
    description = '''Same as a *= b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.imul(self.input(0), self.input(1)))
        


class AutoNode_operator_index(rc.Node):
    title = 'index'
    description = '''Same as a.__index__()'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.index(self.input(0)))
        


class AutoNode_operator_indexOf(rc.Node):
    title = 'indexOf'
    description = '''Return the first index of b in a.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.indexOf(self.input(0), self.input(1)))
        


class AutoNode_operator_inv(rc.Node):
    title = 'inv'
    description = '''Same as ~a.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.inv(self.input(0)))
        


class AutoNode_operator_invert(rc.Node):
    title = 'invert'
    description = '''Same as ~a.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.invert(self.input(0)))
        


class AutoNode_operator_ior(rc.Node):
    title = 'ior'
    description = '''Same as a |= b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.ior(self.input(0), self.input(1)))
        


class AutoNode_operator_ipow(rc.Node):
    title = 'ipow'
    description = '''Same as a **= b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.ipow(self.input(0), self.input(1)))
        


class AutoNode_operator_irshift(rc.Node):
    title = 'irshift'
    description = '''Same as a >>= b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.irshift(self.input(0), self.input(1)))
        


class AutoNode_operator_is_(rc.Node):
    title = 'is_'
    description = '''Same as a is b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.is_(self.input(0), self.input(1)))
        


class AutoNode_operator_is_not(rc.Node):
    title = 'is_not'
    description = '''Same as a is not b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.is_not(self.input(0), self.input(1)))
        


class AutoNode_operator_isub(rc.Node):
    title = 'isub'
    description = '''Same as a -= b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.isub(self.input(0), self.input(1)))
        


class AutoNode_operator_itruediv(rc.Node):
    title = 'itruediv'
    description = '''Same as a /= b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.itruediv(self.input(0), self.input(1)))
        


class AutoNode_operator_ixor(rc.Node):
    title = 'ixor'
    description = '''Same as a ^= b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.ixor(self.input(0), self.input(1)))
        


class AutoNode_operator_le(rc.Node):
    title = 'le'
    description = '''Same as a <= b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.le(self.input(0), self.input(1)))
        


class AutoNode_operator_length_hint(rc.Node):
    title = 'length_hint'
    description = '''Return an estimate of the number of items in obj.

This is useful for presizing containers when building from an iterable.

If the object supports len(), the result will be exact.
Otherwise, it may over- or under-estimate by an arbitrary amount.
The result will be an integer >= 0.'''
    init_inputs = [
        rc.NodeInputBP(label='obj'),
rc.NodeInputBP(label='default'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.length_hint(self.input(0), self.input(1)))
        


class AutoNode_operator_lshift(rc.Node):
    title = 'lshift'
    description = '''Same as a << b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.lshift(self.input(0), self.input(1)))
        


class AutoNode_operator_lt(rc.Node):
    title = 'lt'
    description = '''Same as a < b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.lt(self.input(0), self.input(1)))
        


class AutoNode_operator_matmul(rc.Node):
    title = 'matmul'
    description = '''Same as a @ b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.matmul(self.input(0), self.input(1)))
        


class AutoNode_operator_mod(rc.Node):
    title = 'mod'
    description = '''Same as a % b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.mod(self.input(0), self.input(1)))
        


class AutoNode_operator_mul(rc.Node):
    title = 'mul'
    description = '''Same as a * b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.mul(self.input(0), self.input(1)))
        


class AutoNode_operator_ne(rc.Node):
    title = 'ne'
    description = '''Same as a != b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.ne(self.input(0), self.input(1)))
        


class AutoNode_operator_neg(rc.Node):
    title = 'neg'
    description = '''Same as -a.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.neg(self.input(0)))
        


class AutoNode_operator_not_(rc.Node):
    title = 'not_'
    description = '''Same as not a.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.not_(self.input(0)))
        


class AutoNode_operator_or_(rc.Node):
    title = 'or_'
    description = '''Same as a | b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.or_(self.input(0), self.input(1)))
        


class AutoNode_operator_pos(rc.Node):
    title = 'pos'
    description = '''Same as +a.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.pos(self.input(0)))
        


class AutoNode_operator_pow(rc.Node):
    title = 'pow'
    description = '''Same as a ** b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.pow(self.input(0), self.input(1)))
        


class AutoNode_operator_rshift(rc.Node):
    title = 'rshift'
    description = '''Same as a >> b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.rshift(self.input(0), self.input(1)))
        


class AutoNode_operator_setitem(rc.Node):
    title = 'setitem'
    description = '''Same as a[b] = c.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
rc.NodeInputBP(label='c'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.setitem(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_operator_sub(rc.Node):
    title = 'sub'
    description = '''Same as a - b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.sub(self.input(0), self.input(1)))
        


class AutoNode_operator_truediv(rc.Node):
    title = 'truediv'
    description = '''Same as a / b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.truediv(self.input(0), self.input(1)))
        


class AutoNode_operator_truth(rc.Node):
    title = 'truth'
    description = '''Return True if a is true, False otherwise.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.truth(self.input(0)))
        


class AutoNode_operator_xor(rc.Node):
    title = 'xor'
    description = '''Same as a ^ b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, operator.xor(self.input(0), self.input(1)))
        