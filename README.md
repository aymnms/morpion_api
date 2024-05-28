<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/aymnms/morpion_server">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">morpion_server</h3>

  <p align="center">
    Morpion server game (api)
    <br />
    <br />
    <a href="https://github.com/aymnms/morpion_server">View Demo</a>
    ·
    <a href="https://github.com/aymnms/morpion_server/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/aymnms/morpion_server/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#prerequisites">Prerequisites</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This repository is the server of a morpion game. Soon, there will have a client repository to complete and done the project.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* Python 3.7+
* pip (Python package installer)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/aymnms/morpion_server.git
   ```
2. Create and activate a virtual environment
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install Python packages
   ```sh
   pip install -r requirements.txt
   ```
4. Set up environment variables (if needed)
   ```sh
   cp .env.example .env
   # Update .env with your configuration
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Run the server

```sh
python main.py
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] login
- [x] room
- [ ] game
  - [ ] victory
  - [ ] restart
- [ ] database

See the [open issues](https://github.com/aymnms/morpion_server/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/aymnms/morpion_server.svg?style=for-the-badge
[contributors-url]: https://github.com/aymnms/morpion_server/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/aymnms/morpion_server.svg?style=for-the-badge
[forks-url]: https://github.com/aymnms/morpion_server/network/members
[stars-shield]: https://img.shields.io/github/stars/aymnms/morpion_server.svg?style=for-the-badge
[stars-url]: https://github.com/aymnms/morpion_server/stargazers
[issues-shield]: https://img.shields.io/github/issues/aymnms/morpion_server.svg?style=for-the-badge
[issues-url]: https://github.com/aymnms/morpion_server/issues
[license-shield]: https://img.shields.io/github/license/aymnms/morpion_server.svg?style=for-the-badge
[license-url]: https://github.com/aymnms/morpion_server/blob/master/LICENSE.txt
```