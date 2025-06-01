# Problem 8-1: Favorite Radio Station
def tune_in(station):
    print(f"Let me tune in {station}.")

favorite_station = input("What is your favorite radio station? ")
tune_in(favorite_station)

print("\n" + "-"*40 + "\n")

# Problem 8-2: Business Cards Function
def print_business_cards(name, quantity, tag_line):
    print(f"Printing {quantity} business cards for {name}. Tagline: \"{tag_line}\"")

print_business_cards("Alice Johnson", 200, "Design with Impact")
print_business_cards("Bob Smith", 100, "Built to Lead")
print_business_cards("Cathy Lee", 300, "Innovation Starts Here")

print("\n" + "-"*40 + "\n")

# Problem 8-3: Default Quantity
def print_business_cards_default(name, tag_line, quantity=100):
    print(f"Printing {quantity} business cards for {name}. Tagline: \"{tag_line}\"")

print_business_cards_default("David King", "Smart Solutions", 150)
print_business_cards_default("Emily Turner", "Driven by Passion")

print("\n" + "-"*40 + "\n")

# Problem 8-4: Song Info with Default Artist
def song_info(title, artist="Unknown"):
    return f"{title} by {artist}."

print(song_info("Imagine", "John Lennon"))
print(song_info("Bohemian Rhapsody", "Queen"))
print(song_info("Untitled Track"))

print("\n" + "-"*40 + "\n")

# Problem 8-5: Playlist with Dictionary
def create_song(title, artist="Unknown"):
    return {"title": title, "artist": artist}

def display_playlist(playlist):
    print("\nYour Playlist:")
    for song in playlist:
        print(f"{song['title']} by {song['artist']}")

playlist = []

while True:
    title = input("Enter song title (or type 'done' to finish): ")
    if title.lower() == "done":
        break
    artist = input("Enter artist (leave blank for 'Unknown'): ")
    song = create_song(title, artist) if artist.strip() else create_song(title)
    playlist.append(song)

display_playlist(playlist)
