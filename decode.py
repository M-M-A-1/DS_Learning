import requests
from bs4 import BeautifulSoup
import re

def decode_secret_message(url):
    response = requests.get(url)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    table = soup.find('table')
    
    if not table:
        print("No table found in the document")
        return
    
    rows = table.find_all('tr')
    
    char_positions = {}
    
    for row in rows:
        cells = row.find_all('td')
        
        if len(cells) >= 3:
            try:
                x_text = cells[0].get_text().strip()
                x = int(x_text)
                
                char = cells[1].get_text().strip()
                
                y_text = cells[2].get_text().strip()
                y = int(y_text)
                
                char_positions[(x, y)] = char
                
            except (ValueError, IndexError):
                continue
    
    if not char_positions:
        print("No character data found in the document")
        return
    
    max_x = max(pos[0] for pos in char_positions.keys())
    max_y = max(pos[1] for pos in char_positions.keys())

    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    
    for (x, y), char in char_positions.items():
        grid[y][x] = char
    
    for row in grid:
        print(''.join(row))

url = "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"
decode_secret_message(url)