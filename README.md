# README #

> This is repo that contains Warframe.market item database in JSON format.

> Icon files is not included in that repo, you can find them :

> `Icons`: [Here](https://drive.google.com/open?id=0B0DCzCsWH1SrLU11WnI5SzhRZGM)

> `sub_icons`: [Here](https://drive.google.com/open?id=0B0DCzCsWH1SrbzlneXVrWmxTdms)

## Directories ##

#### queued_updates

All desirable changes belongs to this dir.

If some item need to be updated\added, just create file, like `%item_name%.json` inside this dir.

Then, that item will be verified and if all its fields is correct, it will be added into db and `items` directory, and then removed from this directory.

#### items

All items that presents in the Warframe.market DB. (json-format)

#### icons

Item icons, you can find them [Here](https://drive.google.com/drive/u/0/folders/0B0DCzCsWH1SrZ3hhcG1kVmg1RjA)
Leave this directory empty, except when you contribute an icon.

#### sub_icons

Sub-icons, used for Set parts, like:
1. Blade
2. Gauntlet
3. Grip
4. ...

## Contribution

Use Pull requests.

### Item Template

Inside this repo you can find file `template.json`

Use this file to contribute new item, this file contains all possible fields that you need to define.

You can remove empty \ null fields.

##### Mods exclusive fields
```
"rarity": "Rare",
"mod_max_rank": 3,
```

##### Parts exclusive fields
```
"mastery_level": 2,
"ducats": 1234,
```

##### Automatically generated fields

Do not define them.

1. `thumb`
2. `url_name`
3. `icon_format`
4. `set_root`
5. `part_of_set`

### How to contribute an Icon

When you filling json-template for some item, you can define Icon in 2 ways:

1. Define it as `remote://<direct_link_to_image>`

**Example:**
```
"icon": "remote://https://vignette2.wikia.nocookie.net/warframe/images/0/0e/VoidProjectionsGoldD.png/revision/latest?cb=20160709035734"
```
In this way my script will download this image, do necessary changes to it, and then record into DB.

2. Define it as `local://<path_to_image_relative_to_this_dir>`

**Example:**
```
"icon": "local://icons/ololo.png"
```
In this way my script will copy this image, do necessary changes to it, and then record into DB.

### Sets, how to

No need to define sets in some special way.
Just create all parts of set, and item that represent set itself.
All other work will be handled by the script.

**For Example, Aklex**:

You just need to create:

1. `Aklex Prime Blueprint.json`
2. `Aklex Prime Link.json`
3. `Aklex Prime Set.json`

### Tags, wtf.

Tags will be used for quick filtering user profile, like:
![Screenshot from 2016-10-31 18-00-12.png](https://bitbucket.org/repo/8EAodE/images/349767049-Screenshot%20from%202016-10-31%2018-00-12.png)

How to define them? 

There is no strict way to do so, but you can use this logic:

1. Add item group, like `Blueprint` | `Mod`.
2. Add item type, like `Rifle` | `Warframe`.
3. Add additional definition, like `Prime` | `Corrupted` | `Huras`, `Rare`, etc.

For example Rare Rifle Mod should have `[Mod, Rifle, Rare]` tags.

### Drop locations \ NPC

`link` - link to wiki about location \ NPC. 
`name` - Name of the location \ NPC. 

### Modifying an existing item.

If you want to modify existing item, copy appropriate file from `items` folder into `queues_changes` and do desirable changes.

**Do not remove `_id` filed**


### Contribute Language

Currently i can support only `en` and `ru` localization for all items.

> If you want to add another language, be sure that you can support it in future.

> In additional, you'll need to update all items at once via pull request.
I can't apply half done translation ^^

Use one of [this](https://www.w3schools.com/tags/ref_language_codes.asp) lang codes, to add new translation. 


## Contribution Workflow

1. New Item added into `queued_updates` folder as `%item_name%.json`-file.
2. Contributors do all necessary changes, contribute icon, provide translations, etc.
As result we should have correct `%item_name%.json`-file.
3. Admin reviews changes and apply updates to the Warframe.market DB.
4. New item will appear inside `items` folder, and new icon will be added to folder at Gdrive.