# ARC Workshops

Hands-on robotics workshops from the Autonomous Robotics Club at GMU, built with MkDocs Material.

- Site: https://arc-gmu.github.io/workshops/
- Club website: https://gmu.autonomousrobotics.club/
- Discord: https://discord.gg/zn93yRNZGb

## Preview locally

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

## Layout

```
docs/<category>/<workshop>/     pages: index.md (overview) + numbered lessons
docs/<category>/<workshop>/images/
code/<category>/<workshop>/     starter and solution code, one folder per lesson
templates/workshop/             copy this to start a new workshop
```

Categories become the tabs across the top of the site (Start Here, Electronics, Mechanical, ...). Workshops go in the sidebar under their category.

## Adding a workshop

1. Copy `templates/workshop/` to `docs/<category>/<workshop-name>/`.
2. Fill in `index.md`: the `description` (shown in search results and link previews), tags, level, duration, prerequisites and what to bring. Give each lesson page a one-line `description:` too.
3. Put code in `code/<category>/<workshop-name>/<lesson>/starter/` and `.../solution/`.
4. Add the workshop to `nav` in `mkdocs.yml`, and add a card for it to `docs/index.md` and the category's `index.md`.

### Embedding code

Pages pull code straight from `code/`, so the docs can't drift from the real files:

````markdown
```cpp title="blink_solution.ino"
--8<-- "code/hardware/arduino-beginners/02-blink/blink_solution/blink_solution.ino"
```
````

If the file doesn't exist, the build fails.

Arduino sketches must sit in a folder with the same name as the `.ino` file (`blink_starter/blink_starter.ino`), or the IDE won't open them.

### CAD and other large files

`.stl`, `.step`, `.f3d`, `.3mf` and SolidWorks files are stored with Git LFS (see `.gitattributes`). Run `git lfs install` once before committing them.

## Publishing

- Every push to `main` builds the site and publishes it to GitHub Pages (Repo → Settings → Pages → Source: GitHub Actions).
- Pull requests that touch `docs/` or `code/` run `mkdocs build --strict`, so broken links and missing code files fail the check.

## Notes

- Material for MkDocs is in maintenance mode (fixes through Nov 2026). The version is pinned, so the site keeps building. Zensical, from the same team, reads `mkdocs.yml`, so migrating later should be straightforward.
- Set `NO_MKDOCS_2_WARNING=true` to hide the MkDocs 2.0 warning; `requirements.txt` keeps MkDocs below 2.
