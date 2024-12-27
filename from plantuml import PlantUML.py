from plantuml import PlantUML
import os

# Define the PlantUML server URL
plantuml_server = PlantUML(url='http://www.plantuml.com/plantuml/svg/')

# Read the PlantUML diagram from the file
with open('osspa.plantuml', 'r') as file:
    uml_code = file.read()

# Generate the diagram and save it to a file
output_file = 'diagram.svg'
plantuml_server.process(uml_code, outfile=output_file)

# Open the generated diagram
os.startfile(output_file)
