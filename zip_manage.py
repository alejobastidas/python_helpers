from io import StringIO, BytesIO
from zipfile import ZipFile, ZIP_DEFLATED

text_stream = StringIO()
text_stream.write("I am a text buffer")
text_stream.write("\n")
text_stream.write("The End")

print(text_stream.getvalue())