# Xio's Guide to Monsters

If you're a DM like me, and you have multiple sources of D&D 5e monsters that include WotC as well as third-party suppliers, you may have struggled with how to actually make use of it all. The problem is that they're not in one place, so it's difficult to search across multiple books.

This is my attempt to create a single repository that includes:
- all monster data in one CSV
- Python scripts to create Markdown files for each monster out of the CSV, for use in tools like [Obsidian](https://obsidian.md)
- the created Markdown files with relevant parameters.

Note that the idea is to create an _index_ of monsters to let you find the right one more easily, not a full copy of sourcebooks. Only the following fields for each monster are included:
- Name
- Size
- Type
- Environment
- HP
- AC
- Initiative
- Alignment
- Legendary
- Lair
- Unique
- CR
- Tags
- Source

You'll still need to own the relevant sourcebooks to see the full monster stats.

## How to Use

### If you just want a single list of monsters

... use `monsters.csv`. It has all the monsters stats, and you can open it up in your IDE or spreadsheet editor.

### If you want to import the existing monsters into your Markdown-based editor

... download the Markdown files in `/monsterfiles`. The monster attributes are listed as frontmatter parameters.

Copy them into the directory used by your Markdown editor. You could use these in conjunction with [the Obsidian Dataview plugin](https://blacksmithgu.github.io/obsidian-dataview/) to search all monsters by any parameter(s) you choose. (That's what I'm doing!)

### If you want to create your own monsters

... first, add new monster data in `monsters.csv`.

Then, [install Python3](https://www.python.org/downloads/).

Modify `/scripts/create-md.py` to change the `dir` variable with the filepath you'd like the files to be created under.

Run `python3 create-md.py`. All monsters in `monsters.csv` should now have a `.md` file with their parameters filled out.

## Sources

The goal is to have everything from the core books and all of the most popular third-party content. Here's what's included now.

### Sourcebooks included

#### Official

- Basic Rules
- Monster Manual
- Hoard of the Dragon Queen, plus supplement
- Player's Handbook
- Curse of Strahd
- Explorer's Guide to Wildemount
- Guildmasters' Guide to Ravnica
- Princes of the Apocalypse , plus supplement
- Out of the Abyss
- Rise of Tiamat
- Storm King's Thunder
- Tales from the Yawning Portal
- Volo's Guide to Monsters
- Wayfinder's Guide to Eberron

#### Third-party

- Kobold Press
  - [Creature Codex for 5th Edition](https://koboldpress.com/kpstore/product/creature-codex-for-5th-edition-dnd/)
  - [Tome of Beasts](https://koboldpress.com/kpstore/product/tome-of-beasts-for-5th-edition/)
  - [Tome of Beasts 2 for 5th Edition](https://koboldpress.com/kpstore/product/tome-of-beasts-2-for-5th-edition/)
- Frog God Games: Fifth Edition Foes
- Monster-A-Day (Reddit)
- Nerzugal Role Playing: [Nerzugal's Extended Bestiary](https://www.drivethrurpg.com/product/205000/Nerzugals-Extended-Bestiary)
- Sasquatch Game Studio
  - [Primeval Thule 5e Campaign Setting](https://www.drivethrurpg.com/product/168149/Primeval-Thule-5e-Campaign-Setting?src=hottest_filtered)
  - [Primeval Thule 5e GM Companion](https://www.drivethrurpg.com/product/168153/Primeval-Thule-5e-GM-Companion?src=hottest_filtered)

### Compilations

I got the initial data for these monsters from other people's work:

- [blacktiger994 on Reddit](https://www.reddit.com/r/DnD/comments/m596w4/a_completely_organized_list_of_all_monsters_from/)
- [Asmor of the now-offline Kobold Fight Club](https://github.com/Asmor/5e-monsters)

## Make a contribution

If you have other sources that you'd like to add monsters from, or if you spot typos or other errors in the existing data, feel free to add them to `monsters.csv` and create a pull request!
