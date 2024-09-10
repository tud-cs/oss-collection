import yaml 
from lxml import etree, html

def generate_html_from_yaml(oss_projects_file, cs_groups_file, html_file, output_file):
    # Parse the existing HTML file
    with open(html_file, "r", encoding="utf-8") as f:
        tree = html.parse(f)
    root = tree.getroot()

    # Find the <div> element with id "project-list"
    project_list = root.find(".//div[@id='project-list']")
    
    # Parse the YAML data of projects
    with open(oss_projects_file, "r") as f:
        projects = yaml.load(f, Loader=yaml.Loader)

    # Parse the YAML data of cs groups
    with open(cs_groups_file, "r") as f:
        cs_groups = yaml.load(f, Loader=yaml.Loader)

    licences = set()
    groups = set()

    # sort projects by involvement
    projects_with_involvement = []
    projects_without_involvement = []
    for project in projects:
        involved = project.get("involved", "")
        # Assume N/A is involved
        if involved == False:
            projects_without_involvement.append(project)
        else:
            projects_with_involvement.append(project)

    # Sort projects by name
    projects_with_involvement = sorted(projects_with_involvement, key=lambda x: x.get("name").lower())
    projects_without_involvement = sorted(projects_without_involvement, key=lambda x: x.get("name").lower())

    projects = projects_with_involvement + projects_without_involvement

    no_longer_involved_start = len(projects_with_involvement)
    
    # Generate HTML items for each project
    for i, project in enumerate(projects):
        if i == no_longer_involved_start:
            no_longer_involved = etree.Element("h2", attrib={"class": "no-longer-involved-header"}, id="no-longer-involved")
            no_longer_involved.text = "Projects where the research group is no longer involved"
            project_list.append(no_longer_involved)

        project_name = project.get("name")
        if not project_name:
            continue
        
        # Create project div
        project_item = etree.Element("div", id=str(i), attrib={"class": "project"})
        
        project_main = etree.SubElement(project_item, "div", attrib={"class": "project-main"})
        project_main_left = etree.SubElement(project_main, "div", attrib={"class": "project-main-left"})
        
        involved = project.get("involved", "")
        if involved == False:
            not_involved = etree.SubElement(project_main_left, "span", attrib={"class": "not-involved"})
            not_involved.text = "no longer involved"
        
        # CS group information
        cs_group_handles = project.get("groups")
        if cs_group_handles:
            for group_handle in cs_group_handles:
                group = None
                for cs_group in cs_groups:
                    if cs_group.get("handle") == group_handle:
                        group = cs_group
                        break

                if group:
                    project_group = etree.SubElement(project_main_left, "div", attrib={"class": "project-chair"})
                    group_name = group.get("name")
                    groups.add(group_name)
                    group_link = group.get("website")
                    
                    chair = etree.SubElement(project_group, "a", attrib={"class": "chair"})
                    chair_name_span = etree.SubElement(chair, "span", attrib={"class": "chair-name"})
                    chair_name_span.text = group_name

                    if group_link:
                        chair.set("href", group_link)
                        chair.set("target", "_blank")
                        chair.set("title", group_link)
                        
                        etree.SubElement(chair, "img", attrib={"class": "chair-link-img"}, src="images/external-link-svgrepo-com-grey.svg", style="height: 16px")    

        # Project name and more info
        project_row = etree.SubElement(project_main_left, "div", attrib={"class": "project-row", "onclick": f"popUp({i})"})
        project_name_div = etree.SubElement(project_row, "div", attrib={"class": "project-name"}, id=f"project-name-{i}")
        project_name_div.text = project_name
        
        project_more_info_text = project.get("description")
        if project_more_info_text:      
            project_more_info_popup = etree.SubElement(project_main_left, "div", attrib={"class": "project-more-info-popup"}, id=f"more-info-{i}", title = project_more_info_text)
            project_more_info_popup.text = project_more_info_text
        
        # Project tags
        project_tags = etree.SubElement(project_main_left, "div", attrib={"class": "project-tags"})
        roles = {"Founder": "founder", 
                 "Maintainer": "maintainer", 
                 "Contributor": "contributor"}
        
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
        
        project_site = project.get("website")
        if project_site:
            link_item = etree.SubElement(link_footer_left, "a", attrib={"class": "link-item"}, title=project_site, href=project_site, target="_blank")
            link_item_text = etree.SubElement(link_item, "span", attrib={"class": "link-item-text"})
            link_item_text.text = "Project Site"
            link_item_icon = etree.SubElement(link_item, "img", src="images/external-link-svgrepo-com-white.svg", style="height: 20px")
        
        repository = project.get("repository")
        if repository:
            link_item = etree.SubElement(link_footer_left, "a", attrib={"class": "link-item"}, title=repository, href=repository, target="_blank")
            link_item_text = etree.SubElement(link_item, "span", attrib={"class": "link-item-text"})
            link_item_text.text = "Code"
            link_item_icon = etree.SubElement(link_item, "img", src="images/external-link-svgrepo-com-white.svg", style="height: 20px")
        
        # License
        license = project.get("license")
        if license:
            licences.add(license)
            license_item = etree.SubElement(link_footer, "div", attrib={"class": "license-item"}, title=license, id=f"license-{i}")
            license_item.text = license
        
        project_list.append(project_item)
    
    # Add chair and license filters
    chair_filter = root.find(".//select[@id='chair']")
    if chair_filter is not None:
        for chair in sorted(groups):
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

generate_html_from_yaml("oss-projects.yaml", "cs-groups.yaml", "website/base.html", "website/index.html")
