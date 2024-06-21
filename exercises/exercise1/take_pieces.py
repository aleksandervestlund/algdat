def take_pieces(n_pieces: int) -> int:
    return max(1, (n_pieces - 1) % 8)
