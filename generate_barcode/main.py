from barcode import EAN13
from barcode.writer import ImageWriter

number = '590143215697'

generated_barcode = EAN13(number, writer=ImageWriter())
generated_barcode.save('barcode')