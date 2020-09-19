from writer import Writer
from pen import Pen
from typewriter import Typewriter

writer = Writer('Machado de Assis')
writer2 = Writer('Napoleon Hill')
pen = Pen('Bic')
typewriter = Typewriter()

writer.tool = pen
writer2.tool = typewriter

writer.tool.write()
writer2.tool.write()
