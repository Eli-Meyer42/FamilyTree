# Family Constellation

A family tree in the style of the Path of Exile passive tree: generations as rings
around the oldest ancestors, a classic top-down tree view, birthdays with Hebrew
dates, and a spreadsheet importer for collecting info from relatives.

Live at **https://eli-meyer42.github.io/FamilyTree/**

| File | What it is |
|---|---|
| `index.html` | The whole app. Hosting config (`APP`, `FIREBASE`) is in the persistence section. |
| `manifest.webmanifest` | Makes it installable. Paths are relative because Pages serves from `/FamilyTree/`. |
| `sw.js` | Service worker — network-first for the page, so deploys show up immediately. |
| `make-icons.py` | Regenerates the icons. |

Data lives on the device (`familytree-v1`) and syncs to Firebase at `familytree/main`.
No family data is stored in this repository. Bump the build stamp on every push.
