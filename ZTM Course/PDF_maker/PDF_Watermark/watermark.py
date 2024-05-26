from PyPDF2 import PdfReader,PdfMerger,PdfWriter
import sys

file_to_stamp = sys.argv[1]
file_watermark = sys.argv[2]

def watermark(file,watermark):
  
  reader = PdfReader(file)
  writer = PdfWriter()

  for index in range(len(reader.pages)):
    content_page = reader.pages[index]
    mediabox = content_page.mediabox

    # You need to load it again, as the last time it was overwritten
    reader_stamp = PdfReader(watermark)
    image_page = reader_stamp.pages[0]

    image_page.merge_page(content_page)
    image_page.mediabox = mediabox
    writer.add_page(image_page)

  with open('watermarked.pdf','wb') as output_file:
      writer.write(output_file)

watermark(file_to_stamp,file_watermark)