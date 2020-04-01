





<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div>
  <p>
    <a href="https://github.com/github_username/repo">
      <img src="images/logo.png" alt="Logo">
    </a>
  </p>

  <h3 align="center">Anaphylaxis-Runrex</h3>

  <p>
    Feature extraction for developing an algorithm to identify anaphylaxis cases.
    Additional steps will require use of these variables to build a predictive algorithm.
  </p>
</div>


<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

* Python 3.8+
* runrex package: https://github.com/kpwhri/runrex

### Installation
 
1. Clone the repo
```sh
git clone https://github.com/kpwhri/anaphylaxis-runrex.git
```
2. Install requirements
```sh
pip install -r requirements.txt -r requirements-dev.txt
```
3. Run tests.
```sh
set/export PYTHONPATH=src
pytest tests
```


<!-- USAGE EXAMPLES -->
## Usage

* Build a configuration file as defined in [runrex](https://github.com/kpwhri/runrex)
    - Full details defined in that project's [schema.py](https://github.com/kpwhri/runrex/blob/master/src/runrex/schema.py)
* `python run.py runrex.conf.(py|json|yaml)`


## Variables Identified

Variables (called 'algorithms') are broken down into various 'categories'. Either can be used in building features.

|Algorithm|Category|Description|
|---|---|---|
|epinephrine|EPI_MENTION|any NOS mention of epinephrine|
|epinephrine|HAS_EPI|pt has/carries epipen|
|epinephrine|EPI_USE|description of epi use|
|epinephrine|MULTIPLE|multiple/repeated use of epi|
|epinephrine|RELATED_MEDS|mention of other meds in context of epi use|
|observation|OBSERVATION|admission for observation|
|observation|MONITORING|pt to be monitored|
|sudden|WITHIN_TIME|within/over period of time excl WINTHIN_TIME_SYMPTOM|
|sudden|WITHIN_TIME_SYMPTOM|WITHIN_TIME in vicinity of common symptom|
|sudden|SUDDEN|discussion of sudden onset/changeexcl SUDDEN_SYMPTOM|
|sudden|SUDDEN_SYMPTOM|SUDDEN in vicinity of common symptom|
|dx|PRIMARY|anaphylaxis as primary dx|
|dx|DIFFERENTIAL|anaphylaxis as differntial dx|
|dx|VISIT|anaphylaxis as visit reason|
|dx|FOLLOWUP|anaphylaxis for follow-up|
|dx|GENERIC|anaphylaxis dx in other context|
|dx|FINDING|evidence of anaphylaxis discussed|
|dx|NONE|other mention of 'anaphylaxis'|


## Output Format

See [runrex](https://github.com/kpwhri/runrex).


## Versions

<!-- Uses [SEMVER](https://semver.org/). -->

Updates/changes are not expected. Versioning is based on `YYYYmmm`. See https://github.com/kpwhri/anaphylaxis-runrex/releases.

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/kpwhri/anaphylaxis-runrex/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` or https://kpwhri.mit-license.org for more information.



<!-- CONTACT -->
## Contact

Please use the [issue tracker](https://github.com/kpwhri/anaphylaxis-runrex/issues). 


<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* This work was funded as part of the [Sentinel Initiative](https://www.fda.gov/safety/fdas-sentinel-initiative).





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/kpwhri/anaphylaxis-runrex.svg?style=flat-square
[contributors-url]: https://github.com/kpwhri/anaphylaxis-runrex/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/kpwhri/anaphylaxis-runrex.svg?style=flat-square
[forks-url]: https://github.com/kpwhri/anaphylaxis-runrex/network/members
[stars-shield]: https://img.shields.io/github/stars/kpwhri/anaphylaxis-runrex.svg?style=flat-square
[stars-url]: https://github.com/kpwhri/anaphylaxis-runrex/stargazers
[issues-shield]: https://img.shields.io/github/issues/kpwhri/anaphylaxis-runrex.svg?style=flat-square
[issues-url]: https://github.com/kpwhri/anaphylaxis-runrex/issues
[license-shield]: https://img.shields.io/github/license/kpwhri/anaphylaxis-runrex.svg?style=flat-square
[license-url]: https://kpwhri.mit-license.org/
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/company/kaiser-permanente-washington
<!-- [product-screenshot]: images/screenshot.png -->