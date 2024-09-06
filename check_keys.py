import yaml

PROJECT_NAME_KEY = "Name of the open source project"

REQUIRED_KEYS = {
    "To which Chair do you belong to at the Faculty of Computer Science?": str,
    PROJECT_NAME_KEY: str, 
    "Your role in the open source project? [Founder]": bool, 
    "Your role in the open source project? [Maintainer]": bool,
    "Your role in the open source project? [Contributor]": bool, 
    "Are you still involved?": bool,
    "Anything else you want to let us know?": str,
}

OPTIONAL_KEYS = {
    "License under which the open source project is available": str,
    "URL of the open source project": str,
    "URL of the public repository": str,
    "URL to the chair": str,
    "image": str
}

with open("projects.yaml", "r") as f:
    data = yaml.load(f, Loader=yaml.Loader)

problems = {}

missing_key = "Missing key:"
value_error = "value error:"

for idx, project in enumerate(data):
    for key in REQUIRED_KEYS:
        if key not in project:
            if idx not in problems:
                problems[idx] = [missing_key + key]
            else:
                problems[idx].append(missing_key + key)
        else:
            if not isinstance(project[key], REQUIRED_KEYS[key]):
                    if idx not in problems:
                        problems[idx] = [f"[{key}] {value_error} expected {REQUIRED_KEYS[key].__name__}"]
                    else:
                        problems[idx].append(f"[{key}] {value_error} expected {REQUIRED_KEYS[key].__name__}")
            if isinstance(project[key], str):
                if len(project[key]) == 0:
                    if idx not in problems:
                        problems[idx] = [f"[{key}] {value_error} expected non-empty string"]
                    else:
                        problems[idx].append(f"[{key}] {value_error} expected non-empty string")
    
    for key in OPTIONAL_KEYS:
        if key in project:
            if not isinstance(project[key], OPTIONAL_KEYS[key]):
                if idx not in problems:
                    problems[idx] = [f"(Optional Key) [{key}] {value_error} expected {OPTIONAL_KEYS[key].__name__}"]
                else:
                    problems[idx].append(f"(Optional Key) [{key}] {value_error} expected {OPTIONAL_KEYS[key].__name__}")
            if isinstance(project[key], str):
                if len(project[key]) == 0:
                    if idx not in problems:
                        problems[idx] = [f"(Optional Key) [{key}] {value_error} expected non-empty string"]
                    else:
                        problems[idx].append(f"(Optional Key) [{key}] {value_error} expected non-empty string")

summary = "# Check of projects.yaml file\n"

if len(problems) == 0:
    summary += "✅ No problems found"
    print(summary)
else:
    summary += "❌ Missing keys in yaml\n"
    summary += "| Project index | Project name (if available) | Problems |\n"
    summary += "| ------------- | --------------------------- | -------- |\n"
    for project_idx, keys in problems.items():
        if PROJECT_NAME_KEY not in keys:
            project_name = data[project_idx][PROJECT_NAME_KEY]
        else:
            project_name = "N/A"
        summary += f"| {project_idx} | {project_name} | {', '.join(keys)} |\n"
    
    print(summary)
    raise KeyError("Required keys (information about the open source project) are missing in projects.yaml.")
        
            
