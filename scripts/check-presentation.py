from pathlib import Path
from PIL import Image, ImageOps, ImageDraw
from pypdf import PdfReader

root = Path(__file__).resolve().parents[1]
pages = sorted((root / 'tmp/pdfs').glob('page-*.png'))
assert len(pages) == 12
sheet = Image.new('RGB', (1500, 1360), '#bbbbbb')
for index, path in enumerate(pages):
    image = Image.open(path).convert('RGB')
    image.thumbnail((490, 310))
    x, y = (index % 3) * 500, (index // 3) * 340
    sheet.paste(image, (x, y))
    ImageDraw.Draw(sheet).text((x + 10, y + 315), str(index + 1), fill='black')
sheet.save(root / 'tmp/pdfs/contact.png')
pdf = PdfReader(root / 'output/pdf/Web3-Carnival-Design-Presentation.pdf')
assert len(pdf.pages) == 12
print('PDF: 12 pages, text lengths:', [len(p.extract_text()) for p in pdf.pages])
