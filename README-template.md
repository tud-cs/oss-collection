# TU Dresden - Computer Science: Open Source Projects

This repository contains functionality to generate a HTML and markdown site of all projects entered in `projects.yaml`.

Run `init_site.py` to generate a static HTML page with an overview of all projects.

Run `init_readme.py` to generate README of this repository containing all projects.

## Add a new project

Keys in `projects.yaml`
| Name | Type | Required? |
|------|------|------|
| `To which Chair do you belong to at the Faculty of Computer Science?` | `string` | ✅ |
| `Name of the open source project` | `string` | ✅ |
| `Your role in the open source project? [Founder]` | `boolean` | ✅ |
| `Your role in the open source project? [Maintainer]` | `boolean` | ✅ |
| `Your role in the open source project? [Contributor]` | `boolean` | ✅ |
| `Are you still involved?` | `boolean` | ✅ |
| `Anything else you want to let us know?` | `string` | ✅ |
| `License under which the open source project is available` | `string` | Optional |
| `URL of the open source project` | `string` | Optional |
| `URL of the public repository` | `string` | Optional |
| `URL to the chair` | `string` | Optional |
| `image` | `string` | Optional |

Append this template to `projcets.yaml` and fill in your data:
```yaml
- To which Chair do you belong to at the Faculty of Computer Science?:  
  URL to the chair: 
  Name of the open source project: 
  URL of the open source project: 
  URL of the public repository: 
  Your role in the open source project? [Founder]: 
  Your role in the open source project? [Maintainer]: 
  Your role in the open source project? [Contributor]: 
  License under which the open source project is available: 
  Are you still involved?: 
  Anything else you want to let us know?: 
  image: 
```

For the image, upload the image to the `images` folder and enter the relative URL to the image in the `images` folder.

