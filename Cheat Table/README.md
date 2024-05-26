# SSHD Cheat Table

## Watchlist

This cheat table includes the address offsets for the following in-game
information:
<details>
<summary>Player</summary>
<blockquote>

* Stamina
* Position
* Angle
* Forward Speed
* Velocity
* Several misc attributes

</blockquote>
</details>

<details>
<summary>GameReloader</summary>
<blockquote>

* Trigger Reload
* Speed after Reload
* Stamina after Reload
* Item to use after Reload
* Beedle Shop Spawn State
* Action Index
* Area Type
* Is Reloading
* Prevent Set Spawn Info
* Countdown after Spawn

</blockquote>
</details>

<details>
<summary>Stage (current and next)</summary>
<blockquote>

* Stage
* Layer
* Room
* Entrance
* Night
* Trial
* Transition Type (unused for current)
* Fade Frames

</blockquote>
</details>

<details>
<summary>File Manager</summary>
<blockquote>

  <details>
  <summary>FA offset</summary>
  <blockquote>

  * Player Name
  * Current Health
  * Health Capacity
  * Storyflags
  * Sceneflags
  * Tempflags
  * Zoneflags
  * Itemflags
  * Dungeonflags
  * Enemy Kill Counters
  * Hit by Enemy Counters
  * Skykeep Puzzle
  * Selected B-Wheel Slot
  * Selected Pouch Slot
  * Selected Dowsing Slot

  </blockquote>
  </details>

* FB offset
* Amiibo Position
* Amiibo Stage
* Options
* Camera Speed

</blockquote>
</details>

<details>
<summary>Static Flags</summary>
<blockquote>

* Storyflags
* Sceneflags
* Tempflags
* Zoneflags
* Itemflags
* Dungeonflags
* Tboxflags
* Skipflags
* Enemy Defeat Flags

</blockquote>
</details>

<details>
<summary>Items and Counters</summary>
<blockquote>

  <details>
  <summary>Counters</summary>
  <blockquote>

  * Rupee Counter
  * Bomb Counter
  * Arrow Counter
  * Deku Seed Counter
  * Crystal Counter
  * ET Key Piece Counter

  </blockquote>
  </details>

  <details>
  <summary>B-Wheel Items</summary>
  <blockquote>

  * Bow
  * Iron Bow
  * Sacred Bow
  * Bomb Bag
  * Beetle
  * Hook Beetle
  * Quick Beetle
  * Tough Beetle
  * Slingshot
  * Scattershot
  * Clawshots
  * Whip
  * Gust Bellows

  </blockquote>
  </details>

  <details>
  <summary>Inventory Items</summary>
  <blockquote>

  * Sailcloth
  * Water Dragon's Scale
  * Fireshield Earrings
  * Digging Mitts
  * Mogma Mitts
  * Goddess's Harp
  * Medium Wallet
  * Big Wallet
  * Giant Wallet
  * Tycoon Wallet
  * Adventure Pouch

  </blockquote>
  </details>

  <details>
  <summary>Swords (requires reload)</summary>
  <blockquote>

  * Practice Sword
  * Goddess Sword
  * Goddess Longsword
  * Goddess White Sword
  * Master Sword
  * True Master Sword

  </blockquote>
  </details>

</blockquote>
</details>

<details>
<summary>Actor Globals</summary>
<blockquote>

* dBase::param1
* dAcBase::param2
* dBase::actorid
* dBase::groupType
* dAcBase::subtype
* dAcOBase::infoPtr
* ACTOR_PARAM_POS_PTR
* ACTOR_PARAM_ROT_PTR
* ACTOR_PARAM_SCALE_PTR
* ACTOR_SPAWN_WITH_REF
* ACTOR_STAGE_OBJECT_FLAG
* ACTOR_VIEW_CLIP_INDEX

</blockquote>
</details>

<details>
<summary>InputMgr</summary>
</details>

<details>
<summary>RESPAWN_TYPE</summary>
</details>

## Important Notes

This cheat table works in a similar way to Dolphin's watchlists. If you are
familiar with Cheat Engine, just use the `.CT` file like any other. It will
take ~30 seconds to find the base address to calculate the absolute addresses
from the relative ones in the `.CT` file. Open the file without the game open
to bypass this load time.

### Cheat Engine Bug

If you lock two or more values and then try to modify any value, Cheat Engine
will become unresponsive and the popup dialog used to change the value will
refuse to close. The only solution in this case is to completely close Cheat
Engine and re-open it.

## How to

### Emulators

Cheat Engine runs on desktop operating systems and therefore this cheat table
needs to be used with a Nintendo Switch emulator that can run The Legend of
Zelda: Skyward Sword HD. Specifically, this cheat table has been created and
tested using the [Yuzu Emulator](https://yuzu-emu.org/downloads). The cheat
table should work with other emulators but this hasn't been tested and your
mileage may vary.

### Using Cheat Engine

The cheat table is for use with the Cheat Engine program. You can get Cheat
Engine from here: https://cheatengine.org/downloads.php

Once you have installed and opened Cheat Engine, you will need to enable the
`MEM_MAPPED` setting. To do this, go to:

`Edit -> Settings -> Scan Settings`

![The Cheat Engine Settings menu showing the MEM_MAPPED option](https://raw.githubusercontent.com/mint-choc-chip-skyblade/sshd-cheat-table/main/Cheat%20Table/assets/MEM_MAPPED.png)

Next, ensure that your emulator is running the game and open the process in
Cheat Engine:

`File -> Open Process`

![The Cheat Engine Open Process menu with The Legend of Zelda: Skyward Sword HD yuzu process selected](https://raw.githubusercontent.com/mint-choc-chip-skyblade/sshd-cheat-table/main/Cheat%20Table/assets/process-list.png)

Finally, open the cheat table:

`File -> Load` and select the `.CT` file

Cheat Engine and the emulator will hang and become unresponsive for about 30
seconds. This is a due to the `MEM_MAPPED` setting and it is being used to
search through the memory of the emulator process to find the start of the
game code. Once the base address has been found, the various address offsets
will be updated to use the base address and the different attributes should
now be visible.

You can now use the cheat table to observe how the different values change as
you play the game - just like a Dolphin Memory Engine watchlist :p
