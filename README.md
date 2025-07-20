# Tech Radar

This is my tech radar used to map out technologies, tools, techniques, and platforms that I'm currently using, exploring, or interested in learning more about. The goal is to visualize and prioritize where you are focusing your energy, learning, and development in relation to technology.

This tech radar is inspired by the [ThoughtWorks Tech Radar](https://www.thoughtworks.com/radar) and the [Zalando Tech Radar](https://opensource.zalando.com/tech-radar).

## Table of Contents

- [Tech Radar](#tech-radar)
  - [Table of Contents](#table-of-contents)
  - [Project Technologies](#project-technologies)
  - [Development](#development)
    - [To update the radar data](#to-update-the-radar-data)

## Project Technologies

The project uses basic HTML, CSS, and JavaScript to create a simple visualization of the tech radar which is then hosted on GitHub Pages. The data for the visualization is stored in a JSON file and loaded into the visualization using JavaScript.

## Development

To run the development server:

```bash
python3 -m http.server
```

Then navigate to `http://localhost:8000/github-pages/`

### To update the radar data

To change the radar data, edit the `config.json` file in the `github-pages` directory.

The configuration file is structured as follows:

```json
{
  "date": "2025.07",
  "entries": []
}
```

Each entry in the `entries` array should have the following structure:

```json
{
  "quadrant": 1,
  "ring": 0,
  "label": "Python",
  "active": true,
  "moved": 0,
  "link": "https://www.python.org/"
}
```

Fields:

- `quadrant`: The quadrant the entry belongs to (1-4).
  - 1: Platforms & Cloud Services
  - 2: Languages & Frameworks
  - 3: Techniques & Methodologies
  - 4: Tools
- `ring`: The ring the entry belongs to (0-3).
  - 0: Experienced
  - 1: Trial
  - 2: Watch
  - 3: Maintain
- `label`: The name of the technology, tool, technique, or platform.
- `active`: Whether the entry is currently active (true/false).
- `moved`: The number of rings the entry has moved.
  - 0: No movement
  - 1: Moved inward (up)
  - 2: Moved outward (down)
- `link`: A link to more information about the entry.
