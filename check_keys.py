import yaml

REQUIRED_KEYS_PROJECT = {
    "name": str,
    "description": str, 
    "groups": list, 
    "founder": bool,
    "contributor": bool, 
    "maintainer": bool, 
    "involved": bool,
}

OPTIONAL_KEYS_PROJECT = {
    "license": str,
    "website": str,
    "repository": str,
    "logo": str,
}

REQUIRED_KEYS_GROUP = {
    "name": str,
    "handle": str,
}

OPTIONAL_KEYS_GROUP = {
    "website": str,
}

with open("oss-projects.yaml", "r") as f:
    projects = yaml.load(f, Loader=yaml.Loader)

with open("cs-groups.yaml", "r") as f:
    groups = yaml.load(f, Loader=yaml.Loader)

project_problems = {}
group_problems = {}

missing_key = "Missing key: "
value_error = "value error:"

for idx, project in enumerate(projects):
    for key in REQUIRED_KEYS_PROJECT:
        if key not in project:
            if idx not in project_problems:
                project_problems[idx] = [missing_key + key]
            else:
                project_problems[idx].append(missing_key + key)
        else:
            if not isinstance(project[key], REQUIRED_KEYS_PROJECT[key]):
                    if idx not in project_problems:
                        project_problems[idx] = [f"[{key}] {value_error} expected {REQUIRED_KEYS_PROJECT[key].__name__}"]
                    else:
                        project_problems[idx].append(f"[{key}] {value_error} expected {REQUIRED_KEYS_PROJECT[key].__name__}")
            if isinstance(project[key], str):
                if len(project[key]) == 0:
                    if idx not in project_problems:
                        project_problems[idx] = [f"[{key}] {value_error} expected non-empty string"]
                    else:
                        project_problems[idx].append(f"[{key}] {value_error} expected non-empty string")
    
    for key in OPTIONAL_KEYS_PROJECT:
        if key in project:
            if not isinstance(project[key], OPTIONAL_KEYS_PROJECT[key]):
                if idx not in project_problems:
                    project_problems[idx] = [f"(Optional Key) [{key}] {value_error} expected {OPTIONAL_KEYS_PROJECT[key].__name__}"]
                else:
                    project_problems[idx].append(f"(Optional Key) [{key}] {value_error} expected {OPTIONAL_KEYS_PROJECT[key].__name__}")
            if isinstance(project[key], str):
                if len(project[key]) == 0:
                    if idx not in project_problems:
                        project_problems[idx] = [f"(Optional Key) [{key}] {value_error} expected non-empty string"]
                    else:
                        project_problems[idx].append(f"(Optional Key) [{key}] {value_error} expected non-empty string")

for idx, group in enumerate(groups):
    for key in REQUIRED_KEYS_GROUP:
        if key not in group:
            if idx not in group_problems:
                group_problems[idx] = [missing_key + key]
            else:
                group_problems[idx].append(missing_key + key)
        else:
            if not isinstance(group[key], REQUIRED_KEYS_GROUP[key]):
                if idx not in group_problems:
                    group_problems[idx] = [f"[{key}] {value_error} expected {REQUIRED_KEYS_GROUP[key].__name__}"]
                else:
                    group_problems[idx].append(f"[{key}] {value_error} expected {REQUIRED_KEYS_GROUP[key].__name__}")
            if isinstance(group[key], str):
                if len(group[key]) == 0:
                    if idx not in group_problems:
                        group_problems[idx] = [f"[{key}] {value_error} expected non-empty string"]
                    else:
                        group_problems[idx].append(f"[{key}] {value_error} expected non-empty string")
    
    for key in OPTIONAL_KEYS_GROUP:
        if key in group:
            if not isinstance(group[key], OPTIONAL_KEYS_GROUP[key]):
                if idx not in group_problems:
                    group_problems[idx] = [f"(Optional Key) [{key}] {value_error} expected {OPTIONAL_KEYS_GROUP[key].__name__}"]
                else:
                    group_problems[idx].append(f"(Optional Key) [{key}] {value_error} expected {OPTIONAL_KEYS_GROUP[key].__name__}")
            if isinstance(group[key], str):
                if len(group[key]) == 0:
                    if idx not in group_problems:
                        group_problems[idx] = [f"(Optional Key) [{key}] {value_error} expected non-empty string"]
                    else:
                        group_problems[idx].append(f"(Optional Key) [{key}] {value_error} expected non-empty string")

summary = "# Check of projects.yaml file\n"

if len(project_problems) == 0:
    summary += "✅ No problems in oss-projects yaml found"
    print(summary)
else:
    summary += "❌ Missing keys in oss-projects yaml\n"
    summary += "| Project index | Project name (if available) | Problems |\n"
    summary += "| ------------- | --------------------------- | -------- |\n"
    for project_idx, keys in project_problems.items():
        if "name" not in keys:
            project_name = projects[project_idx]["name"]
        else:
            project_name = "N/A"
        summary += f"| {project_idx} | {project_name} | {', '.join(keys)} |\n"
    
    print(summary)

print("")
summary = "# Check of cs-groups.yaml file\n"

if len(group_problems) == 0:
    summary += "✅ No problems in cs-groups yaml found"
    print(summary)
else:
    summary += "❌ Missing keys in cs-groups yaml\n"
    summary += "| Group index | Group name (if available) | Problems |\n"
    summary += "| ----------- | -------------------------- | -------- |\n"
    for group_idx, keys in group_problems.items():
        if "name" not in keys:
            group_name = groups[group_idx]["name"]
        else:
            group_name = "N/A"
        summary += f"| {group_idx} | {group_name} | {', '.join(keys)} |\n"
    
    print(summary)

if (len(project_problems) != 0) or (len(group_problems) != 0):
    raise KeyError("Required keys (information about the open source project) are missing in oss-projects.yaml or cs-groups.yaml.")
