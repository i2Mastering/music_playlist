# SpamJamz Music Playlist

## Description
The SpamJamz Music Playlist is a Python-based interactive program that allows users to manage their music playlist. Users can:
- View the current playlist.
- Search for songs in the playlist.
- Add new songs to the playlist.
- Remove songs from the playlist.

This program provides an easy-to-use interface for interacting with a predefined song collection while allowing modifications.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Functions](#functions)
- [Requirements](#requirements)
- [License](#license)

## Features
- Displays an existing playlist.
- Allows users to search for songs.
- Adds user-specified songs along with artist details.
- Removes songs from the playlist.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/spamjamz-playlist.git
   ```
2. Navigate to the project directory:
   ```sh
   cd spamjamz-playlist
   ```
3. Ensure Python 3.x is installed on your system.

## Usage
1. Run the script:
   ```sh
   python music_playlist.py
   ```
2. Follow the prompts to:
   - View the playlist.
   - Search for songs.
   - Add new songs.
   - Delete songs from the playlist.

## Example
```sh
Thank you for adding our playlist to your profile...
Would you like to display the list? YES
Purple Lamborghini - Skrillex
Lean Back - Fat Joe
...
Would you like to search for songs on the playlist? YES
Type the song you would like to search: Work
Work by Drake is on the playlist.

Type in the song you would like to add: Starboy
Enter the artist name: The Weeknd
Added Starboy by The Weeknd to the playlist.

What song do you want to delete from the list: Lean Back
Lean Back has been removed from the playlist.
```

## Functions
- **`dictPrint()`**: Displays the full playlist.
- **`spamJamz2024()`**: Shows a welcome message.
- **`displayDict()`**: Displays or searches for songs in the playlist.
- **`userJamz2024()`**: Adds new songs to the playlist.
- **`sjDel2024()`**: Removes a song from the playlist.
- **`sjPrint()`**: Prints the updated playlist.

## Requirements
- Python 3.x

## License
This project is licensed under the MIT License.
