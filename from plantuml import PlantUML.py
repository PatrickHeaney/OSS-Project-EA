import zlib
import base64
import requests
import pyperclip

# Define the PlantUML server URL
plantuml_server = 'http://www.plantuml.com/plantuml/'

# Read the PlantUML diagram from the file
with open('osspa.plantuml', 'r') as file:
    plantuml_text = file.read()

# Encode the UML code
def encode_plantuml(plantuml_text):
    zlibbed_str = zlib.compress(plantuml_text.encode('utf-8'))
    compressed_string = zlibbed_str[2:-4]
    encoded = base64.b64encode(compressed_string).decode('utf-8')
    return encoded.replace('+', '-').replace('/', '_').replace('=', '')

# Get the PlantUML diagram
def get_plantuml_diagram(plantuml_encoded, output_format='svg'):
    api_url = f"{plantuml_server}{output_format}/~1{plantuml_encoded}"
    response = requests.get(api_url)
    return response.content

# Encode the script and get the diagram
encoded_script = encode_plantuml(plantuml_text)
diagram = get_plantuml_diagram(encoded_script)

# Save the diagram to a file
output_file = 'diagram.svg'
with open(output_file, 'wb') as file:
    file.write(diagram)

# Print the URL to render the diagram on a webpage
uml_url = f"{plantuml_server}uml/~1{encoded_script}"
print("View the UML diagram at:", uml_url)

# Copy the URL to the clipboard
pyperclip.copy(uml_url)
print("The URL has been copied to the clipboard.")
