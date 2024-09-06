import yaml

def generate_markdown_from_yaml(yaml_file, markdown_file, output_file):
    # Open the existing markdown file
    with open(markdown_file, "r", encoding="utf-8") as f:
        markdown_content = f.read() 
    
    # Parse the yaml data
    with open(yaml_file, "r") as f:
        projects = yaml.load(f, Loader=yaml.Loader)

    markdown_content += "\n"
    markdown_content += "# Projects"

    project_list = ""

    projects.sort(key=lambda x: x.get("Name of the open source project", "zzzzzz").lower())
    for project in projects:
        project_entry = "### "

        project_name = project.get("Name of the open source project")
        if project_name is None or len(project_name) == 0:
            project_name = "N/A"
        project_entry += project_name 

        project_image = project.get("image")
        if project_image is not None and len(project_image) != 0:
            project_entry += "\n\n"
            project_entry += f'<img align="right" height="100" src="./website/images/projects/{project_image}">'

        project_entry += "\n\n"
        project_entry += "Research Group: "

        chair_name = project.get("To which Chair do you belong to at the Faculty of Computer Science?")
        if chair_name is None or len(chair_name) == 0:
            chair_name = "N/A"

        chair_link = project.get("URL to the chair")
        if chair_link is not None:
            project_entry += f"[{chair_name}]({chair_link}) "
        else:
            project_entry += f"{chair_name} "

        founder = project.get("Your role in the open source project? [Founder]")
        if founder is not None or type(founder)!=bool:
            if founder:
                project_entry += "(Founder) "

        maintainer = project.get("Your role in the open source project? [Maintainer]")
        if maintainer is not None or type(maintainer)!=bool:
            if maintainer:
                project_entry += "(Maintainer) "

        contributor = project.get("Your role in the open source project? [Contributor]")
        if contributor is not None or type(contributor)!=bool:
            if contributor:
                project_entry += "(Contributor) "
        
        involved = project.get("Are you still involved?", "")
        if involved is not None and type(involved)==bool:
            if not involved:
                project_entry += "- no longer involved"

        project_entry += "\n\n"
        project_entry += "More information: "

        project_more_info_text = project.get("Anything else you want to let us know?")
        if project_more_info_text is None or len(project_more_info_text) == 0:
            project_more_info_text = "N/A"
        project_entry += project_more_info_text

        project_entry += "\n\n"
        project_entry += "License: "
        license = project.get("License under which the open source project is available")
        if license is None or len(license) == 0:
            license = "N/A"
        project_entry += license

        project_entry += "\n\n"

        repository = project.get("URL of the public repository")
        if repository is not None and len(repository) != 0:
            project_entry += f"[Code]({repository}) "

        project_site = project.get("URL of the open source project")
        if project_site is not None and len(project_site) != 0:
            project_entry += f"[Project Site]({project_site})"

        project_list += project_entry
        project_list += "\n\n"
        project_list += "---"
        project_list += "\n"

    markdown_content += "\n"
    markdown_content += project_list 

    # Write the modified HTML back to a file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(markdown_content)

generate_markdown_from_yaml("projects.yaml", "README-template.md", "README.md")
