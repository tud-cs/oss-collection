import yaml

def generate_markdown_from_yaml(oss_projects_file, cs_groups_file, markdown_file, output_file):
    # Open the existing markdown file
    with open(markdown_file, "r", encoding="utf-8") as f:
        markdown_content = f.read() 
    
    # Parse the yaml data of projects
    with open(oss_projects_file, "r") as f:
        projects = yaml.load(f, Loader=yaml.Loader)

    # Parse the yaml data of cs groups
    with open(cs_groups_file, "r") as f:
        cs_groups = yaml.load(f, Loader=yaml.Loader)

    markdown_content += "\n"
    markdown_content += "# Projects"

    project_list = ""

    projects.sort(key=lambda x: x.get("name", "zzzzzz").lower())
    for project in projects:
        project_entry = "### "

        project_name = project.get("name")
        if project_name is None or len(project_name) == 0:
            project_name = "N/A"
        project_entry += project_name 

        project_image = project.get("logo")
        if project_image is not None and len(project_image) != 0:
            project_entry += "\n\n"
            project_entry += f'<img align="right" height="100" src="./website/images/projects/{project_image}">'

        project_entry += "\n\n"
        project_entry += "Research Group: "

        group_handles = project.get("groups")
        if group_handles is None or len(group_handles) == 0:
            project_entry += "N/A "
        else:
            for group_handle in group_handles:
                # find the cs group with the handle
                group = None
                for cs_group in cs_groups:
                    if cs_group.get("handle") == group_handle:
                        group = cs_group
                        break
                
                if group is not None:
                    group_name = group.get("name")
                    if group_name is None or len(group_name) == 0:
                        group_name = "N/A"
                    group_website = group.get("website")
                    if group_website is None or len(group_website) == 0:
                        group_website = "N/A"
                    
                    project_entry += f"[{group_name}]({group_website}) "

        founder = project.get("founder")
        if founder is not None or type(founder)!=bool:
            if founder:
                project_entry += "(Founder) "

        maintainer = project.get("maintainer")
        if maintainer is not None or type(maintainer)!=bool:
            if maintainer:
                project_entry += "(Maintainer) "

        contributor = project.get("contributer")
        if contributor is not None or type(contributor)!=bool:
            if contributor:
                project_entry += "(Contributor) "
        
        involved = project.get("involved", "")
        if involved is not None and type(involved)==bool:
            if not involved:
                project_entry += "- no longer involved"

        project_entry += "\n\n"
        project_entry += "More information: "

        project_more_info_text = project.get("description")
        if project_more_info_text is None or len(project_more_info_text) == 0:
            project_more_info_text = "N/A"
        project_entry += project_more_info_text

        project_entry += "\n\n"
        project_entry += "License: "
        license = project.get("license")
        if license is None or len(license) == 0:
            license = "N/A"
        project_entry += license

        project_entry += "\n\n"

        repository = project.get("repository")
        if repository is not None and len(repository) != 0:
            project_entry += f"[Code]({repository}) "

        project_site = project.get("website")
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

generate_markdown_from_yaml("oss-projects.yaml", "cs-groups.yaml", "README-template.md", "README.md")
