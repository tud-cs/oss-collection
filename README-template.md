# TU Dresden - Computer Science: Open Source Projects

This repository contains functionality to generate a HTML and markdown site of all projects entered in `oss-projects.yaml` and computer science groups in `cs-groups.yaml`.

Run `init_site.py` to generate a static HTML page with an overview of all projects.

Run `init_readme.py` to generate README of this repository containing all projects.

## Add a new project

Keys in `oss-projects.yaml`
| Name | Type | Required? |
|------|------|------|
| `name` | `string` | ✅ |
| `description` | `string` | ✅ |
| `groups` | `string[]` | ✅ |
| `founder` | `boolean` | ✅ |
| `maintainer` | `boolean` | ✅ |
| `contributer` | `boolean` | ✅ |
| `involved` | `boolean` | ✅ |
| `website` | `string` | Optional |
| `repository` | `string` | Optional |
| `license` | `string` | Optional |
| `logo` | `string` | Optional |

Keys in `cs-groups.yaml`
| Name | Type | Required? |
|------|------|------|
| `name` | `string` | ✅ |
| `handle` | `string` | ✅ |
| `website` | `string` | Optional |

Append this template to `oss-projects.yaml` and fill in your data:
```yaml
- name:
  description:
  website:
  repository:
  license:
  groups: []
  founder:
  maintainer:
  contributer:
  involved:
  logo:
```

For the logo, upload the logo to the `images/projects` folder and enter the relative URL to the logo in the `images/projects` folder.

For the groups add the handle of your computer science group to the list.

If your computer science group does not exist yet, append this template to `cs-groups.yaml` and fill in your data:
```yaml
- name: 
  handle: 
  website: 
```
