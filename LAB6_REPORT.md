# Laboratory Work #6 Report

## Topic: "CI/CD Pipeline with GitHub Actions"

---

## Objective:
Implement automated CI/CD pipeline using GitHub Actions for building RPM and DEB packages.

---

## Implementation:

### Workflow Structure:
- **File:** `.github/workflows/build.yml`
- **Trigger:** Push to main branch
- **Jobs:** Parallel DEB and RPM building

### Key Components:
- Automated dependency installation
- Parallel package building
- Artifact upload

---

## Results:

### Success Metrics:
- Workflow executes automatically
- Both DEB and RPM packages built successfully
- Build duration: ~1 minute 37 seconds
- Artifacts available for download

### Deliverables:
- DEB package: `count-files_1.0-1_all.deb`
- RPM package: `count-files-1.0-1.noarch.rpm`

---

## Conclusion:
GitHub Actions provides effective automation for software packaging, enabling continuous integration and delivery for Linux packages.

---
**Performed by:** Arshyn Anna  
**Date:** November 26, 2024
