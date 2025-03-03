# La funcion toma un directorio (objeto "playlist_in") donde se encuentren las listas de reproduccion exportadas desde 
#   Itunes (archivos .m3u), le modifica el path a cada renglon (los renglones indican donden estan los archivos de audio 
#   con las canciones de la lista) por un path relativo "../cancion123.mp3" y los guarda en la carpeta indicada por (objeto "playlist_out").
# Una vez que se crean estos archivos .m3u nuevos, hay que guardarlos en una carpeta nueva que esté adentro de la 
#   carpeta en donde se guarde toda la música en el celular. Una vez que están copiados así en el celular, hay que ir al
#   reproductor de audio del celular (ej. Samsung music) a que identifique estos archivos como listas de reproducción y listo.

# TO DOs:
# - Hacer que esto sea una funcion con (al menos) 2 parametros

import os

def modify_m3u_files(playlists_dir_in=r'C:\Users\Usuario\Music\Musica JB\itunes_playslist_for_android\in', 
                     playlists_dir_out=r'C:\Users\Usuario\Music\Musica JB\itunes_playslist_for_android\out'):
    """
    Modifies m3u files by changing the directory of each line that points to an audio file to a relative directory.

    Args:
        playlists_dir_in (str): The input directory containing the m3u files.
        playlists_dir_out (str): The output directory where modified m3u files will be saved.

    Returns:
        None
    """

    if playlists_dir_in is None:
        playlists_dir_in = input("Enter the input directory containing the m3u files: ")

    if playlists_dir_out is None:
        playlists_dir_out = input("Enter the output directory where modified m3u files will be saved: ")

    m3u_files = [f for f in os.listdir(playlists_dir_in) if f.endswith(".m3u")]

    for file in m3u_files:
        print(f"Modifying file: {file}")
        file_in = os.path.join(playlists_dir_in, file)
        file_out = os.path.join(playlists_dir_out, file)
        # with open(file_in, "rt", encoding="cp1252") as f:  # Changed encoding to cp1252
        with open(file_in, "rt", encoding="utf8", errors="ignore") as f:
            with open(file_out, "w", encoding="utf8") as f1:
                # f1.write("#EXTM3U\n")  # Uncomment if needed
                for line in f:
                    if not line.startswith("#"):
                        song_name = line.strip().split("\\")[-1]
                        line_output = "../musica_de_juan/" + song_name + "\n"
                        f1.write(line_output)
                    else:
                        f1.write(line)  # Include lines that start with '#' if needed

# Allowing interactive input if running in console
if __name__ == "__main__":
    modify_m3u_files()
