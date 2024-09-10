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
| `contributor` | `boolean` | ✅ |
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

# Projects
### A 4-Approximation Algorithm for Min Max Correlation Clustering

Research Group: [Chair of Machine Learning for Computer Vision](https://mlcv.inf.tu-dresden.de/index-de.html) (Founder) 

More information: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.

License: N/A

[Code](https://github.com/JannikIrmai/min-max-correlation-clustering) [Project Site](https://github.com/JannikIrmai/min-max-correlation-clustering)

---
### AccessibleMaps

Research Group: [Chair of Human-Computer-Interaction](https://tu-dresden.de/ing/informatik/ai/mci?set_language=en) (Contributor) 

More information: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.

License: MIT

[Code](https://github.com/AccessibleMaps) [Project Site](https://accessiblemaps.de/)

---
### ACM LaTeX template

Research Group: [Chair of Networked Systems Modeling](https://www.cms-labs.org/) (Contributor) 

More information: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.

License: LPPL-1.3c

[Code](https://github.com/borisveytsman/acmart) [Project Site](https://ctan.org/pkg/acmart)

---
### AMCS

Research Group: [Chair of Distributed and Networked Systems](https://netd.cs.tu-dresden.de) (Founder) 

More information: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.

License: N/A

[Project Site](https://amcs.website/)

---
### AN.ON

Research Group: [Chair of Privacy and Security](https://tu-dresden.de/ing/informatik/sya/ps?set_language=en) (Founder) (Maintainer) (Contributor) 

More information: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.

License: BSD-style

[Code](https://dud-scm.inf.tu-dresden.de/an.on) [Project Site](https://anon.inf.tu-dresden.de)

---
### base2-mlir

Research Group: [Chair for Compiler Construction](https://www.cfaed.tu-dresden.de/ccc-about) (Founder) (Maintainer) (Contributor) 

More information: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.

License: ISC

[Code](https://github.com/KFAFSP/base2-mlir) [Project Site](https://github.com/KFAFSP/base2-mlir)

---
### BenchIT

Research Group: [Chair of Computer Architecture](https://tu-dresden.de/ing/informatik/ti/professur-fuer-rechnerarchitektur?set_language=en) (Maintainer) (Contributor) 

More information: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.

License: BSD'ish

[Code](https://gitlab.hrz.tu-chemnitz.de/tud-zih-energy/benchit) [Project Site](https://gitlab.hrz.tu-chemnitz.de/tud-zih-energy/benchit)

---
### BrailleIO

Research Group: [Chair of Human-Computer-Interaction](https://tu-dresden.de/ing/informatik/ai/mci?set_language=en) (Maintainer) - no longer involved

More information: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.

License: BSD-2-Clause

[Code](https://github.com/TUD-INF-IAI-MCI/BrailleIO) [Project Site](no URL, publication Bornschein, J. (2014, November). BrailleIO–a tactile display abstraction framework. In The Proceedings of Workshop Tactile/Haptic User Interfaces for Tabletops and Tablets (TacTT 2014). S (pp. 36-41).)

---
### Cinnamon

Research Group: [Chair for Compiler Construction](https://www.cfaed.tu-dresden.de/ccc-about) (Founder) (Maintainer) (Contributor) 

More information: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.

License: MIT

[Project Site](https://github.com/tud-ccc/Cinnamon)

---
### compy-learn

Research Group: [Chair for Compiler Construction](https://www.cfaed.tu-dresden.de/ccc-about) (Founder) (Maintainer) (Contributor) 

More information: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.

License: Apache-2.0

[Code](https://github.com/tud-ccc/compy-learn) [Project Site](https://github.com/tud-ccc/compy-learn)

---
### condrust

Research Group: [Chair for Compiler Construction](https://www.cfaed.tu-dresden.de/ccc-about) (Founder) (Maintainer) (Contributor) 

More information: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.

License: ISC

[Code](https://github.com/ohua-lang/condrust) [Project Site](https://github.com/ohua-lang/condrust)

---
### conexp-clj

Research Group: [Chair of Knowledge-Based Systems](https://iccl.inf.tu-dresden.de/web/Wissensbasierte_Systeme/en) (Contributor) 

More information: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.

License: EPL-1.0

[Code](https://github.com/tomhanika/conexp-clj) [Project Site](https://github.com/tomhanika/conexp-clj)

---
### CP2K

Research Group: [Computational Systems Science](N/A) (Maintainer) (Contributor) 

More information: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.

License: GPL-2.0

[Code](https://github.com/cp2k) [Project Site](https://cp2k.org)

---
### CSBDeep

Research Group: [Chair of Machine Learning for Spatial Understanding](https://fis.tu-dresden.de/portal/en/organisations/chair-of-machine-learning-for-spatial-understanding-scadsai-dresdenleipzig(69b2a2a2-aede-411d-a762-df4bb49490eb).html) (Founder) 

More information: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.

License: BSD-3-Clause

[Code](https://github.com/CSBDeep/CSBDeep) [Project Site](http://csbdeep.bioimagecomputing.com/doc/)

---
### dear

Research Group: [Chair for Compiler Construction](https://www.cfaed.tu-dresden.de/ccc-about) (Founder) (Maintainer) (Contributor) - no longer involved

More information: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.

License: ISC

[Code](https://github.com/tud-ccc/dear) [Project Site](https://github.com/tud-ccc/dear)

---
### dfg-mlir

Research Group: [Chair for Compiler Construction](https://www.cfaed.tu-dresden.de/ccc-about) (Founder) (Maintainer) (Contributor) 

More information: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.

License: ISC

[Code](https://github.com/Feliix42/dfg-mlir) [Project Site](https://github.com/Feliix42/dfg-mlir)

---
### dudle

Research Group: [Chair of Privacy and Security](https://tu-dresden.de/ing/informatik/sya/ps?set_language=en) (Contributor) 

More information: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.

License: AGPL-3.0

[Code](https://github.com/kellerben/dudle/) [Project Site](https://dud-poll.inf.tu-dresden.de/)

---
### Eclipse SUMO

Research Group: [Chair of Networked Systems Modeling](https://www.cms-labs.org/) (Contributor) 

More information: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.

License: EPL-2.0 and more

[Code](https://github.com/eclipse-sumo/sumo) [Project Site](https://eclipse.dev/sumo/)

---
### FAIL*

Research Group: [Chair of Operating Systems](https://tu-dresden.de/ing/informatik/sya/professur-fuer-betriebssysteme?set_language=en) (Founder) (Maintainer) (Contributor) 

More information: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.

License: GPL-3.0

[Code](https://github.com/danceos/fail) [Project Site](https://github.com/danceos/fail)

---
### FIRESTARTER

Research Group: [Chair of Computer Architecture](https://tu-dresden.de/ing/informatik/ti/professur-fuer-rechnerarchitektur?set_language=en) (Contributor) 

More information: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.

License: GPL-3.0

[Code](https://github.com/tud-zih-energy/FIRESTARTER) [Project Site](https://github.com/tud-zih-energy/FIRESTARTER)

---
### gem5

Research Group: [Chair for Compiler Construction](https://www.cfaed.tu-dresden.de/ccc-about) (Contributor) - no longer involved

More information: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.

License: BSD-3-Clause

[Code](https://www.gem5.org/) [Project Site](https://www.gem5.org/)

---
### GNU Taler

Research Group: [Chair of Distributed and Networked Systems](https://netd.cs.tu-dresden.de) (Contributor) 

More information: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.

License: GPL

[Code](https://git.taler.net/) [Project Site](https://taler.net/de/index.html)

---
### GraalVM with Role Support

Research Group: [Chair for Compiler Construction](https://www.cfaed.tu-dresden.de/ccc-about) (Founder) (Maintainer) (Contributor) - no longer involved

More information: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.

License: GPL-2.0 with the “Classpath” Exception

[Code](https://github.com/lschuetze/graal) [Project Site](https://github.com/lschuetze/graal)

---
### Graphs and graph algorithms in C++

Research Group: [Chair of Machine Learning for Computer Vision](https://mlcv.inf.tu-dresden.de/index-de.html) (Founder) 

More information: This project sits in a small niche. For most applications, BGL, Blitz or Lemon are a better choice.

License: MIT

[Code](https://github.com/bjoern-andres/graph) [Project Site](https://github.com/bjoern-andres/graph)

---
### learning-compiler-graphs

Research Group: [Chair for Compiler Construction](https://www.cfaed.tu-dresden.de/ccc-about) (Founder) (Maintainer) (Contributor) 

More information: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.

License: N/A

[Code](https://github.com/tud-ccc/learning-compiler-graphs) [Project Site](https://github.com/tud-ccc/learning-compiler-graphs)

---
### libAPR, pyapr, apr-napari

Research Group: [Chair of Scientific Computing for Systems Biology](https://tu-dresden.de/ing/informatik/ki/wr?set_language=en) (Founder) (Maintainer) (Contributor) 

More information: C++ core library for the adaptive particle representation (APR) of images, including its Python package (pyapr) and plugin for the image viewer "napari" (napari-apr) as well as an APR-native volume renderer and a Big Data Viewer for distributed and tiled volume images.

License: Apache-2.0

[Code](https://github.com/AdaptiveParticles) [Project Site](https://github.com/AdaptiveParticles)

---
### Lingua Franca

Research Group: [Chair for Compiler Construction](https://www.cfaed.tu-dresden.de/ccc-about) (Founder) (Maintainer) (Contributor) 

More information: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.

License: BSD-2-Clause

[Code](https://github.com/lf-lang/lingua-franca) [Project Site](https://github.com/lf-lang/lingua-franca)

---
### Linux kernel

Research Group: [Chair of Computer Architecture](https://tu-dresden.de/ing/informatik/ti/professur-fuer-rechnerarchitektur?set_language=en) (Contributor) 

More information: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.

License: GPL-2.0

[Code](https://github.com/torvalds/linux) [Project Site](https://github.com/torvalds/linux)

---
### Marray

Research Group: [Chair of Machine Learning for Computer Vision](https://mlcv.inf.tu-dresden.de/index-de.html) (Founder) 

More information: Now largely adopted into ISO C++ as std::span

License: N/A

[Code](https://github.com/bjoern-andres/marray) [Project Site](https://github.com/bjoern-andres/marray)

---
### messner

Research Group: [Chair for Compiler Construction](https://www.cfaed.tu-dresden.de/ccc-about) (Founder) (Maintainer) (Contributor) 

More information: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.

License: ISC

[Code](https://github.com/everest-h2020/messner) [Project Site](https://github.com/everest-h2020/messner)

---
### Mobile trace generator

Research Group: [Chair for Compiler Construction](https://www.cfaed.tu-dresden.de/ccc-about) (Founder) (Maintainer) (Contributor) - no longer involved

More information: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.

License: ISC

[Code](https://github.com/tud-ccc/mobile-traces) [Project Site](https://github.com/tud-ccc/mobile-traces)

---
### Mocasin

Research Group: [Chair for Compiler Construction](https://www.cfaed.tu-dresden.de/ccc-about) (Founder) (Maintainer) (Contributor) 

More information: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.

License: ISC

[Code](https://github.com/tud-ccc/mocasin) [Project Site](https://github.com/tud-ccc/mocasin)

---
### MOSAICsuite

Research Group: [Chair of Scientific Computing for Systems Biology](https://tu-dresden.de/ing/informatik/ki/wr?set_language=en) (Founder) (Maintainer) (Contributor) 

More information: Plugin suite for the popular bio-image analysis software "Image/J" and "Fiji" with all image processing and analysis methods from our group. Around 30'000 unique-IP starts ups per day worldwide.

License: GPL-3.0

[Code](https://git.mpi-cbg.de/mosaic/software/bio-imaging/MosaicSuite) [Project Site](https://sbalzarini-lab.org/?q=downloads/imageJ)

---
### mpsym

Research Group: [Chair for Compiler Construction](https://www.cfaed.tu-dresden.de/ccc-about) (Founder) (Maintainer) (Contributor) - no longer involved

More information: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.

License: MIT

[Code](https://github.com/tud-ccc/mpsym) [Project Site](https://github.com/tud-ccc/mpsym)

---
### Nemo

Research Group: [Chair of Knowledge-Based Systems](https://iccl.inf.tu-dresden.de/web/Wissensbasierte_Systeme/en) (Founder) (Maintainer) (Contributor) 

More information: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.

License: Apache-2.0 and MIT

[Code](https://github.com/knowsys/nemo) [Project Site](https://github.com/knowsys/nemo)

---
### Object Teams

Research Group: [Chair for Compiler Construction](https://www.cfaed.tu-dresden.de/ccc-about) (Contributor) - no longer involved

More information: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.

License: EPL-2.0

[Code](https://gitlab.eclipse.org/eclipse/objectteams/objectteams) [Project Site](https://www.eclipse.org/objectteams/)

---
### Object Teams InvokeDynamic

Research Group: [Chair for Compiler Construction](https://www.cfaed.tu-dresden.de/ccc-about) (Founder) (Maintainer) (Contributor) - no longer involved

More information: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.

License: EPL-2.0

[Code](https://github.com/lschuetze/objectteams-poly) [Project Site](https://github.com/lschuetze/objectteams-poly)

---
### ODNS Measurement Tools

Research Group: [Chair of Distributed and Networked Systems](https://netd.cs.tu-dresden.de) (Founder) (Maintainer) (Contributor) 

More information: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.

License: BSD-2-Clause

[Code](https://github.com/netd-tud/odns-measurement-tools) [Project Site](https://github.com/netd-tud/odns-measurement-tools)

---
### OMNeT++

Research Group: [Chair of Networked Systems Modeling](https://www.cms-labs.org/) (Contributor) 

More information: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.

License: custom

[Code](https://github.com/omnetpp/omnetpp) [Project Site](https://omnetpp.org/)

---
### OMNeT++ INET Framework

Research Group: [Chair of Networked Systems Modeling](https://www.cms-labs.org/) (Contributor) 

More information: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.

License: LGPL-3.0-or-later and others

[Code](https://github.com/inet-framework/inet) [Project Site](https://inet.omnetpp.org/)

---
### OpenFPM

Research Group: [Chair of Scientific Computing for Systems Biology](https://tu-dresden.de/ing/informatik/ki/wr?set_language=en) (Founder) (Maintainer) (Contributor) 

More information: Scalable middleware and domain-specific language for scientific computing on CPU and GPU clusters with transparent parallelization.

License: BSD-3-Clause

[Code](https://github.com/mosaic-group/openfpm/) [Project Site](http://openfpm.mpi-cbg.de/)

---
### OpenGM

Research Group: [Chair of Machine Learning for Computer Vision](https://mlcv.inf.tu-dresden.de/index-de.html) (Founder) 

More information: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.

License: N/A

[Code](https://github.com/opengm/opengm) [Project Site](https://github.com/opengm/opengm)

---
### OpenPME

Research Group: [Chair for Compiler Construction](https://www.cfaed.tu-dresden.de/ccc-about) (Founder) (Maintainer) (Contributor) 

More information: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.

License: ISC

[Code](https://github.com/Nesrinekh/OpenPME) [Project Site](https://github.com/Nesrinekh/OpenPME)

---
### Partial Optimality in Cubic Correlation Clustering

Research Group: [Chair of Machine Learning for Computer Vision](https://mlcv.inf.tu-dresden.de/index-de.html) (Founder) 

More information: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.

License: N/A

[Code](https://github.com/dsteindd/partial-optimality-in-cubic-correlation-clustering) [Project Site](https://github.com/dsteindd/partial-optimality-in-cubic-correlation-clustering)

---
### polygym

Research Group: [Chair for Compiler Construction](https://www.cfaed.tu-dresden.de/ccc-about) (Founder) (Maintainer) (Contributor) - no longer involved

More information: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.

License: N/A

[Code](https://github.com/PolyGym) [Project Site](https://github.com/PolyGym)

---
### PrioBike

Research Group: [Chair of Distributed and Networked Systems](https://netd.cs.tu-dresden.de) (Founder) (Contributor) 

More information: App and services of a traffic light assistance system for cyclists

License: MIT

[Code](https://github.com/priobike/) [Project Site](https://github.com/priobike/)

---
### reactor-cpp

Research Group: [Chair for Compiler Construction](https://www.cfaed.tu-dresden.de/ccc-about) (Founder) (Maintainer) (Contributor) 

More information: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.

License: ISC

[Code](https://github.com/lf-lang/reactor-cpp) [Project Site](https://github.com/lf-lang/reactor-cpp)

---
### RIOT

<img align="right" height="100" src="./website/images/projects/RIOT-logo.png">

Research Group: [Chair of Distributed and Networked Systems](https://netd.cs.tu-dresden.de) (Founder) (Maintainer) (Contributor) 

More information: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.

License: LGPL

[Code](https://github.com/RIOT-OS/RIOT) [Project Site](https://riot-os.org)

---
### RTM Compiler

Research Group: [Chair for Compiler Construction](https://www.cfaed.tu-dresden.de/ccc-about) (Founder) (Maintainer) (Contributor) - no longer involved

More information: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.

License: BSD-2-Clause

[Code](https://github.com/tud-ccc/rtm-compiler) [Project Site](https://github.com/tud-ccc/rtm-compiler)

---
### RTRlib

Research Group: [Chair of Distributed and Networked Systems](https://netd.cs.tu-dresden.de) (Founder) (Maintainer) (Contributor) 

More information: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.

License: MIT

[Code](https://github.com/rtrlib) [Project Site](https://rtrlib.realmv6.org/)

---
### RTSim

Research Group: [Chair for Compiler Construction](https://www.cfaed.tu-dresden.de/ccc-about) (Founder) (Maintainer) (Contributor) 

More information: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.

License: N/A

[Code](https://github.com/tud-ccc/RTSim) [Project Site](https://github.com/tud-ccc/RTSim)

---
### Rulewerk

Research Group: [Chair of Knowledge-Based Systems](https://iccl.inf.tu-dresden.de/web/Wissensbasierte_Systeme/en) (Founder) (Maintainer) 

More information: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.

License: Apache-2.0

[Code](https://github.com/knowsys/rulewerk) [Project Site](https://github.com/knowsys/rulewerk)

---
### Scenery

Research Group: [Chair of Scientific Computing for Systems Biology](https://tu-dresden.de/ing/informatik/ki/wr?set_language=en) (Founder) (Contributor) 

More information: Platform-portable VR/AR visualization and driver library including distributed rendering of very large datasets and user-interaction modalities.

License: LGPL-3

[Code](https://github.com/scenerygraphics/scenery) [Project Site](https://sbalzarini-lab.org/?q=downloads/scenery)

---
### Score-P

Research Group: [Chair of Computer Architecture](https://tu-dresden.de/ing/informatik/ti/professur-fuer-rechnerarchitektur?set_language=en) (Contributor) 

More information: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.

License: BSD-style

[Code](https://gitlab.com/score-p/scorep) [Project Site](https://gitlab.com/score-p/scorep)

---
### Score-P autotools

Research Group: [Chair of Computer Architecture](https://tu-dresden.de/ing/informatik/ti/professur-fuer-rechnerarchitektur?set_language=en) (Contributor) 

More information: This contains multiple packages. My latest contributions were for the NEC compiler suite

License: GPL-3.0+

[Code](https://perftools.pages.jsc.fz-juelich.de/utils/perftools-dev/perftools-dev-latest.tar.gz) [Project Site](https://gitlab.jsc.fz-juelich.de/perftools/utils/)

---
### Score-P libsensors Plugin Counter

Research Group: [Chair of Computer Architecture](https://tu-dresden.de/ing/informatik/ti/professur-fuer-rechnerarchitektur?set_language=en) (Maintainer) (Contributor) 

More information: There are various plugins available, which I maintain and contribute to this is one of them.

License: BSD 3-Clause "New" or "Revised" License

[Code](https://github.com/score-p/scorep_plugin_libsensors) [Project Site](https://github.com/score-p/scorep_plugin_libsensors)

---
### Semantic MediaWiki

Research Group: [Chair of Knowledge-Based Systems](https://iccl.inf.tu-dresden.de/web/Wissensbasierte_Systeme/en) (Founder) (Maintainer) - no longer involved

More information: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.

License: GPL

[Code](https://github.com/SemanticMediaWiki/SemanticMediaWiki/) [Project Site](https://www.semantic-mediawiki.org)

---
### Sigi-frontend

Research Group: [Chair for Compiler Construction](https://www.cfaed.tu-dresden.de/ccc-about) (Founder) (Maintainer) (Contributor) 

More information: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.

License: Apache-2.0

[Project Site](https://github.com/tud-ccc/kp-mlir-sigi-frontend)

---
### Sigi-mlir

Research Group: [Chair for Compiler Construction](https://www.cfaed.tu-dresden.de/ccc-about) (Founder) (Maintainer) (Contributor) 

More information: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.

License: MIT

[Project Site](https://github.com/tud-ccc/kp-mlir-sigi-mlir)

---
### SQID

Research Group: [Chair of Knowledge-Based Systems](https://iccl.inf.tu-dresden.de/web/Wissensbasierte_Systeme/en) (Founder) (Maintainer) 

More information: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.

License: Apache-2.0

[Code](https://github.com/Wikidata/SQID/) [Project Site](https://sqid.toolforge.org/)

---
### stardist

Research Group: [Chair of Machine Learning for Spatial Understanding](https://fis.tu-dresden.de/portal/en/organisations/chair-of-machine-learning-for-spatial-understanding-scadsai-dresdenleipzig(69b2a2a2-aede-411d-a762-df4bb49490eb).html) (Founder) 

More information: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.

License: BSD-3-Clause

[Code](https://github.com/stardist/stardist) [Project Site](https://github.com/stardist/stardist)

---
### Tetris

Research Group: [Chair for Compiler Construction](https://www.cfaed.tu-dresden.de/ccc-about) (Founder) (Maintainer) (Contributor) - no longer involved

More information: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.

License: GPL-3.0

[Code](https://github.com/l3nkz/tetris) [Project Site](https://github.com/l3nkz/tetris)

---
### Veins

Research Group: [Chair of Networked Systems Modeling](https://www.cms-labs.org/) (Founder) 

More information: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.

License: GPL-2.0-or-later and more

[Code](https://github.com/sommer/veins) [Project Site](https://veins.car2x.org/)

---
### ViewR

Research Group: [Junior Professorship in Immersive Media](https://tu-dresden.de/ing/informatik/smt/im?set_language=en) (Founder) (Maintainer) (Contributor) 

More information: We maintain a internal repo that is under active development, preparing for a large update of the public facing repo.

License: Apache-2.0

[Code](https://github.com/ixlabTUD/ViewR) [Project Site](https://github.com/ixlabTUD/ViewR)

---
### VLog

Research Group: [Chair of Knowledge-Based Systems](https://iccl.inf.tu-dresden.de/web/Wissensbasierte_Systeme/en) (Contributor) - no longer involved

More information: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.

License: Apache-2.0

[Code](https://github.com/karmaresearch/vlog) [Project Site](https://github.com/karmaresearch/vlog)

---
### Wikidata Toolkit

Research Group: [Chair of Knowledge-Based Systems](https://iccl.inf.tu-dresden.de/web/Wissensbasierte_Systeme/en) (Founder) (Maintainer) - no longer involved

More information: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.

License: Apache-2.0

[Code](https://github.com/Wikidata/Wikidata-Toolkit) [Project Site](https://github.com/Wikidata/Wikidata-Toolkit)

---
### X86-Energy Libraries

Research Group: [Chair of Computer Architecture](https://tu-dresden.de/ing/informatik/ti/professur-fuer-rechnerarchitektur?set_language=en) (Founder) (Maintainer) (Contributor) 

More information: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam.

License: LGPL-2.1

[Code](https://github.com/tud-zih-energy/x86_energy) [Project Site](https://github.com/tud-zih-energy/x86_energy)

---
