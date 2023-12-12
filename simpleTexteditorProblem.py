implement a simple text editor. The editor intially contains an empty string,
S. Perform Q operatios of the following 4 types:
1. append(W) - Append string W to the end of S.
2. delete(K) - Delete the last k character of S.
3. print(k) - Print the Kth character of S.
4. undo() - Undo the last (not previously undone) operation of type 1 or 2, 
reverting S to the state it was in prior to that operation. 

S = 'abcde'

ops = ['1 fg', '3 6', '2 5', '4', '37', '4', '34']

class TextEditor:
    def __init__(self):
        self.s = ''
        self.operations = []

    def append(self, k):
        self.operation.append(self.s)
        self.s = self.s[:-k]

    def print_kth(self, k):
        print(self.s[k - 1] if 0 < k <= len(self.s) else '')

    def undo(self):
        if self.operations:
            self.s = self.operations.pop()

# Example usage :

text_editor = TextEditor()

ops = ['1 fg', '3 6', '2 5', '4', '3 7', '4', '3 4']


for operation in ops:
    op_type, *args = operation.split()
    if op_type == '1':
        text_editor.append(arg[0])
    elif op_type == '2':
        text_editor.delete(int(args[0]))
    elif op_type == '3':
        text_editor.print_kth(int(args[0]))
    elif op_type == '4':
        text_editor.undo
