# cypto functions with lots of print statements to help comprehension.

def brute_keysize(cipherbytes):
    """
    Use statistical analysis to try to determine the length (in bytes) of a
    repeating key that was used to encrypt the given cipher text. Returns a
    list of the best 5 guesses, in descending order of likelihood.
    """
    distances = []
    for keysize in range(2, 100):
        print("Keysize: {}".format(keysize))
#        chunks = [cipherbytes[keysize*n:keysize*(n+1)] for n in range(0,4)]
        chunks = []
        for n in range(0, 4):
            print("n is {}".format(n))
            print("Indexing: {}:{}".format(keysize*n, keysize*(n+1)))
            a = cipherbytes[keysize*n:keysize*(n+1)]
            print("Indexed Text: {}".format(a))
            chunks.append(a)
        print("Chunks: {}".format(chunks))
        print("Chunks[1:] {}".format(chunks[1:]))
        if len(chunks[-1]) < keysize:
            # Cipher text isn't long enough to discover a key this big.
            break
        ds = list(starmap(get_hamming_distance, zip(chunks, chunks[1:])))
        print("ds {}".format(ds))
        # Normalized distance to keysize
        avg_distance = float(sum(ds))/len(ds)/keysize
        print("Ave distance: {}\n".format(avg_distance))
        distances.append((keysize, avg_distance))
    print("Distances before sorted: {}\n".format(distances))
    distances = sorted(distances, key=lambda item: item[1])
    print("Distances after sorted: {}\n".format(distances))
    return [item[0] for item in distances[:5]]
