<!-- This template states what should be included in what way in your MR for each specific kind branches (feature/docs/bugfix).-->


<!-- For a "feature/" branch, provide a detailed description of the changes made in the MR and the related errata release plan or schedule. Also include reasons behind the changes and other considerations that reviewers should know, if any. -->
<!-- For a "docs/" branch, provide a detailed description of the code changes made in the MR and the reasons behind. Also include reasons other considerations that reviewers should know, if any. -->
<!-- For a "bugfix/" branch, provide a detailed description to help reviewers understand the issue, its cause, impact, and the proposed solution. -->

_Add descriptions right here and remove the italics formatting._ <!-- Mandatory -->


## Checklist <!-- Optional -->

<!-- Select one from the first three items for your MR and delete the other two items. -->
<!-- Include other items specific to your MR if any.  -->
<!-- This entire section can be deleted if all items are checked. -->

* [ ] <!-- Specific to "feature/" branches --> The MR only covers major content change for preparing the initial release or a new release for the document.
* [ ] <!-- Specific to "docs/" branches --> The MR only covers document code change that only requires doc internal review, e.g., updating templates, modifying documents based on templates, or making changes to the LaTeX code.
* [ ] <!-- Specific to "bugfix/" branches --> The MR only covers minor document fix, e.g., fixing typos, bugs, or mistakes.
* [ ] The MR title is clear and descriptive that summarizes the purpose of the MR.
* [ ] All related links, including Jira tasks and related MRs, are mentioned in the `Related` section.
* [ ] The correct chip label(s) is added in the `Labels` tab.
* [ ] The commit log is clean and ready to merge.
* [ ] The CI jobs for building and deploying the docs have been passed.
* [ ] All required approvers have been added to the `Reviewer` tab.
* [ ] Select `Mark as draft` if the MR is still a work in progress or click `Mark as ready` if the MR is ready to be merged.
* [ ] The branch is up to date with the master branch or has been rebased to master before merge.
* [ ] All required files in the Chip Errata Checklist (see repo Wiki) have been updated.


## Related <!-- Optional -->

* Mention related DOC Jira tasks to make sure they get updated, e.g., "- Closes DOC-0000"
* Mention related DIG Jira tasks labeled with `Errata` to indicate what bugs are documented, e.g., "- Documents DIG-000"
* Mention other related MRs or links, if any


## Release Notes <!-- Optional -->

<!-- Changes made in this MR relevant to developers, mostly for "feature/" branches, should be listed in this section using the past tense.-->
<!-- Remove this section if there are only minor changes in this MR, mostly for "docs/" and "bugfix/" branches.-->
<!-- Below are some examples.-->

* Added the bug "Chip will be damaged when BIAS_SLEEP = 0 and PD_CUR = 1" to ESP32-S3 Errata
* Updated descriptions for the bug "The USB-OTG Download function is unavailable" in ESP32-S3 Errata
* Translated the bug "The TOUCH\_SCAN\_DONE\_INT interrupt raw data value is undefined" in ESP32-S3 Errata
