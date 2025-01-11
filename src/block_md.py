# block md functions


# document: a string representing a full md doc
# return a list of strings that is the blocks
def markdown_to_blocks(document):
    blocks = []
    raw =  document.split('\n')
    for b in document.split('\n'):
        if b != '':
            blocks.append(b.strip())





    return blocks 
