function onFilterChange() {
    const search = document.getElementById("search")
    const searchValue = search.value.toLowerCase()

    roleToFilter = document.getElementById("role").value
    licenseToFilter = document.getElementById("license").value
    chairToFilter = document.getElementById("chair").value
    stillInvolvedToFilter = document.getElementById("still-involved").value

    const projects = document.getElementsByClassName("project")

    // Reset all projects
    if (roleToFilter === "" && licenseToFilter === "" && chairToFilter === "" && stillInvolvedToFilter === "" && (searchValue === "" || searchValue.length <= 2)) {
        for (let project of projects) {
            project.style.display = "block"
        }
    } else {
        // Filter projects for each filter set
        for (let project of projects) {
            const i = project.id

            const groups = project.getElementsByClassName("chair-name")
    
            if (searchValue !== "" && searchValue.length > 2) {
                const title = document.getElementById("project-name-" + i).innerHTML.toLowerCase()
                const description = document.getElementById("more-info-" + i).innerHTML.toLowerCase()
                const licenseElement = document.getElementById("license-" + i)
                let license = licenseElement !== null ? licenseElement.innerHTML.toLowerCase() : ""

                // Tags
                let containsTag = false
                if ("founder".includes(searchValue)) {
                    const tag_founder = project.getElementsByClassName("tag founder")
                    if (tag_founder.length == 0) {
                        project.style.display = "none"
                        continue;
                    } else {
                        containsTag = true
                    }
                }
                if ("maintainer".includes(searchValue)) {
                    const tag_maintainer = project.getElementsByClassName("tag maintainer")
                    if (tag_maintainer.length == 0) {
                        project.style.display = "none"
                        continue;
                    } else {
                        containsTag = true
                    }
                }
                if ("contributor".includes(searchValue)) {
                    const tag_contributor = project.getElementsByClassName("tag contributor")
                    if (tag_contributor.length == 0) {
                        project.style.display = "none"
                        continue;
                    } else {
                        containsTag = true
                    }
                }

                includesGroup = false
                for (let group of groups) {
                    includesGroup = includesGroup || group.innerHTML.toLowerCase().includes(searchValue)
                }

                if (!title.includes(searchValue) && !description.includes(searchValue) && !includesGroup && !license.includes(searchValue) && !containsTag) {
                    project.style.display = "none"
                    continue;
                }
            }
    
            if (roleToFilter !== "") {
                if (!containsRole(project)) {
                    project.style.display = "none"
                    continue;
                }
            }
    
            if (licenseToFilter !== "") {
                if (!containsLicense(i, licenseToFilter)) {
                    project.style.display = "none"
                    continue;
                }
            }
    
            if (chairToFilter !== "") {
                if (!containsChair(groups, chairToFilter)) {
                    project.style.display = "none"
                    continue;
                }
            }
    
            if (stillInvolvedToFilter !== "") {
                if (!containsStillInvolved(project, stillInvolvedToFilter)) {
                    project.style.display = "none"
                    continue;
                }
            }
    
            project.style.display = "block"
        }
    }

    // Check if not-involved is empty
    const projectsNoLongerInvolved = document.getElementsByClassName("not-involved")
    
    let isNoLongerInvolvedDisplayed = false
    for (let project of projectsNoLongerInvolved) {
        var parentProject = project.closest(".project");
        if (parentProject.style.display !== "none") {
            isNoLongerInvolvedDisplayed = true
            break
        }
    }
    document.getElementById("no-longer-involved").style.display = isNoLongerInvolvedDisplayed ? "block" : "none"
}

function containsRole(project) {
    const tags = project.getElementsByClassName("tag")
    let show = false
    for (let tag of tags) {
        if (tag.innerHTML == roleToFilter) {
            show = true
            break
        }
    }
    return show
}

function containsLicense(idx, liceseToFilter) {
    const license = document.getElementById("license-" + idx)
    if (license === null) {
        return false
    }

    // Decode HTML entities
    const txt = document.createElement('textarea');
	txt.innerHTML = license.innerHTML;

    return txt.innerHTML == liceseToFilter
}

function containsChair(groups, chairToFilter) {
    for (let group of groups) {
        if (group.innerHTML.includes(chairToFilter)) {
            return true
        }
    }

    return false
}

function containsStillInvolved(project, stillInvolvedToFilter) {
    const notInvolved = project.getElementsByClassName("not-involved")
    if (stillInvolvedToFilter === "yes") {
        return notInvolved === null || notInvolved.length === 0
    } else {
        return notInvolved.length > 0
    }
}
