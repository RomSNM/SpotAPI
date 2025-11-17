# 🎵 Spotify Playlist Generator by Genre

This Python project allows you to generate a Spotify playlist with 10 songs from a genre of your choice. It's a simple and fun way to discover music based on your favorite styles — fully automated using the Spotify Web API.

## 🚀 Features

- 🔎 Search for songs by genre  
- 🎧 Automatically creates a playlist on your Spotify account  
- ➕ Adds 10 tracks to the playlist  
- ✅ Uses OAuth2 for secure authentication  

## 🛠️ Technologies Used

- Python 3  
- [Spotipy](https://spotipy.readthedocs.io/en/2.22.1/)  
- [python-dotenv](https://pypi.org/project/python-dotenv/)  

## 🧰 Installation

### 1. Clone the repository

```bash
git clone [(https://github.com/RomSNM/SpotAPI/tree/main)]
cd spotify-genre-playlist
```

### 2. Install the dependencies

```bash
pip install -r requirements.txt
```

### 3. Create your `.env` file

Create a file named `.env` in the root directory with the following content:

```env
SPOTIPY_CLIENT_ID=your_client_id
SPOTIPY_CLIENT_SECRET=your_client_secret
SPOTIPY_REDIRECT_URI=http://localhost:8888/callback
```

Get your credentials from the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).

### 4. Run the script

```bash
python main.py
```

## 💡 Example Usage

```python
generate_playlist("jazz swing", "Swingin'")
```

This will create a playlist named **Swingin'** with 10 songs from the **jazz swing** genre.

## 📸 Thumbnail

![Spotify Genre Playlist Generator](thumbnail.png)

## 📄 License

MIT License.
