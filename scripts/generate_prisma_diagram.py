from PIL import Image, ImageDraw, ImageFont
import os

# Este script gera o diagrama PRISMA como PNG
os.makedirs('protocol', exist_ok=True)

# Configurações
width, height = 800, 550
img = Image.new('RGB', (width, height), 'white')
draw = ImageDraw.Draw(img)

# Fonte padrão
font = ImageFont.load_default()

# Passos do fluxo PRISMA
diagram_steps = [
    ('Identificação', '1137 registros identificados'),
    ('Triagem', '780 avaliados em título-resumo\nExcluídos: 509'),
    ('Elegibilidade', '271 texto completo\nExcluídos: 104'),
    ('Inclusão', '167 estudos incluídos')
]

# Desenhar boxes e setas
y_positions = [0.85, 0.65, 0.45, 0.25]
for (title, info), y in zip(diagram_steps, y_positions):
    x1, x2 = 0.1*width, 0.9*width
    y1, y2 = (y-0.1)*height, (y+0.05)*height
    draw.rectangle([x1, y1, x2, y2], outline='black', width=2)
    draw.text((x1+10, y1+10), f"{title}\n{info}", fill='black', font=font)

# Desenhar setas
for y1, y2 in zip(y_positions[:-1], y_positions[1:]):
    draw.line(
        [(0.5*width, (y1-0.05)*height), (0.5*width, (y2+0.05)*height)],
        fill='black', width=2
    )
    # Cabeça da seta
    head_x, head_y = 0.5*width, (y2+0.05)*height
    draw.polygon([
        (head_x-10, head_y-10),
        (head_x+10, head_y-10),
        (head_x, head_y)
    ], fill='black')

# Salvar imagem
img.save('protocol/prisma_diagrama.png')
