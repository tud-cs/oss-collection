import yaml 
from lxml import etree, html

def generate_html_from_yaml(yaml_file, html_file, output_file):
    # Parse the existing HTML file
    with open(html_file, "r", encoding="utf-8") as f:
        tree = html.parse(f)
    root = tree.getroot()

    # Find the <div> element with id "project-list"
    project_list = root.find(".//div[@id='project-list']")
    
    # Parse the YAML data
    with open(yaml_file, "r") as f:
        projects = yaml.load(f, Loader=yaml.Loader)

    licences = set()
    chairs = set()

    # sort projects by involvement
    projects_with_involvement = []
    projects_without_involvement = []
    for project in projects:
        involved = project.get("Are you still involved?", "")
        # Assume N/A is involved
        if involved == False:
            projects_without_involvement.append(project)
        else:
            projects_with_involvement.append(project)

    # Sort projects by name
    projects_with_involvement = sorted(projects_with_involvement, key=lambda x: x.get("Name of the open source project").lower())
    projects_without_involvement = sorted(projects_without_involvement, key=lambda x: x.get("Name of the open source project").lower())

    projects = projects_with_involvement + projects_without_involvement

    no_longer_involved_start = len(projects_with_involvement)
    
    # Generate HTML items for each project
    for i, project in enumerate(projects):
        if i == no_longer_involved_start:
            no_longer_involved = etree.Element("h2", attrib={"class": "no-longer-involved-header"}, id="no-longer-involved")
            no_longer_involved.text = "Projects where the research group is no longer involved"
            project_list.append(no_longer_involved)

        project_name = project.get("Name of the open source project")
        if not project_name:
            continue
        
        # Create project div
        project_item = etree.Element("div", id=str(i), attrib={"class": "project"})
        
        project_main = etree.SubElement(project_item, "div", attrib={"class": "project-main"})
        project_main_left = etree.SubElement(project_main, "div", attrib={"class": "project-main-left"})
        
        # Chair information
        chair_name = project.get("To which Chair do you belong to at the Faculty of Computer Science?")
        if chair_name:
            project_chair = etree.SubElement(project_main_left, "div", attrib={"class": "project-chair"})
            chairs.add(chair_name)
            chair_link = project.get("URL to the chair")
            
            chair = etree.SubElement(project_chair, "a", attrib={"class": "chair"})
            chair_name_span = etree.SubElement(chair, "span", id=f"chair-{i}")
            chair_name_span.text = chair_name

            if chair_link:
                chair.set("href", chair_link)
                chair.set("target", "_blank")
                chair.set("title", chair_link)
                
                etree.SubElement(chair, "img", attrib={"class": "chair-link-img"}, src="images/external-link-svgrepo-com-grey.svg", style="height: 16px")
        
            involved = project.get("Are you still involved?", "")
            if involved == False:
                not_involved = etree.SubElement(project_chair, "span", attrib={"class": "not-involved"})
                not_involved.text = "- no longer involved"
        
        # Project name and more info
        project_row = etree.SubElement(project_main_left, "div", attrib={"class": "project-row", "onclick": f"popUp({i})"})
        project_name_div = etree.SubElement(project_row, "div", attrib={"class": "project-name"}, id=f"project-name-{i}")
        project_name_div.text = project_name
        
        project_more_info_text = project.get("Anything else you want to let us know?")
        if project_more_info_text:      
            project_more_info_popup = etree.SubElement(project_main_left, "div", attrib={"class": "project-more-info-popup"}, id=f"more-info-{i}", title = project_more_info_text)
            project_more_info_popup.text = project_more_info_text
        
        # Project tags
        project_tags = etree.SubElement(project_main_left, "div", attrib={"class": "project-tags"})
        roles = {"Founder": "Your role in the open source project? [Founder]", 
                 "Maintainer": "Your role in the open source project? [Maintainer]", 
                 "Contributor": "Your role in the open source project? [Contributor]"}
        
        for role, key in roles.items():
            if project.get(key) == True: 
                tag = etree.SubElement(project_tags, "span", attrib={"class": f"tag {role.lower()}"})
                tag.text = role
        
        project_main.append(project_main_left)

        # Project image
        img_src = f"images/projects/{project['image']}" if project.get("image") else ""
        if img_src:
            img = etree.SubElement(project_main, "img", src=img_src, attrib={"class": "project-logo"})

        project_item.append(project_main)
        
        # Link footer
        link_footer = etree.SubElement(project_item, "div", attrib={"class": "link-footer"})
        link_footer_left = etree.SubElement(link_footer, "div", attrib={"class": "link-footer-left"})
        
        project_site = project.get("URL of the open source project")
        if project_site:
            link_item = etree.SubElement(link_footer_left, "a", attrib={"class": "link-item"}, title=project_site, href=project_site, target="_blank")
            link_item_text = etree.SubElement(link_item, "span", attrib={"class": "link-item-text"})
            link_item_text.text = "Project Site"
            link_item_icon = etree.SubElement(link_item, "img", src="images/external-link-svgrepo-com-white.svg", style="height: 20px")
        
        repository = project.get("URL of the public repository")
        if repository:
            link_item = etree.SubElement(link_footer_left, "a", attrib={"class": "link-item"}, title=repository, href=repository, target="_blank")
            link_item_text = etree.SubElement(link_item, "span", attrib={"class": "link-item-text"})
            link_item_text.text = "Code"
            link_item_icon = etree.SubElement(link_item, "img", src="images/external-link-svgrepo-com-white.svg", style="height: 20px")
        
        # License
        license = project.get("License under which the open source project is available")
        if license:
            licences.add(license)
            license_item = etree.SubElement(link_footer, "div", attrib={"class": "license-item"}, title=license, id=f"license-{i}")
            license_item.text = license
        
        project_list.append(project_item)
    
    # Add chair and license filters
    chair_filter = root.find(".//select[@id='chair']")
    if chair_filter is not None:
        for chair in sorted(chairs):
            option = etree.SubElement(chair_filter, "option", value=chair)
            option.text = chair

    license_filter = root.find(".//select[@id='license']")
    if license_filter is not None:
        for license in sorted(licences):
            option = etree.SubElement(license_filter, "option", value=license)
            option.text = license

    etree.indent(root)    
    # Write the modified HTML back to a file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("<!DOCTYPE html>\n")
        f.write(etree.tostring(root, pretty_print=True, encoding="unicode", method='html'))

generate_html_from_yaml("projects.yaml", "website/base.html", "website/index.html")
