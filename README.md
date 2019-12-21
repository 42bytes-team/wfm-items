# README

- [README](#readme)
  - [Directories](#directories)
  - [How to contribute](#how-to-contribute)
  - [Contribution Workflow](#contribution-workflow)
  - [File structure](#file-structure)
    - [Common fields](#common-fields)
    - [Mod exclusive fields](#mod-exclusive-fields)
    - [Weapons, parts fields](#weapons-parts-fields)
    - [Contributing an Icon](#contributing-an-icon)
    - [Sets](#sets)
    - [Tags](#tags)
  - [Contribute a new Language](#contribute-a-new-language)

> This is repo that contains Warframe.market item database in JSON format.

## Directories

1. `items` - Item files, full copy of the database.
2. `riven_items` - Weapons for which Riven mods are applicable.
3. `riven_attributes` - All possible attributes of Riven mods.
4. `queued_updates` - All files intended for updating the database should be located here.  
If you want to update an item, copy the file from the `items` folder to this directory, if file is not present inside `items` directory, just create it based on a template. (`template.json`)
5. `icons` - If it is not possible to provide an icon by url, you can copy it here in binary format. (`png`/`jpg`)

## How to contribute

By using Pull requests.

## Contribution Workflow

1. Add a new item or copy an old one into `queued_updates` folder in `%item_name%.json` format.
2. Make your changes to this file, or multiple files.
3. Do a pull request.
4. I'll review these changes and if everything is ok, i'll merge your request and merge all changes into the WFM database.
5. Then I will upload the new database dump to the `items` folder.

## File structure

### Common fields

1. `_id` - id of an item, do not modify it and do not create it (in case of addin a new item)
2. `tags` - not used right now in any way, butr it still prefarable to add them.
3. `icon` - local or remore path to the icon, check [This section](####Contributing-an-Icon)
4. `thumb` - Generated automatically.
5. `icon_format` - Generated automatically.
6. `sub_icon` - sub icon of an item, represent part of the set, like `handle` or `grip`, check [This section](####Sets)
7. `url_name` - Generated automatically.
8. `tradable` - This item is tradable. (`true`/`false`)
9. `part_of_set` - This item is part of the set. (`true`/`false`)
10. `set_root` - This item is set itself, like `Some Prime Set`, it's parrent of other parts.
11. `en` \ `ru` \ `ko` - lang specific fields
    1. `item_name` - Name of the item.
    2. `description` - item descriptrion.
    3. `wiki_link` - link to the wiki.
    4. `drop` - drop locations.
       1. `name` - Name of the location.
       2. `link` - link to the resource (wiki or wfm).
12. `trading_tax` - Tax

### Mod exclusive fields

1. `rarity` - Mod rarity.
2. `mod_max_rank` - Maximum possible rank

### Weapons, parts fields

1. `mastery_level` - mastery requirenments.
2. `ducats` - Cost in ducats.

### Contributing an Icon

From the remote source:  
`"icon": "remote://<direct_link_to_image>"`

From icon folder:  
`"icon": "local://items/icons/<icon_file>"`

### Sets

If you want to add set, just create set of files, and put `"part_of_set" : true`  
Our script will do the rest (link DB-documents with eachother)

**For Example, Aklex**  
You just need to create:

1. `Aklex Prime Blueprint.json`
2. `Aklex Prime Link.json`
3. `Aklex Prime Set.json`

### Tags

There is no strict convention, but you can use this logic:

1. Add item group, like `Blueprint` | `Mod`.
2. Add item type, like `Rifle` | `Warframe`.
3. Add additional definition, like `Prime` | `Corrupted` | `Huras`, `Rare`, etc.

For example Rare Rifle Mod should have `[Mod, Rifle, Rare]` tags.

## Contribute a new Language

Currently i can support only `en` and `ru` localizations.

> If you want to add another language, be sure that you will be able to finish your work.  
> There is 2600+ items in WFM database, this could be a tough task.

It's preferable to contribute translation for all items at once.

Use one of [this](https://www.w3schools.com/tags/ref_language_codes.asp) lang codes, to add a new translation.