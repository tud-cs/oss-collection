# Open Source Projects of the Faculty of Computer Science at TU Dresden

This repository contains scripts and data to generate HTML and markdown files presenting open source software projects of the [Faculty of Computer Science](https://cs.tu-dresden.de) at [TU Dresden](https://www.tu-dresden.de). The sources of information are `oss-projects.yaml`, which describes the projects, and `cs-groups.yaml`, which describes the research groups involved.

## How to use?

Install the required packages (e.g. in venv):
```bash
pip3 install -r ./requirements.txt
```

Run `init_site.py` to generate a static HTML page with an overview of all projects.

Run `init_readme.py` to generate the README of this repository containing all projects.

## Add a new project

Keys in `oss-projects.yaml`
| Name | Type | Required? | Description |
|------|------|------|-----|
| `name` | `string` | ✅ | The name of the project |
| `groups` | `string[]` | ✅ | The handles of the research groups that are part of the project (see `cs-groups.yaml`) |
| `founder` | `boolean` | ✅ | If you are the founder of the project |
| `maintainer` | `boolean` | ✅ | If you are a maintainer of the project |
| `contributor` | `boolean` | ✅ | If you are a contributor of the project |
| `involved` | `boolean` | ✅ | If you are still involved |
| `description` | `string` | Optional | A short description of the project |
| `website` | `string` | Optional | A link to the website of the project |
| `repository` | `string` | Optional | URL of the public repository |
| `license` | `string` | Optional | The license under which the project is available |
| `logo` | `string` | Optional | The relative path to the logo of your project in the `projects` directory (place your logo in `/website/images/projects`) |

Keys in `cs-groups.yaml`
| Name | Type | Required? | Description |
|------|------|------|-----|
| `name` | `string` | ✅ | The name of the research group |
| `handle` | `string` | ✅ | The handle of the research group |
| `website` | `string` | Optional | URL to the website of the research group |

Append this template to `oss-projects.yaml` and fill in your data:
```yaml
- name:
  groups: []
  founder:
  maintainer:
  contributor:
  involved:
  description:
  website:
  repository:
  license:
  logo:
```

For the logo, upload the logo to the `website/images/projects` folder and enter the relative URL to the logo in the `website/images/projects` folder.

For the groups, add the handle of your research group to the list.

If your research group does not exist yet, append this template to `cs-groups.yaml` and fill in your data:
```yaml
- name: 
  handle: 
  website: 
```

# Projects

The following list presents open source software projects in which members of the Faculty of Computer Science at TU Dresden are involved.
