# README

- [README](#readme)
  - [Directories](#directories)
  - [How to contribute](#how-to-contribute)
  - [Contribution Workflow](#contribution-workflow)
  - [File structure](#file-structure)
    - [Common fields](#common-fields)
    - [Mod exclusive fields](#mod-exclusive-fields)
    - [Weapons and parts fields](#weapons-and-parts-fields)
    - [Contributing an Icon](#contributing-an-icon)
    - [How to create Sets](#how-to-create-sets)
    - [How to define Tags](#how-to-define-tags)
  - [Contribute a new Language](#contribute-a-new-language)

## Directories

1. `dump` - Database dump in json format.
   1. `items` - common items, mods, warframes, scenes, etc. (non auctions)
   2. `liches` - auctions, lich related entities. (used in auctions)
   3. `rivens` - riven related entities. (used in auctions)
2. `icons` - If it is not possible to provide an icon by url, you can copy icon here, in binary format. (`png`/`jpg`)
3. `queued_updates` - Here are the files to be added to the database at the next upload.
   1. `items` - common items (see dump).
   2. `rivens` - riven related entities.
   3. `liches` - lich related entities.
4. `untranslated` - List of untranslated items.

## How to contribute

By issuing Pull requests, "rebase" workflow.

## Contribution Workflow

1. Add a new item or copy an old one into `queued_updates` folder in `%item_name%.json` format.
2. Apply desired changes to these files.
3. Commit with short description of your changes.
4. Send a pull request.
5. I'll review these changes and if everything is ok, i'll accept your pull request.
6. All changes will be merged into WFM database in a few days.
7. New `dump` will be created along with a new commit.

## File structure

### Common fields

1. `_id` - id of an item, do not modify it, and do not create it (in case of adding a new item)
2. `tags` - not used right now in any way, but it still prefarable to add them.
3. `icon` - local or remore path to the icon, check [This section](####Contributing-an-Icon)
4. `thumb` - Will be generated automatically.
5. `icon_format` - Will b generated automatically.
6. `sub_icon` - sub icon of an item, represent part of the set, like `handle` or `grip`, check [This section](####Sets)
7. `url_name` - Will be generated automatically.
8. `tradable` - This item is tradable. (`true`/`false`)
9. `part_of_set` - This item is part of a set. (`true`/`false`)
10. `set_root` - This item is set itself, like `Some Prime Set`, it's parrent of other parts.
11. `en` \ `ru` \ `ko` - lang specific subdocument.
    1. `item_name` - Name of an item.
    2. `description` - Item descriptrion.
    3. `wiki_link` - Link to the wiki.
    4. `drop` - Drop locations.
       1. `name` - Name of the location.
       2. `link` - link to the resource (wiki or wfm).
12. `trading_tax` - Tax

### Mod exclusive fields

1. `rarity` - Mod rarity.
2. `mod_max_rank` - Maximum possible mod\\arcane rank.

### Weapons and parts fields

1. `mastery_level` - mastery requirenment.
2. `ducats` - Costs in ducats.

### Contributing an Icon

From a remote source:  
`"icon": "https://vignette.wikia.nocookie.net/warframe/images/6/6d/Hind.png"`

From the icon folder:  
`"icon": "icons/<icon_file>"`

### How to create Sets

If you want to add a set, just create a set of files, and put a flag `"part_of_set" : true` inside a main file. (`Some Prime Set.json`)  
Our script will do the rest (crosslinks DB-documents with each other)

**For Example, Aklex**  
You just need to create:

1. `Aklex Prime Blueprint.json`
2. `Aklex Prime Link.json`
3. `Aklex Prime Set.json`

### How to define Tags

There is no strict convention, but you can use this logic:

1. Add item group, like `Blueprint` | `Mod`.
2. Add item type, like `Rifle` | `Warframe`.
3. Add additional definition, like `Prime` | `Corrupted` | `Huras`, `Rare`, etc.

For example Rare Rifle Mod should have `[Mod, Rifle, Rare]` tags.

## Contribute a new Language

Currently i can only ~reliably support only `en` and `ru` localizations.

> If you want to add another language, be sure that you will be able to finish your work.  
> There is 2600+ items in WFM database, this could be a tough task.

It's preferable to contribute translations for all items at once.

Use one of [this](https://www.w3schools.com/tags/ref_language_codes.asp) lang codes, to add a new translation.
