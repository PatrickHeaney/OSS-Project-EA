from plantuml import PlantUML
import os

# Define the PlantUML server URL
plantuml_server = PlantUML(url='http://www.plantuml.com/plantuml/svg/')

# Define the PlantUML diagram
uml_code = """
@startuml
title Open Source Software (OSS) Project Architecture

package "Frontend" {
    [Web Application]
}

package "Backend" {
    [API Server]
    [Database]
}

package "CI/CD" {
    [Jenkins]
    [GitHub Actions]
}

[Web Application] --> [API Server]
[API Server] --> [Database]
[GitHub Actions] --> [API Server]
[Jenkins] --> [API Server]

@enduml
"""

# Generate the diagram and save it to a file
output_file = 'diagram.svg'
plantuml_server.process(uml_code, outfile=output_file)

# Open the generated diagram
os.startfile(output_file)
