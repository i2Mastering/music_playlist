"""
Module for managing a music playlist, allowing users to view, add, and delete songs.

This script initializes a playlist with predefined songs and their respective artists. It provides functionalities to:
- Display the current playlist.
- Search for a song in the playlist.
- Add new songs to the playlist.
- Remove songs from the playlist.

Classes:
    - SpamJamzPlaylist: Handles all playlist operations including viewing, searching, adding, and deleting songs.

Functions:
    - dictPrint(): Prints the current playlist.

Example Usage:
    $ python music_playlist.py
    Thank you for adding our playlist to your profile...
    Would you like to display the list? YES
    Purple Lamborghini - Skrillex
    Lean Back - Fat Joe
    ...

Author: Ike Iloegbu
License: MIT
"""

import time

# Initialize the playlist dictionary
SpamJamz = {
    'Purple Lamborghini': 'Skrillex',
    'Lean Back': 'Fat Joe',
    'Monster': 'Paramore',
    'Dirt off My Shoulders': 'Jay-Z',
    '10%': 'Kaytranada',
    'Work': 'Drake',
    'Drunk In Love': 'Beyonce',
    'Where is Your Boy': 'Fall Out Boy',
    'Bat Country': 'Avenged Sevenfold',
    'Around The World': 'Daft Punk'
}

# Print the playlist

def dictPrint():
    """Displays all songs in the playlist."""
    for song, artist in SpamJamz.items():
        print(f'{song} - {artist}')

class SpamJamzPlaylist:
    """
    A class that manages the playlist operations such as displaying, searching, adding, and deleting songs.
    """
    @staticmethod
    def spamJamz2024():
        """Displays a welcome message."""
        print('Thank you for adding our playlist to your profile. You can search, add, and delete songs of your choosing.')
    
    @staticmethod
    def displayDict():
        """Displays the playlist if the user opts in and allows searching for a song."""
        if input('Would you like to display the list (NO/YES)? ').upper() == 'YES':
            dictPrint()

        if input('Would you like to search for songs on the playlist (NO/YES)? ').upper() == 'YES':
            searchDict = input('Type the song you would like to search: ')
            if searchDict in SpamJamz:
                print(f'{searchDict} by {SpamJamz[searchDict]} is on the playlist.')
            else:
                print(f'{searchDict} is not in SpamJamz.')
    
    @staticmethod
    def userJamz2024():
        """Allows the user to add songs to the playlist."""
        while True:
            userInput = input("Type in the song you would like to add. Type 'EXIT' to move on: \n")
            if userInput.upper() == 'EXIT':
                break
            if userInput in SpamJamz:
                print(f"{userInput} by {SpamJamz[userInput]} is already on the playlist.")
            else:
                artistInput = input("Enter the artist name: ")
                SpamJamz[userInput] = artistInput
                print(f'Added {userInput} by {artistInput} to the playlist.')
    
    @staticmethod
    def sjDel2024():
        """Allows the user to delete a song from the playlist."""
        while True:
            songTitle = input('What song do you want to delete from the list: ')
            if songTitle not in SpamJamz:
                print('Song title not in playlist. Choose a song currently in the playlist:')
                dictPrint()
            else:
                del SpamJamz[songTitle]
                print(f'{songTitle} has been removed from the playlist.')
                break
    
    @staticmethod
    def sjPrint():
        """Displays the updated playlist after deletion."""
        print('\nUpdated Playlist:')
        dictPrint()

if __name__ == "__main__":
    SpamJamzPlaylist.spamJamz2024()
    SpamJamzPlaylist.displayDict()
    SpamJamzPlaylist.userJamz2024()
    SpamJamzPlaylist.sjDel2024()
    SpamJamzPlaylist.sjPrint()




