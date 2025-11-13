<!-- This is the approval form template for chip errata release. If you decide to implement the approval process on Gitlab instead of the traditional way, use this template for your MR.-->


## Errata Title <!-- Mandatory -->

<!-- Insert errata title here together with the version number, e.g.,-->

ESP32-S3 Chip Series Errata v1.0

## Revision History <!-- Mandatory -->

<!-- Summarize the revision history here, e.g.,-->

* Added bug 1: The Digital Controller of SAR ADC2 cannot work
* Added bug 2: Chip will be damaged when BIAS_SLEEP = 0 and PD_CUR = 1
* Added chip identification information for ESP32-S3 chip revision v0.2


## Proposed Release Date <!-- Mandatory -->

<!-- Insert proposed errata release date here, e.g.,-->

2023-10-24


## Instructions for Reviewer <!-- Mandatory -->

Please follow the instructions below to approve the errata:
* Scroll down to find the latest comment posted by `Post MR Note`.
* Open the errata preview links to review the documents and comment if you have any feedback.
* Click the `Approve` button below to approve the errata release.


## Checklist for Chip Owner <!-- Optional -->

<!-- Include other items specific to your MR, if any. This entire section can be deleted if all items are checked. -->

* [ ] The MR title is in the format of `ESPxx Chip Series Errata vx.x Approval`
* [ ] The MR only includes updates to the _Revision History_ section of the errata and updates you made in response to reviewer's comments
* [ ] All related links, including Jira tasks and related MRs, are mentioned in the `Related` section.
* [ ] The correct chip label(s) is added in the `Labels` tab.
* [ ] The commit log is clean and ready to merge.
* [ ] The CI jobs for building and deploying the docs have been passed.
* [ ] All required approvers have been added to the `Reviewer` tab.
* [ ] The branch is up to date with the master branch or has been rebased to master before merge.
* [ ] All required files in the Chip Errata Checklist (see repo Wiki) have been updated.


## Related <!-- Optional -->

* Mention related DOC Jira tasks to make sure they get updated, e.g., "- Closes DOC-0000"
* Mention related MRs that contribute to this release, e.g., "- Releases updates in MR !0"
* Mention other links, if any
