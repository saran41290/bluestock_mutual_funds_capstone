import requests
from bs4 import BeautifulSoup
def decode_secret_message(inp_doc_url):
  print(f"Decoding secret message from: {inp_doc_url}")
  #download the google doc
  response=requests.get(inp_doc_url)
  response.raise_for_status()

  #Parse the HTML
  soup = BeautifulSoup(response.text, "html.parser")
  
 # Find the first table
  table = soup.find("table")
  if table is None:
      raise ValueError("No table found in document.")
  rows = table.find_all("tr")
  data = []
  max_x = 0
  max_y = 0

  # Skip header row
  for row in rows[1:]:
      cols = [c.get_text(strip=True) for c in row.find_all(["td", "th"])]
      if len(cols) != 3:
          continue

      try:
          x = int(cols[0])
          char = cols[1]
          y = int(cols[2])

          data.append((x, y, char))
          max_x = max(max_x, x)
          max_y = max(max_y, y)
      except ValueError:
          continue

  # Create empty grid
  grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]

  # Place characters
  for x, y, char in data:
      grid[y][x] = char

  # Print the grid
  for row in grid:
      print("".join(row))
  

# Example usage
inp_doc_url = "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"
decode_secret_message(inp_doc_url)